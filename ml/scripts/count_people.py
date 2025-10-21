from ultralytics import YOLO

def count_people(image_path):
    model = YOLO('results/person_detection/weights/best.pt')
    results = model(image_path)
    boxes = results[0].boxes
    count = len(boxes)
    print(f" На изображении найдено {count} человек")
    return count

if __name__ == "__main__":
    count_people('datasets/test/images/example.jpg')