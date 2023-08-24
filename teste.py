import os
import subprocess

# Obtém o diretório do script Python em execução
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o executável
executavel = os.path.join(diretorio_atual, "CadeMinhaInternet.exe")

# Execute o executável
subprocess.run([executavel])
