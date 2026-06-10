import cv2
import numpy as np
import os

class FinalSelfCorrectingSystem:
    def __init__(self, det_size=(256, 256)):
        print("[1/4] Loading AI Model Architecture into Memory...")
        from insightface.app import FaceAnalysis
        self.app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
        self.app.prepare(ctx_id=0, det_size=det_size)
        self.known_face_embeddings = {}

    def auto_register_images(self):
        # We create a dedicated clean folder inside your Pandas app directory
        project_folder = r"C:\Users\UDAYPATNALA\OneDrive\Documents\Pandas app\faces"
        supported_formats = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
        
        if not os.path.exists(project_folder):
            print(f"\n[ALERT] Creating a dedicated image folder at: {project_folder}")
            os.makedirs(project_folder, exist_ok=True)
            print("👉 ACTION REQUIRED: Please drop your uday.jpg, deva.jpg, jhansi.jpg, and acharya.jpg files directly into that new 'faces' folder!")
            return

        files = os.listdir(project_folder)
        print(f"\n[2/4] Scanning folder: {project_folder}")
        print(f"[INFO] Files found inside 'faces' directory: {files}")
        
        for filename in files:
            if filename.lower().endswith(supported_formats):
                full_image_path = os.path.join(project_folder, filename)
                formatted_name = os.path.splitext(filename)[0].strip().capitalize()
                
                img = cv2.imread(full_image_path)
                if img is None:
                    print(f" -> [ERROR] Cannot read file: {filename}")
                    continue
                
                detected_faces = self.app.get(img)
                if len(detected_faces) == 0:
                    print(f" -> [SKIP] '{filename}' - Found image file, but the AI cannot see a face in it. Make sure it's a clear headshot.")
                    continue
                
                self.known_face_embeddings[formatted_name] = detected_faces[0].embedding
                print(f" -> [SUCCESS] Registered Identity: '{formatted_name}'")

        print(f"[SUCCESS] Final database size: {len(self.known_face_embeddings)} faces loaded successfully.\n")

    def compare_live_face(self, live_embedding, threshold=0.4):
        if not self.known_face_embeddings:
            return "Unknown"
        closest_match = "Unknown"
        lowest_distance = float('inf')
        for name, saved_emb in self.known_face_embeddings.items():
            dot_prod = np.dot(live_embedding, saved_emb)
            norm_a = np.linalg.norm(live_embedding)
            norm_b = np.linalg.norm(saved_emb)
            similarity = dot_prod / (norm_a * norm_b)
            distance = 1.0 - similarity
            if distance < lowest_distance and distance < threshold:
                lowest_distance = distance
                closest_match = name
        if closest_match != "Unknown":
            accuracy = (1.0 - lowest_distance) * 100
            return f"{closest_match} ({accuracy:.1f}%)"
        return "Unknown"

    def process_live_video(self):
        print("[3/4] Initializing connection to Webcam hardware...")
        webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not webcam.isOpened():
            print("[ERROR] Webcam hardware could not be reached!")
            return

        webcam.set(cv2.CAP_PROP_FPS, 30)
        webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        print("[4/4] Camera hardware linked! Booting up Video Window stream...")
        window_name = 'AI 30FPS Automated Face Recognition Feed'
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        
        while True:
            ret, frame = webcam.read()
            if not ret:
                continue
            live_faces = self.app.get(frame)
            for face in live_faces:
                x1, y1, x2, y2 = face.bbox.astype(int)
                identity_tag = self.compare_live_face(face.embedding)
                box_color = (0, 255, 0) if "Unknown" not in identity_tag else (0, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
                cv2.putText(frame, identity_tag, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)
                
            cv2.imshow(window_name, frame)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
            if cv2.waitKey(33) & 0xFF == ord('q'):
                break
        webcam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    engine = FinalSelfCorrectingSystem()
    engine.auto_register_images()
    if engine.known_face_embeddings:
        engine.process_live_video()
    else:
        print("[CRITICAL] App closing: Please add image files inside the 'faces' folder first.")
