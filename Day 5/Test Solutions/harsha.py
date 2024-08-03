import re

def extract_characters(data):
    # Define the pattern to match alphabetic characters
    pattern = r'[a-zA-Z]+'
    # Find all sequences of alphabetic characters
    characters = re.findall(pattern, data)
    # Join the list into a single string
    return ''.join(characters)

# Example usage
random_data = input("enter the data:")
extracted_chars = extract_characters(random_data)
print(extracted_chars)  # Output will be 'abcdef'