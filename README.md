# Automação de Upload e Edição de Fotos no Remini

Este script automatiza o processo de upload e edição de fotos no site Remini. Realiza o upload das fotos, aplica as edições de "Blur" e "AutoColor", e baixa as fotos editadas, salvando-as em uma pasta específica.


# Requisitos

 - Python 3.x
 - Selenium
 - pyautogui
 - geckodriver (para Firefox)
 - Navegador Firefox
 - PyInstaller


# Instalação

Clone o repositório:
git clone https://github.com/seu-usuario/repo-automacao.git
cd repo-automacao

Instale as dependências necessárias:
pip install selenium 
pip install pyautogui
pip install pyinstaller

Baixe o geckodriver:
Baixe o geckodriver e coloque o executável no diretório apropriado. Atualize o caminho do geckodriver no script.


# Configuração


service = r'C:\Users\LATITUDE 3540\Desktop\BOT\geckodriver.exe' (Linha 15)
base_path = "C:\\Users\\LATITUDE 3540\\Desktop\\Fotos\\AGUARDANDO" (Linha 68)
modified_folder_path (Linha 71)



# Uso

python rafaBot.py


# Estrutura do Código

 - setup_driver(): Configura o driver do Firefox.
 - wait_for_element(driver, locator, timeout): Espera até que um elemento esteja presente, clicável e visível.
 - find_folder_with_file(base_path): Encontra a primeira pasta com arquivos no caminho base.
 - main(): Função principal que orquestra o processo de automação.


# Gerando Executável

pyinstaller --onefile rafaBot.py
O executável será criado na pasta dist.


