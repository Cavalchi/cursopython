import cv2
import mediapipe as mp

# Inicializa o mediapipe
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection()

def reconhecer_rosto(frame):
    # Converte a imagem para RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta os rostos
    results = face_detection.process(image)

    # Desenha os resultados
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)
            cv2.putText(frame, 'Rosto', (int(detection.location_data.relative_bounding_box.xmin * frame.shape[1]), int(detection.location_data.relative_bounding_box.ymin * frame.shape[0]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame
