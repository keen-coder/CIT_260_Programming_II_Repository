import re

text = "Wait... what?! Are you *serious*—right now?! (No way!) Well, I guess: 'Anything's possible,' she said—smiling. #unbelievable @everyone; check this out: www.example.com/path?query=value&sort=desc."


# Use a regex to substitute any character that is NOT A-Z, a-z, 0-9, or a whitespace character
# with the empty string ''
normalized_text = re.sub(r'[^A-Za-z0-9\s]', '', text)

print(normalized_text)