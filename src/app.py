import cv2
from detector import FaceDetector

def main():
    # Initialize the camera and detector
    cap = cv2.VideoCapture(0)
    detector = FaceDetector(min_detection_confidence=0.6)

    print("Starting Face Detection... Press 'q' to quit.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error: Could not read frame from webcam.")
            break

        # Process the frame to detect faces
        processed_frame = detector.process_frame(frame)

        # Display the result
        cv2.imshow('Face Detection Application', processed_frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    detector.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
