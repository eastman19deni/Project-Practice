import cv2
from pathlib import Path
import numpy as np

class YoloModel:
    def __init__(self, cfg):
        self.cfg_path = cfg.get('cfg_path', 'models/yolov3.cfg')
        self.weights_path = cfg.get('weights_path', 'models/yolov3.weights')
        self.names_path = cfg.get('names_path', 'models/coco.names')
        self.conf_threshold = cfg.get('conf_threshold', 0.5)
        self.nms_threshold = cfg.get('nms_threshold', 0.4)

        self.net = cv2.dnn.readNetFromDarknet(self.cfg_path, self.weights_path)
        self.classes = self._load_names(self.names_path)
        self.output_layers = self._get_output_layers()

    def _load_names(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]

    def _get_output_layers(self):
        layer_names = self.net.getLayerNames()
        try:
            return [layer_names[i[0]-1] for i in self.net.getUnconnectedOutLayers()]
        except Exception:
            return [layer_names[i-1] for i in self.net.getUnconnectedOutLayers()]

    def detect(self, frame):
        H, W = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416,416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        class_ids, confidences, boxes = [], [], []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = int(np.argmax(scores))
                confidence = float(scores[class_id])
                if confidence > self.conf_threshold:
                    center_x = int(detection[0] * W)
                    center_y = int(detection[1] * H)
                    w = int(detection[2] * W)
                    h = int(detection[3] * H)
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    boxes.append([x,y,w,h])
                    confidences.append(confidence)
                    class_ids.append(class_id)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)
        detections = []
        if len(idxs) > 0:
            for i in idxs.flatten():
                x,y,w,h = boxes[i]
                cx = x + w//2
                cy = y + h//2
                detections.append({
                    'class_id': int(class_ids[i]),
                    'class_name': self.classes[int(class_ids[i])] if int(class_ids[i]) < len(self.classes) else str(class_ids[i]),
                    'score': float(confidences[i]),
                    'box': [int(x),int(y),int(w),int(h)],
                    'center': (int(cx), int(cy))
                })
        return detections
