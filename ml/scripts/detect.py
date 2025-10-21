from ultralytics import YOLO
import cv2

def main(image_path):
    model = YOLO('results/person_detection/weights/best.pt')
    results = model(image_path, show=True)  
    results[0].save('results/detected.jpg')
    print(" Результат сохранён в results/detected.jpg")

if __name__ == "__main__":
    main('datasets/test/images/example.jpg')