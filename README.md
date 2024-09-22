# Attendance Management System with Emotion Detection

## Overview
This Attendance Management System (AMS) is a web-based application designed to automate the process of tracking attendance. Developed using Flask, the system integrates **Cloudinary** for image storage and leverages a third-party API from **RapidAPI** for real-time emotion detection. The system not only records attendance but also analyzes the emotional state of attendees, providing valuable insights for educational or corporate environments.

## Features
- **Automated Attendance Tracking**: Users can check in by submitting their photo, name, and roll number.
- **Real-Time Emotion Detection**: Analyzes the submitted photos to detect emotions such as happiness, sadness, neutrality, etc.
- **Cloud-Based Image Storage**: Utilizes Cloudinary for secure and scalable image storage.
- **Data Analytics**: Provides emotional and attendance analytics to enhance understanding of user engagement and well-being.
- **User-Friendly Interface**: Responsive and intuitive web interface for easy interaction.
- **Downloadable Reports**: Users can download their attendance and emotion history in CSV format.

## System Architecture
The AMS is structured around a client-server model:
- **Frontend**: HTML, CSS, and JavaScript for user interaction, with webcam integration to capture photos.
- **Backend**: Flask handles requests, stores attendance records, and integrates with external services for emotion detection and image storage.
- **Storage**: Cloudinary is used for storing and retrieving images.
- **API Integration**: RapidAPI's emotion detection API is used for analyzing facial expressions.

## Installation and Setup

### Prerequisites
- Python 3.x
- Cloudinary account for image storage
- RapidAPI account for the emotion detection API

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BhuwanAwasthi/attendance-management-system.git
   cd attendance-management-system
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Cloudinary and RapidAPI Credentials**
   - Create a `.env` file in the root directory and add the following environment variables:
     ```plaintext
     CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
     CLOUDINARY_API_KEY=your_cloudinary_api_key
     CLOUDINARY_API_SECRET=your_cloudinary_api_secret
     RAPIDAPI_KEY=your_rapidapi_key
     ```

5. **Run the Application**
   ```bash
   flask run
   ```

## Usage

### Accessing the Application
- Open a web browser and navigate to `http://127.0.0.1:5000/`.

### Submitting Attendance
- Enter your **name** and **roll number**.
- Capture a photo using the integrated webcam feature.
- Click **"Submit"** to record your attendance and receive feedback on detected emotions.

### Downloading Reports
- Enter your **roll number** in the "Download Your Report" section.
- Click **"Download Report"** to retrieve your attendance and emotion data in CSV format.

## Deployment

### Live Deployment
- The application is deployed and accessible at:
  [https://attendance-system-with-emotion-detection.onrender.com](https://attendance-system-with-emotion-detection.onrender.com)

## Technology Stack
- **Frontend**: HTML, CSS (with animations), JavaScript
- **Backend**: Flask (Python)
- **Image Storage**: Cloudinary
- **Emotion Detection**: RapidAPI (Emotion Detection API)
- **Web Hosting**: Render

## Contributing

We welcome contributions from the community! To contribute:
1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -am 'Add new feature'`).
4. **Push to the branch** (`git push origin feature-branch`).
5. **Create a Pull Request**.

## Contact

For questions or feedback, please contact **bhuwanawasthi2021@gmail.com**.

