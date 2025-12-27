import json

file_path = 'My_Projects/Hard-Coded/Mini/Banglish-Dictionary/dictionary_data.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        # Loading into a dict automatically removes duplicates (keeps last one)
        data = json.load(f)
    
    print(f"Loaded {len(data)} unique words.")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Cleaned up duplicates and saved.")

except Exception as e:
    print(f"Error: {e}")
