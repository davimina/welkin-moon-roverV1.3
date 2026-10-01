from gpiozero import Motor
import config

class ChassiRover:
    def __init__(self):
        # Inicializa os motores usando os pinos configurados
        self.motor_esquerdo = Motor(forward=config.PINO_MOTOR_ESQ_FRENTE, backward=config.PINO_MOTOR_ESQ_TRAS)
        self.motor_direito = Motor(forward=config.PINO_MOTOR_DIR_FRENTE, backward=config.PINO_MOTOR_DIR_TRAS)

    def mover(self, direcao):
        if direcao == "frente":
            self.motor_esquerdo.forward()
            self.motor_direito.forward()
        elif direcao == "tras":
            self.motor_esquerdo.backward()
            self.motor_direito.backward()
        elif direcao == "esquerda":
            self.motor_esquerdo.backward()
            self.motor_direito.forward()
        elif direcao == "direita":
            self.motor_esquerdo.forward()
            self.motor_direito.backward()
        elif direcao == "parar":
            self.motor_esquerdo.stop()
            self.motor_direito.stop()