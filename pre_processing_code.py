!pip install roboflow

from roboflow import Roboflow
# Add your Roboflow API key here
rf = Roboflow(api_key="YOUR_ROBOFLOW_API_KEY")
project = rf.workspace("chaitra-cc6kt").project("my-first-project-upzwf")
version = project.version(4)
dataset = version.download("yolov8")

                
