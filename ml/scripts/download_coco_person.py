import fiftyone.zoo as foz
import fiftyone.utils.yolo as fouy

def main():
    print(" Загружаем COCO-2017 (только людей)...")
    dataset = foz.load_zoo_dataset(
        "coco-2017",
        split="train",
        label_types=["detections"],
        classes=["person"],
        max_samples=500,
    )

    print(" Экспортируем в YOLO формат...")
    export_dir = "datasets"
    fouy.export_yolo_detection_dataset(
        dataset,
        export_dir=export_dir,
        label_field="detections",
        split="train",
    )

    print(" Готово! Датасет сохранён в папке:")
    print(f"{export_dir}/train/images и {export_dir}/train/labels")

if __name__ == "__main__":
    main()
