import cv2
import mediapipe as mp
import numpy as np

# Inicializa o mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

def reconhecer_maos(frame):
    # Converte a imagem para RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta as mãos
    results = hands.process(image)

    # Desenha os resultados
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Verifica se cada dedo está levantado
            dedos = ['Polegar', 'Indicador', 'Medio', 'Anelar', 'Minimo']
            dedos_levantados = []
            for i, dedo in enumerate(dedos):
                # O ponto de referência 0 é o pulso.
                # Para cada dedo, o ponto de referência 4*i+1 é a base do dedo.
                # O ponto de referência 4*i+4 é a ponta do dedo.
                base = np.array([hand_landmarks.landmark[4*i+1].x, hand_landmarks.landmark[4*i+1].y])
                ponta = np.array([hand_landmarks.landmark[4*i+4].x, hand_landmarks.landmark[4*i+4].y])
                distancia = np.linalg.norm(base - ponta)
                if distancia > 0.1:  # Ajuste este valor conforme necessário
                    dedos_levantados.append(dedo)

            # Verifica gestos específicos
            if set(['Polegar', 'Indicador']).issubset(dedos_levantados) and len(dedos_levantados) == 2:
                cv2.putText(frame, 'Arminha', (int(hand_landmarks.landmark[0].x * frame.shape[1]), int(hand_landmarks.landmark[0].y * frame.shape[0]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            elif set(['Indicador', 'Medio']).issubset(dedos_levantados) and len(dedos_levantados) == 2:
                cv2.putText(frame, 'PAZ', (int(hand_landmarks.landmark[0].x * frame.shape[1]), int(hand_landmarks.landmark[0].y * frame.shape[0]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                for dedo in dedos_levantados:
                    # Para o polegar, verifica se está perto do indicador
                    if dedo == 'Polegar' and 'Indicador' in dedos_levantados:
                        continue
                    cv2.putText(frame, dedo, (int(hand_landmarks.landmark[4*dedos.index(dedo)+4].x * frame.shape[1]), int(hand_landmarks.landmark[4*dedos.index(dedo)+4].y * frame.shape[0]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return frame
