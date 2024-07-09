import cv2
import numpy as np

# Function to detect and count vehicles
def detect_and_count_vehicles(video_path):
    cap = cv2.VideoCapture(video_path)

    # Create a background subtractor using MOG (Mixture of Gaussians) method
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Variables for vehicle counting
    total_vehicles = 0
    previous_frame = None

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Apply background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Apply morphological operations to remove noise and fill gaps in the foreground mask
        kernel = np.ones((5, 5), np.uint8)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)

        # Find contours in the foreground mask
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop through the contours
        for contour in contours:
            # Filter out small contours (noise)
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)

                # Draw a bounding box around the detected vehicle
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Check if the vehicle is moving from the top to bottom (change in y-coordinate)
                if previous_frame is not None:
                    if y > previous_frame[1]:
                        total_vehicles += 1

                previous_frame = (x, y, w, h)

        # Display the frame with detected vehicles and the count
        cv2.putText(frame, f"Total Vehicles: {total_vehicles}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Vehicle Detection', frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Specify the path to your video file
video_path = 'video.mp4'

# Call the function to detect and count vehicles
detect_and_count_vehicles(video_path)
