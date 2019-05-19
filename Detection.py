import face_recognition
import cv2
import os
from datetime import datetime
# Get a reference to webcam #0 (the default one)

def intrusion_fn(detect1):
    x = 0
    labels = []
    check = []
    image_pic = []
    known_face_encodings=[]
    known_face_names=[]

    for root, dirs, files in os.walk("IntrusionDetected"):
        num = len(files)

    for root, dirs, files in os.walk("Images"):
        for file in files:
            if file.endswith("jpg") or file.endswith("JPG"):
                path = os.path.join(root, file)
                label = os.path.basename(file).replace(" ", "-").lower()
                labels.append(label)
    for i in range (0,len(labels)):
        image_pic.append(face_recognition.load_image_file(str("Images/")+str(labels[i])))
    for i in range (0,len(labels)):
        known_face_encodings.append(face_recognition.face_encodings(image_pic[i])[0])
        known_face_names.append(labels[i][0:-4])

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    video_capture = cv2.VideoCapture(0)
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right+35, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom -35), (right+35, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, str(datetime.now()), (5, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)
        # print(face_names)
        item = "Unknown"
        if detect1 == 1:
            if x == 0:
                if len(face_names) != 0 and item not in face_names:
                    check = face_names
                    x = 1
                elif item in face_names:
                    cv2.imwrite(str("IntrusionDetected/Intrusion_") + str(num)+ str(".jpg"), frame)
                    num = num+1
            elif x == 1:
                if check == face_names:
                    x = 2
                else:
                    x = 0
            elif x == 2:
                if check == face_names:
                    break
                else:
                    x = 0
        # Hit 'q' on the keyboard to quit!
        elif detect1 == 0:
            if item in face_names:
                cv2.imwrite(str("IntrusionDetected/Intrusion_")+str(num)+str(".jpg"),frame)
                num = num+1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
