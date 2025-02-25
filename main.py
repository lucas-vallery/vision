import torch
import cv2

# Load the YOLOv5 model
model = torch.hub.load("./yolov5", "yolov5s", source="local")
model.eval()

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model([rgb_frame])

    # Parse results
    detections = results.xyxy[0].numpy()

    # Draw bounding boxes and labels
    for detection in detections:
        x1, y1, x2, y2, confidence, class_id = detection
        label = model.names[int(class_id)]
        color = (0, 255, 0)
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(frame, f"{label}: {confidence:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame
    cv2.imshow("YOLOv5 Object Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()