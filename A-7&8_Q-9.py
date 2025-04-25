import re

def gujarati_tokenizer(text):
    # Define regex patterns for different token types
    patterns = {
        "url": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
        "email": r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}",
        "date": r"\b\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}\b",
        "number": r"\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b|\b\d+/\d+\b",
        "social_handle": r"@[A-Za-z0-9_]+",
        "punctuation": r"[.,!?;:()\[\]{}'""“”‘’]",
        "gujarati_word": r"[\u0A80-\u0AFF]+",
        "english_word": r"[A-Za-z]+"
    }
    
    # Combine patterns into a single regex
    combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())
    
    # Tokenize using regex
    tokens = []
    for match in re.finditer(combined_pattern, text, re.UNICODE):
        for key, value in match.groupdict().items():
            if value:
                tokens.append((key, value))
    
    return tokens

# Example usage:
# text = "આજનું તારીખ 12-03-2024 છે. મારા ઈમેલ abc@gmail.com છે અને વેબસાઇટ https://example.com છે!"  
text = input("Enter your text: \n")ed
tokens = gujarati_tokenizer(text)
print(tokens)
