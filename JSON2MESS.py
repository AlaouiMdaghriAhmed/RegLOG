import json

# Define the JSON file path
json_file_path = r"C:/Users/admin/Documents/GitHub/RegLOG/data/gen/parsed_Apache.json"

# Output file path
output_file = r"C:/Users/admin/Documents/GitHub/RegLOG/data/gen/messages.txt"

# Load the JSON data
with open(json_file_path, "r") as file:
    json_data = json.load(file)

# Extract messages
messages = [entry["message"] for entry in json_data]

# Save messages to a text file
with open(output_file, "w") as f:
    f.write("\n".join(messages))

print(f"Messages saved to {output_file}")
