import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
    driver.maximize_window()
    yield driver
    driver.quit()
    
    #Prueba automatizada 1: Si no deja agregar una tarea vacia
def test_add_task(driver):
 
    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10)  

    plus_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus-circle.fs-3")
    plus_icon.click()

    add_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.w-100")
    add_button.click()

    warning_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#swal2-html-container"))
    )
    assert warning_message.is_displayed(), "El mensaje de advertencia no apareció."

    driver.save_screenshot("screenshots/add_task_warning_message.png")

 #Prueba automatizada 2: Si la fecha es visible al momento de agregar una tarea
def test_add_task_with_date_field(driver):

    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10)  

    plus_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus-circle.fs-3")
    plus_icon.click()

    try:
        date_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "date"))
        )

        assert date_input.is_displayed(), "El campo de fecha no está visible."
    except Exception as e:
        raise AssertionError(f"Error al encontrar el campo de fecha: {e}")

    driver.save_screenshot("screenshots/add_task_with_date_field.png")

 #Prueba automatizada 3: Si nos deja agregar el nombre del responsable de la tarea
def test_add_person_name(driver):

    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10)  

    plus_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus-circle.fs-3")
    plus_icon.click()

    name_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "title"))
    )
    assert name_input.is_displayed(), "El campo para el nombre no está visible."
    
    name_input.send_keys("Juan Perez")
    assert name_input.get_attribute("value") == "Juan Perez", "No se pudo ingresar el nombre."

    driver.save_screenshot("screenshots/add_person_name.png")

 #Prueba automatizada 4: Si nos deja agregar un detalle a nuestra tarea
def test_add_task_description(driver):

    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10) 

    plus_icon = driver.find_element(By.CSS_SELECTOR, "i.bi.bi-plus-circle.fs-3")
    plus_icon.click()

    description_input = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "text"))
    )
    assert description_input.is_displayed(), "El campo de descripción no está visible."
    
    description_input.send_keys("Realizar la prueba automatizada para la tarea.")
    assert description_input.get_attribute("value") == "Realizar la prueba automatizada para la tarea.", "No se pudo ingresar la descripción."

    driver.save_screenshot("screenshots/add_task_description.png")

    #Prueba automatizada 5: Si tiene un contador de las tareas Pendientes/Completadas
def test_task_counter(driver):
    # Carga la página local
    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10)  

    task_counter = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p[style*='color: white; text-align: center;']"))
    )

    task_counter_text = task_counter.text
    assert "Total: 0" in task_counter_text, f"El total de tareas no es correcto: {task_counter_text}"
    assert "Completadas: 0" in task_counter_text, f"El número de tareas completadas no es correcto: {task_counter_text}"
    assert "Pendientes: 0" in task_counter_text, f"El número de tareas pendientes no es correcto: {task_counter_text}"

    driver.save_screenshot("screenshots/task_counter.png")

    #Prueba automatizada 6: Si en el Footer aparece el nombre de la empresa y el logo
def test_logo_presence(driver):
    driver.get("file:///C:/Users/guill/Downloads/Proyecto%20Final%20Programacion%203/index.html")
    time.sleep(10) 

    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='logogsrelojes.png' and @alt='GS Relojes RD']"))
    )

    assert logo.is_displayed(), "El logo no está visible en la página."
    
    driver.save_screenshot("screenshots/logo_presence.png")