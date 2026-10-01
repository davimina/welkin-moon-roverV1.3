import cv2

class SistemaVisao:
    def __init__(self):
        # 0 é geralmente a primeira webcam USB conectada
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def gerar_frames(self):
        while True:
            sucesso, frame = self.camera.read()
            if not sucesso:
                break
            
            # Aqui você poderia adicionar o código do TFLite para IA no futuro
            # Ex: frame = detectar_obstaculos(frame)

            # Codifica a imagem em JPEG para transmissão
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Formato necessário para stream de vídeo no navegador (MJPEG)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')