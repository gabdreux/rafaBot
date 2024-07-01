import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuração do Firefox
def setup_driver():
    options = Options()
    service = Service(r'C:\Users\LATITUDE 3540\Desktop\BOT\geckodriver.exe')
    profile = webdriver.FirefoxProfile()

    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.useDownloadDir", False)
    profile.set_preference("browser.download.manager.showWhenStarting", True)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "")
    
    options.profile = profile
    driver = webdriver.Firefox(service=service, options=options)
    return driver

# Função para esperar até que um elemento esteja visível e clicável
def wait_for_element(driver, locator, timeout=30):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element
    except TimeoutException:
        print(f"Elemento {locator} não encontrado no tempo especificado.")
        return None

# Função para encontrar a primeira pasta com arquivos
def find_folder_with_file(base_path):
    i = 1
    while True:
        folder_path = os.path.join(base_path, str(i))
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                if files:
                    return folder_path
        i += 1

# Função principal
def main():
    driver = setup_driver()
    driver.get('https://app.remini.ai/?utm_source=reminiai&utm_medium=try-remini')

    print("Bem-Vindo, Rafael! :)")
    
    pyautogui.hotkey('win', 'up')
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    for _ in range(3):
        pyautogui.scroll(-100)
    pyautogui.keyUp('ctrl')

    # Espera e clica no botão de upload
    upload_button = wait_for_element(driver, (By.XPATH, "//div[@class='btn btn--large btn--primary w-max mx-auto py-1 px-6 ps-8 flex justify-center items-center rounded-full']"))
    if upload_button:
        upload_button.click()
        print("Iniciando uploads...")

    base_path = "C:\\Users\\LATITUDE 3540\\Desktop\\Fotos\\AGUARDANDO"
    folder_path = find_folder_with_file(base_path)
    if folder_path:
        modified_folder_path = folder_path.replace("AGUARDANDO", "EDITADAS")
        print(f"Pasta contendo arquivos: {folder_path}")
    else:
        print("Nenhuma pasta com arquivos foi encontrada.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if files:
        first_file = files[0]
        first_file_path = os.path.join(folder_path, first_file)
        pyautogui.write(first_file_path)
        time.sleep(5)
        pyautogui.press('enter')
        print(f"Primeiro arquivo digitado: {first_file_path}")
    else:
        print("A pasta está vazia ou não contém arquivos.")
        return

    # Pula o tutorial
    time.sleep(30)
    skip_tutorial_button = wait_for_element(driver, (By.XPATH, "//button[@type='button']//span[text()='Skip tutorial']"), timeout=60)
    if skip_tutorial_button:
        skip_tutorial_button.click()

    # Seleciona blur
    print("Selecionando blur...")
    blur_image = wait_for_element(driver, (By.XPATH, "//img[@src='/images/icons/backgroundBlur.svg' and @class='w-9 h-9']"))
    if blur_image:
        blur_image.click()
        time.sleep(5)
        none_blur_image = wait_for_element(driver, (By.XPATH, "//div[@class='flex bg-gray-450 rounded-[6px] w-[66px] h-[66px] border-2 justify-center border-transparent']//img[@alt='none']"))
        if none_blur_image:
            none_blur_image.click()

    # Seleciona autoColor
    print("Escolhendo autoColor...")
    auto_color_image = wait_for_element(driver, (By.XPATH, "//img[@src='/images/icons/autoColor.svg' and @class='w-9 h-9']"))
    if auto_color_image:
        auto_color_image.click()
        time.sleep(5)
        steady_image = wait_for_element(driver, (By.XPATH, "//img[@src='/images/thumbnails/steady.webp' and @class='object-cover w-[66px] h-[66px] rounded-[6px] border-2 border-transparent ']"))
        if steady_image:
            steady_image.click()
        time.sleep(8)

    # Baixar imagem
    download_button = wait_for_element(driver, (By.ID, "tutorial-bulk-step3"))
    if download_button:
        download_button.click()
        time.sleep(10)

    # Aplica as mudanças
    apply_button = wait_for_element(driver, (By.XPATH, "//button[contains(@class, 'w-11/12 btn btn--large shadow-dark-button btn--black mt-7 inline-flex')]//span[contains(@class, 'SB16')]//span[text()='Apply']"))
    if apply_button:
        apply_button.click()
        time.sleep(5)
        print("Alterações aplicadas!")

    # Baixar imagem novamente
    download_button = wait_for_element(driver, (By.ID, "tutorial-bulk-step3"))
    if download_button:
        download_button.click()
        print("Salvando foto...")

    # Define path de salvamento
    time.sleep(7)
    caminho_completo = os.path.join(modified_folder_path, first_file)
    pyautogui.write(caminho_completo)
    time.sleep(3)
    pyautogui.press('enter')

    # Fecha caixa de diálogo do download
    time.sleep(5)
    pyautogui.press('esc')
    print("Foto salva com sucesso!")

    # Deleta o arquivo original
    try:
        os.remove(first_file_path)
    except OSError as e:
        print(f"Erro ao deletar o arquivo {first_file_path}: {e.strerror}")

    # Sequência a partir da nova tela
    main_folder = base_path
    edited_folder = modified_folder_path
    subfolders = os.listdir(main_folder)

    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder, subfolder)
        if os.path.isdir(subfolder_path):
            while os.listdir(subfolder_path):
                first_file_loop = os.listdir(subfolder_path)[0]
                file_path = os.path.join(subfolder_path, first_file_loop)

                # Realiza as edições
                time.sleep(10)
                upload_image = wait_for_element(driver, (By.XPATH, "//img[@src='/_next/static/media/upload--white.e68b14d4.svg' and @alt='']"))
                if upload_image:
                    upload_image.click()
                    time.sleep(8)
                    pyautogui.write(file_path)
                    pyautogui.press('enter')

                    time.sleep(10)
                    print("Selecionando blur...")
                    none_blur_image = wait_for_element(driver, (By.XPATH, "//div[@class='flex bg-gray-450 rounded-[6px] w-[66px] h-[66px] border-2 justify-center border-transparent']//img[@alt='none']"))
                    if none_blur_image:
                        none_blur_image.click()

                    print("Escolhendo autoColor...")
                    steady_image = wait_for_element(driver, (By.XPATH, "//img[@src='/images/thumbnails/steady.webp' and @class='object-cover w-[66px] h-[66px] rounded-[6px] border-2 border-transparent ']"))
                    if steady_image:
                        steady_image.click()

                    time.sleep(5)
                    download_button = wait_for_element(driver, (By.ID, "tutorial-bulk-step3"))
                    if download_button:
                        download_button.click()
                    time.sleep(3)

                    time.sleep(5)
                    apply_button = wait_for_element(driver, (By.XPATH, "//button[contains(@class, 'w-11/12 btn btn--large shadow-dark-button btn--black mt-7 inline-flex')]//span[contains(@class, 'SB16')]//span[text()='Apply']"))
                    if apply_button:
                        apply_button.click()
                        time.sleep(3)
                        print("Alterações aplicadas!")
                        time.sleep(15)

                    download_button = wait_for_element(driver, (By.ID, "tutorial-bulk-step3"))
                    if download_button:
                        download_button.click()
                        print("Salvando foto...")

                    download_button = wait_for_element(driver, (By.XPATH, "//button[contains(@class, 'w-full h-9 btn btn--large btn--primary rounded-full border-0 mt-6')]//span[text()='Download']"))
                    if download_button:
                        download_button.click()

                    edited_subfolder = os.path.join(edited_folder, subfolder)
                    if not os.path.exists(edited_subfolder):
                        os.makedirs(edited_subfolder)
                    edited_path = os.path.join(edited_subfolder, first_file_loop)

                    print(f"Arquivo será salvo em editadas: {edited_path}")

                    time.sleep(5)
                    pyautogui.write(edited_path)
                    time.sleep(4)
                    pyautogui.press('enter')

                    time.sleep(5)
                    pyautogui.press('esc')
                    print("Foto salva com sucesso!")

                    try:
                        os.remove(file_path)
                    except OSError as e:
                        print(f"Erro ao deletar o arquivo {first_file_loop}: {e.strerror}")

                    time.sleep(2)

    print('Edições finalizadas com sucesso! :)')
    driver.quit()

    

if __name__ == "__main__":
    main()
