import cv2
import rosto
import maos

def abrir_camera():
    cap = cv2.VideoCapture(0)  # 0 é geralmente a câmera integrada

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Chama a função de reconhecimento de rosto
        frame = rosto.reconhecer_rosto(frame)

        # Chama a função de reconhecimento de mãos
        frame = maos.reconhecer_maos(frame)

        # Exibe o frame
        cv2.imshow('Webcam', frame)

        # Se a tecla 'q' for pressionada, sai do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
