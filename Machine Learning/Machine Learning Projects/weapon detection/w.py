import cv2
import numpy as np

# Load YOLOv3 model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load COCO labels
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Load image
image = cv2.imread("test_image.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Create a blob from the image (preprocessing)
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

# Set the input to the YOLO network
net.setInput(blob)

# Get output layer names
layer_names = net.getUnconnectedOutLayersNames()

# Run forward pass
outputs = net.forward(layer_names)

# Initialize lists for detected objects, their bounding boxes, and confidences
detections = []
boxes = []
confidences = []

# Minimum confidence threshold for detection
conf_threshold = 0.5

# Loop over each output layer
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > conf_threshold:
            # Scale the bounding box coordinates to the original image size
            box = detection[0:4] * np.array([width, height, width, height])
            (center_x, center_y, box_width, box_height) = box.astype("int")

            # Calculate the top-left corner of the bounding box
            x = int(center_x - (box_width / 2))
            y = int(center_y - (box_height / 2))

            boxes.append([x, y, int(box_width), int(box_height)])
            confidences.append(float(confidence))
            detections.append(class_id)

# Apply non-maximum suppression to remove overlapping boxes
nms_threshold = 0.3
indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

# Check if any object was detected
if len(indices) > 0:
    for i in indices.flatten():
        label = str(classes[detections[i]])
        confidence = confidences[i]
        (x, y, w, h) = boxes[i]

        # Draw bounding box and label on the image
        color = (0, 255, 0)  # Green color for the bounding box
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        text = f"{label}: {confidence:.2f}"
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Display the output image
cv2.imshow("Weapon Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
