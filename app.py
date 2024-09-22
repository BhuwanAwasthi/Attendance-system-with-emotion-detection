from flask import Flask, request, jsonify, send_from_directory, send_file
import cloudinary
import cloudinary.uploader
from google.oauth2 import service_account
import requests, json, os
from datetime import datetime

import os
import cloudinary

# Flask App and Cloudinary Setup
app = Flask(__name__)

# Configure Cloudinary using environment variables
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# You can do the same for other API keys like RapidAPI:
rapidapi_key=os.getenv('RAPIDAPI_KEY')

DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'photo' not in request.files or 'rollNo' not in request.form:
        return jsonify({'error': 'Missing photo or roll number'}), 400

    photo = request.files['photo']
    name = request.form['name']
    roll_no = request.form['rollNo']
    
    # Upload the image to Cloudinary
    image_url = upload_image_to_cloudinary(photo, roll_no)
    if image_url is None:
        return jsonify({'error': 'Failed to upload image'}), 500

    emotion_data = detect_emotion(image_url)
    if emotion_data != 'Error':
        save_attendance_record(roll_no, name, image_url, emotion_data['emotion'], emotion_data['accuracy'])
        return jsonify({'message': 'Submission successful', 'rollNo': roll_no, **emotion_data}), 200
    else:
        return jsonify({'error': 'Emotion detection failed'}), 500

def upload_image_to_cloudinary(photo, roll_no):
    try:
        # Using Cloudinary uploader to upload image
        result = cloudinary.uploader.upload(photo, public_id=f"{roll_no}_{datetime.now().strftime('%Y%m%d%H%M%S')}")
        return result.get("url")  # Return the URL of the uploaded image
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None

def save_attendance_record(roll_no, name, image_url, emotion, accuracy):
    filepath = os.path.join(DATA_DIR, f'{roll_no}.json')
    record = {'rollNo': roll_no, 'name': name, 'image_url': image_url, 'emotion': emotion, 'accuracy': accuracy, 'date': datetime.now().strftime('%Y-%m-%d')}
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            json.dump([record], file, indent=4)
    else:
        with open(filepath, 'r+') as file:
            records = json.load(file)
            records.append(record)
            file.seek(0)
            json.dump(records, file, indent=4)
            file.truncate()

def detect_emotion(image_url):
    try:
        url = "https://emotion-detection2.p.rapidapi.com/emotion-detection"
        payload = {"url": image_url}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "rapidapi_key",
            "X-RapidAPI-Host": "emotion-detection2.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            emotions = response.json()
            if emotions:
                primary_emotion = emotions[0]['emotion']['value']
                probability = emotions[0]['emotion']['probability'] * 100
                return {'emotion': primary_emotion, 'accuracy': f"{probability:.2f}%"}
        return 'Error'
    except Exception as e:
        print(f"Exception calling emotion API: {e}")
        return 'Error'

import csv
import json
import os

def generate_csv(filepath):
    with open(filepath, 'r') as json_file:
        records = json.load(json_file)

    # Define a path for the CSV file
    csv_file_path = filepath.replace('.json', '.csv')

    # Define CSV columns
    columns = ['rollNo', 'name', 'image_url', 'emotion', 'accuracy', 'date']

    # Write the JSON data to a CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    return csv_file_path

@app.route('/download-report/<roll_no>', methods=['GET'])
def download_report(roll_no):
    filepath = os.path.join(DATA_DIR, f'{roll_no}.json')
    if os.path.exists(filepath):
        csv_file_path = generate_csv(filepath)
        return send_file(csv_file_path, as_attachment=True, download_name=f'{roll_no}_report.csv')
    else:
        return jsonify({'error': 'Report not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
