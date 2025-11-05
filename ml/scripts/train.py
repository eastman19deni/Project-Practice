from ultralytics import YOLO
import os

def main():
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../configs/dataset.yaml"))
    print(f"Используется dataset.yaml: {data_path}")

    model = YOLO('yolov8n.pt')
    model.train(
        data=data_path,
        epochs=50,
        imgsz=640,
        batch=16,
        project='../results',
        name='person_detection',
        exist_ok=True
    )

if __name__ == "__main__":
    main()
