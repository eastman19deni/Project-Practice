import cv2

def draw_text(img, text, org, scale=0.6, color=(0,255,0), thickness=2):
    cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness, cv2.LINE_AA)

def visualize_frame(frame, detections, cfg):
    out = frame.copy()
    people = [d for d in detections if d['class_name']=='person']

    for d in people:
        x,y,w,h = d['box']
        cv2.rectangle(out, (x,y), (x+w,y+h), (0,255,0), 2)
        draw_text(out, f"{d['class_name']} {d['score']:.2f}", (x, y-6))

    desks = cfg.get('detection', {}).get('desks', [])
    desk_counts = []
    for i,desk in enumerate(desks):
        x1,y1,x2,y2 = desk['rect']
        cv2.rectangle(out, (x1,y1),(x2,y2),(255,0,0),2)
        cnt = 0
        for d in people:
            cx,cy = d['center']
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                cnt += 1
        desk_counts.append(cnt)
        draw_text(out, f"Desk {i+1}: {cnt}", (x1, y2+16))

    total = len(people)
    draw_text(out, f"Total people: {total}", (10,30))

    info = {'total': total, 'desk_counts': desk_counts}
    return out, info
