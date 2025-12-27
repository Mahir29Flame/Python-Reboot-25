from collections import Counter
import re

file_path = 'My_Projects/Hard-Coded/Mini/Banglish-Dictionary/dictionary_data.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all keys using regex
    keys = re.findall(r'"([^"]+)":', content)
    
    counts = Counter(keys)
    duplicates = {k: v for k, v in counts.items() if v > 1}
    
    print(f"Total keys found: {len(keys)}")
    print(f"Duplicate keys count: {len(duplicates)}")
    
    if duplicates:
        print("Duplicate words:")
        for word, count in duplicates.items():
            print(f"  - {word}: {count} times")
    else:
        print("No duplicates found in the file.")

except Exception as e:
    print(f"Error: {e}")
