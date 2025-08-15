def parse_csvish_numbers(text: str) -> tuple[int, int]:
    """
    Parse a multiline string containing comma-separated integers and
    return (total_sum, bad_lines).

    Rules:
      - Ignore blank lines.
      - Sum every valid integer token.
      - If a line contains at least one non-integer token, count that line once in bad_lines
        but still add any valid integers from that same line.

    Raises:
      - TypeError if text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    total = 0
    bad_lines = 0

    # Iterate line-by-line to apply per-line error counting
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:  # Skip empty/whitespace-only lines completely
            continue

        line_had_error = False  # Track whether this line contained any bad token

        # Split by commas; allow spaces around numbers (e.g., " 10 , 20 ")
        for token in line.split(','):
            token = token.strip()
            if token == "":
                # Empty token (e.g., trailing comma). Treat as error and continue.
                line_had_error = True
                continue
            try:
                total += int(token)
            except ValueError:
                # Not an integer; mark the line as bad but keep parsing the rest
                line_had_error = True
                continue

        if line_had_error:
            bad_lines += 1

    return total, bad_lines

# Quick sanity check based on the prompt example
sample = "10,20
x,2
5
"
print(parse_csvish_numbers(sample))  # (37, 1)