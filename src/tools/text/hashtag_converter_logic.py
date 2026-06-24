import string


def convert_text_to_hashtags(text: str) -> str:
    """Convert text to hashtags by prefixing each word with #.
    
    Removes punctuation and special characters from words.
    Returns a string where each cleaned word is prefixed with # and separated by spaces.
    """
    if not text or not text.strip():
        return ""
    
    words = text.split()
    cleaned_words = []
    
    for word in words:
        # Remove punctuation and special characters
        cleaned = "".join(char for char in word if char not in string.punctuation)
        # Only add if there's at least one alphanumeric character left
        if cleaned and any(char.isalnum() for char in cleaned):
            cleaned_words.append(cleaned)
    
    hashtags = [f"#{word}" for word in cleaned_words]
    return " ".join(hashtags)
