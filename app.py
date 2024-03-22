from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/preferences', methods=['POST'])
def save_user_preferences():
    new_data = request.json
    print("Saving preferences:", new_data)
    
    file_path = 'user_preferences.json'
    
    # Initialize existing_data as an empty list
    existing_data = []
    
    # If file exists AND is not empty, load its content into existing_data
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    
    # Append the new data to the existing_data list
    print("Existing data before appending:", existing_data)
    existing_data.append(new_data)
    print("Existing data after appending:", existing_data)

    
    # Write the updated list back to the file
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)  # Added indent for readability
    
    return jsonify({"message": "Preferences saved successfully"}), 200

@app.route('/api/fetch-content', methods=['GET'])
def fetch_content():
    # This will later fetch and filter content based on preferences
    return jsonify({"content": "Placeholder for personalized content"}), 200

if __name__ == '__main__':
    app.run(debug=True)
