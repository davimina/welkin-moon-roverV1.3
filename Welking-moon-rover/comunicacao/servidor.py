from flask import Flask, Response, request, jsonify, render_template
import time
import config
from hardware.motores import ChassiRover
from visao.camera import SistemaVisao

app = Flask(__name__, template_folder='../templates')
rover = ChassiRover()
visao = SistemaVisao()

# Armazena o atraso atual (inicia com o valor padrão do config.py)
delay_atual = config.LATENCIA_LUNAR_SEGUNDOS

@app.route('/')
def interface_controle():
    return render_template('index.html')

@app.route('/video')
def feed_video():
    return Response(visao.gerar_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/configurar_delay', methods=['POST'])
def configurar_delay():
    global delay_atual
    dados = request.json
    try:
        novo_delay = float(dados.get('delay', 2.5))
        if novo_delay < 0:
            return jsonify({"status": "erro", "mensagem": "O delay não pode ser negativo."}), 400
        
        delay_atual = novo_delay
        print(f"[SISTEMA] Latência de sinal atualizada para {delay_atual} segundos.")
        return jsonify({"status": "sucesso", "novo_delay": delay_atual})
    except (ValueError, TypeError):
        return jsonify({"status": "erro", "mensagem": "Valor de delay inválido."}), 400

@app.route('/comando', methods=['POST'])
def receber_comando():
    dados = request.json
    comando = dados.get('direcao', 'parar')
    
    print(f"[ESTAÇÃO TERRA] Comando '{comando}' enviado. Aguardando {delay_atual}s de viagem...")
    time.sleep(delay_atual) # Utiliza o delay dinâmico configurado
    
    print(f"[LUA - ROVER] Comando '{comando}' executado!")
    rover.mover(comando)
    
    return jsonify({
        "status": "sucesso", 
        "comando_executado": comando, 
        "delay_aplicado": delay_atual
    })

def iniciar_servidor():
    app.run(host='0.0.0.0', port=5000, threaded=True)