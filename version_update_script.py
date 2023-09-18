import os
import subprocess
import time
import requests

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
lock_file = diretorio_atual + "/my_app.lock"

repo_usuario = "lpc1990"
repo_nome = "EstamosComInternetOuNao"

# Faz a solicitação GET para a API do GitHub
site = (f"https://api.github.com/repos/{repo_usuario}/{repo_nome}/releases")
response = requests.get(site)


# Verifica se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    releases = response.json()  # Converte a resposta para formato JSON
    for release in releases:

        latest_release = releases[0]
        tag_git_com_v = (release["tag_name"])
        tag_git_sem_v = tag_git_com_v.lstrip("v")

        nome_arquivo = "Instalador_versao_" + tag_git_com_v + ".exe"


# Fecha o programa principal (substitua "seu_programa.exe" pelo nome real do executável) e remove o lock_file
os.system("taskkill /F /IM CadeMinhaInternet.exe")
if os.path.exists(lock_file):
    os.remove(lock_file)


# Aguarda alguns segundos para garantir que o programa foi completamente encerrado
time.sleep(5)

# Realiza a atualização (substitua "installer.exe" pelo nome real do instalador)
subprocess.run([nome_arquivo, '/SILENT'], shell=True)
os.remove(nome_arquivo)
subprocess.run(["CadeMinhaInternet.exe"])

