# Attendance Management System with Emotion Detection

## Overview

This Attendance Management System (AMS) is a web-based application designed to automate the process of tracking attendance. Developed using Flask, the system integrates Google Cloud Storage for image storage and leverages a third-party API for real-time emotion detection. The system not only records attendance but also analyzes the emotional state of attendees, providing valuable insights for educational or corporate environments.

## Features

- **Automated Attendance Tracking**: Users can check in by submitting their photo, name, and roll number.
- **Real-Time Emotion Detection**: Analyzes the submitted photos to detect emotions such as happiness, sadness, neutrality, etc.
- **Cloud Storage**: Utilizes Google Cloud Storage for secure and scalable image storage.
- **Data Analytics**: Provides emotional and attendance analytics to enhance understanding of user engagement and well-being.
- **User-Friendly Interface**: Responsive and intuitive web interface for easy interaction.

## System Architecture

The AMS is structured around a client-server model:
- **Frontend**: HTML, CSS, JavaScript for user interactions.
- **Backend**: Flask for handling requests and integrating with external services.
- **Storage**: Google Cloud Storage for storing images.
- **API Integration**: Third-party emotion detection API for analyzing facial expressions.

## Installation and Setup

### Prerequisites

- Python 3.x
- Google Cloud account with a storage bucket set up
- RapidAPI account for the emotion detection API

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/BhuwanAwasthi/attendance-management-system.git
    cd attendance-management-system
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Google Cloud Credentials**
    - Create a `credentials.json` file with your Google Cloud service account details.
    - Place the `credentials.json` file in the root directory of the project.

5. **Configure Environment Variables**
    Create a `.env` file in the root directory and add the following environment variables:
    ```plaintext
    GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
    BUCKET_NAME="your-google-cloud-bucket-name"
    RAPIDAPI_KEY="your-rapidapi-key"
    ```

6. **Run the Application**
    ```bash
    flask run
    ```

## Usage

### Accessing the Application

- Open a web browser and navigate to `http://127.0.0.1:5000/`.

### Submitting Attendance

1. Enter your name and roll number.
2. Capture a photo using the integrated webcam feature.
3. Click "Submit" to record your attendance and receive feedback on detected emotions.

### Downloading Reports

1. Enter your roll number in the "Download Your Report" section.
2. Click "Download Report" to retrieve your attendance and emotion data in CSV format.

## Deployment
URL: https://bhuwan1111.pythonanywhere.com/ 

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For questions or feedback, please contact bhuwanawasthi2021@gmail.com

