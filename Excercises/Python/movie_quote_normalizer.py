# Python Exercise – Problem 1: Movie Quote Normalizer

## Goal
Write a function `normalize_quote(text) -> list[str]` that:
1. Converts all letters to lowercase  
2. Removes punctuation  
3. Collapses extra spaces  
4. Splits into individual words  

**Edge Cases:**
- If `text` is **not a string**, raise `TypeError`.  
- If `text` is empty or only whitespace, raise `ValueError`.  

---

## Annotated Solution
```python
import re  # Import Python's Regular Expressions module

def normalize_quote(text: str) -> list[str]:
    # Step 1: Ensure the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    
    # ---
    # Step 2: Check for empty or whitespace-only strings
    if not text.strip():
        raise ValueError("text is empty/whitespace")
    
    # ---
    # Step 3: Convert all characters to lowercase for consistency
    text = text.lower()
    
    # ---
    # Step 4: Replace punctuation with spaces
    # [^\w\s] = any character that is NOT a word char (\w) or whitespace (\s)
    text = re.sub(r"[^\w\s]", " ", text)
    
    # ---
    # Step 5: Split on spaces — split() automatically removes extra whitespace
    words = text.split()
    
    # ---
    # Step 6: Return the cleaned list of words
    return words
```
