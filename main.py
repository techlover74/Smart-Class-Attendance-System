import cv2
from face_detection import detect_faces
from face_recognition import load_known_faces, recognize_faces
from attendance_logger import init_db, log_attendance
from notifier import notify_mentor

def main():
    init_db()
    known_encodings, known_names = load_known_faces()
    
    cap = cv2.VideoCapture(0)
    present_students = set()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        faces = detect_faces(frame)
        students = recognize_faces(frame, known_encodings, known_names)
        
        for student in students:
            if student not in present_students:
                present_students.add(student)
                log_attendance(student)
        
        cv2.imshow("Classroom Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    notify_mentor(list(present_students))

if __name__ == "__main__":
    main()
