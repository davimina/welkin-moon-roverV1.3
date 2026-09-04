# 🛰️ Welkin Moon Rover

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/hardware-Raspberry%20Pi-red.svg)](https://www.raspberrypi.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Simulando a exploração planetária remota e a latência de comunicação entre a Terra e Marte.**

O **Welkin Moon Rover** é um projeto de robótica e visão computacional desenvolvido sobre a plataforma **Raspberry Pi**. O objetivo principal é simular o controle e a telemetria de um rover espacial operando na superfície lunar ou martiana, incorporando atrasos de sinal programados (*signal delay*) para replicar o desafio real enfrentado por engenheiros e operadores da NASA e ESA no comando de robôs extraterrestres.

---

## 🌟 Destaques do Projeto

- **🕹️ Teleoperação com Latência Configurável:** Simulação do atraso de transmissão de dados proporcional à distância Terra-Marte (de 3 a 22 minutos em escala real ou ajustável para testes).
- **👁️ Visão Computacional Embarcada:** Transmissão de vídeo via câmera acoplada ao Raspberry Pi com análise de terreno em tempo real.
- **🧱 Suporte a Processamento Leve:** Estruturado em Python com OpenCV/TFLite para execução otimizada em hardware embarcado.
- **📊 Telemetria Interativa:** Envio de dados operacionais, status dos sensores e feed visual para uma estação de controle remota.