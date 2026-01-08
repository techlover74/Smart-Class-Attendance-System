import face_recognition
import os

def load_known_faces(path="data/students/"):
    known_encodings = []
    known_names = []
    
    for file in os.listdir(path):
        img = face_recognition.load_image_file(os.path.join(path, file))
        encoding = face_recognition.face_encodings(img)[0]
        known_encodings.append(encoding)
        known_names.append(os.path.splitext(file)[0])  # filename = student name
    
    return known_encodings, known_names

def recognize_faces(frame, known_encodings, known_names):
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    recognized_students = []
    
    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        if True in matches:
            index = matches.index(True)
            recognized_students.append(known_names[index])
    
    return recognized_students
