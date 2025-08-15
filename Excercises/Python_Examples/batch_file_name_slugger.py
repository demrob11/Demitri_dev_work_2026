from pathlib import Path  # Easier/safer filename parsing
import re                  # Pattern-based cleanup

def slugify_filenames(items):
    """
    Convert a list of filenames to safe, unique slugs.

    Args:
        items (list): Filenames (strings). Non-strings are skipped.
    Returns:
        slugs (list[str]): Cleaned, unique filenames.
        errors (int): Count of inputs that were not strings.
    """
    slugs = []
    errors = 0
    seen = {}  # maps base slug (w/ extension) -> count

    for item in items:
        # 1) Validate input type
        if not isinstance(item, str):
            errors += 1
            continue

        # 2) Normalize casing and pull just the filename portion
        p = Path(item)
        name = p.name.lower()  # lower entire name first

        # 3) Separate stem and extension; keep only the LAST suffix
        stem, ext = Path(name).stem, Path(name).suffix  # ext includes the dot or ''

        # 4) Replace spaces with '-' first (so they don't vanish)
        stem = stem.replace(" ", "-")

        # 5) Remove any character that is NOT a-z, 0-9, or '-' using regex
        #    Keep dashes; drop everything else (e.g., parentheses, commas)
        stem = re.sub(r"[^a-z0-9-]", "", stem)

        # 6) Collapse repeated dashes and trim leading/trailing dashes
        stem = re.sub(r"-+", "-", stem).strip("-")

        # 7) Reassemble candidate slug with original extension (already lowercased)
        candidate = f"{stem}{ext}"

        # 8) Ensure uniqueness by appending -2, -3, ... for collisions
        if candidate not in seen:
            seen[candidate] = 1
            slugs.append(candidate)
        else:
            seen[candidate] += 1
            unique = f"{stem}-{seen[candidate]}{ext}"
            slugs.append(unique)

    return slugs, errors