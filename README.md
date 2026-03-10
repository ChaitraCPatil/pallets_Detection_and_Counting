Pallets Detection and Counting using YOLOv8

Project Overview
This project builds an AI-based computer vision system that automatically detects and counts pallets from warehouse images. The system uses a custom-trained YOLOv8 object detection model and provides an interactive web application using Streamlit.

The main goal of the project is to automate pallet counting in warehouses, which helps reduce manual effort and improve inventory management efficiency.

Business Problem
In warehouse environments, pallet counting is usually performed manually. This process is:
Time-consuming
Prone to human errors
Inefficient for large warehouses
Manual counting can lead to incorrect inventory tracking and operational delays.

Solution
To solve this problem, a deep learning object detection model was trained to detect pallets from images.
The system performs the following tasks:
Accepts an image input from the user
Detects pallets using a trained YOLOv8 model
Displays bounding boxes around detected pallets
Automatically counts the number of pallets
A Streamlit web application was developed to make the system easy to use.

Dataset

The dataset was created and managed using Roboflow.

Dataset Details:
Images: 200+ pallet images
Annotation Tool: Roboflow
Dataset Format: YOLOv8
Class Label: Pallet

Images were annotated with Polygon Tool to train the object detection model.

Model Training
The object detection model was trained using YOLOv8.
Training Configuration:
Model: YOLOv8n
Epochs: 30
Image Size: 640
Batch Size: 16

Training was performed using Google Colab.

The final trained model weights are saved as:

best.pt
Project Workflow
Dataset Collection
        ↓
Image Annotation (Roboflow)
        ↓
Dataset Export (YOLOv8 Format)
        ↓
Model Training (YOLOv8)
        ↓
Model Weights Generated (best.pt)
        ↓
Streamlit Web Application
        ↓
Upload Image
        ↓
Pallet Detection and Counting
Features

Automated pallet detection from images
Real-time object detection
Pallet counting functionality
Interactive web interface using Streamlit
Bounding box visualization of detected pallets

Project Structure

pallets_detection_and_counting

README.md
app.py
requirements.txt

best.pt

pallets_detection_and_counting_263.py
pre_processing_code.py

Technologies Used

Python
YOLOv8
Streamlit
Roboflow
NumPy
Pillow
Google Colab

Installation
Clone the repository:
git clone https://github.com/your-username/pallets_detection_and_counting.git
Move into the project directory:
cd pallets_detection_and_counting

Install dependencies:

pip install -r requirements.txt
Run the Application

Start the Streamlit application:
streamlit run app.py

After running the command, the web interface will open in your browser.

Steps:
1 Upload an image
2 The model detects pallets
3 Bounding boxes are displayed
4 The system shows the total pallet count

Dataset Download (Important)

To download the dataset using Roboflow, open:

pre_processing_code.py

Replace the API key with your own Roboflow API key:

rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
Sample Output

The system displays:

Uploaded image
Detected pallets with bounding boxes
Detection summary
Total pallet count

Future Improvements
Real-time pallet detection using CCTV cameras
Video-based pallet tracking
Integration with warehouse management systems
Deployment on edge devices for industrial use

Author

Chaitra Patil
Data Science Student – 360DigiTMG
