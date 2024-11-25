import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "D:/algoritmos/selenium-test/tests/driver/msedgedriver.exe"
edge_options = Options()
edge_options.use_chromium = True
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(screenshots_dir, exist_ok=True)

report_path = os.path.join(os.path.dirname(__file__), "report.html")
report_content = ["<html><head><title>Reporte de Pruebas</title></head><body><h1>Reporte de Pruebas</h1><ul>"]

def take_screenshot(name):
    screenshot_path = os.path.join(screenshots_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def wait_for_element(by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

def wait_for_result_container_update():
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result-container"))
    )

def clear_form():
    clear_button = wait_for_element(By.ID, "clear-button")
    clear_button.click()

# Prueba 1: Verificar que la conversión de mm a cm funciona correctamente
def test_mm_to_cm():
    try:
        driver.get("file:///D:/algoritmos/selenium-test/src/index.html")
        
        clear_form()

        value_input = wait_for_element(By.ID, "value")
        value_input.clear()
        value_input.send_keys("100") 

        convert_button = wait_for_element(By.ID, "convert-button")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "convert-button"))) 
        convert_button.click()

        wait_for_result_container_update()

        result_container = driver.find_element(By.ID, "result-container")
        take_screenshot("test_mm_to_cm")
        assert "Resultado: 10.000 cm" in result_container.text, f"Expected 'Resultado: 10.000 cm', but got {result_container.text}"
        
        report_content.append("<li>Test mmToCm: <span style='color: green;'>PASSED</span></li>")
    except Exception as e:
        take_screenshot("test_mm_to_cm_error")
        report_content.append(f"<li>Test mmToCm: <span style='color: red;'>FAILED - {str(e)}</span></li>")

# Prueba 2: Verificar si el formulario se limpia correctamente
def test_clear_form():
    try:
        driver.get("file:///D:/algoritmos/selenium-test/src/index.html")

        clear_form()

        value_input = wait_for_element(By.ID, "value")
        value_input.clear()
        value_input.send_keys("500")

        convert_button = wait_for_element(By.ID, "convert-button")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "convert-button"))) 
        convert_button.click()

        wait_for_result_container_update()

        result_container = driver.find_element(By.ID, "result-container")
        take_screenshot("test_clear_form")
        assert "Resultado: 50.000 cm" in result_container.text, f"Expected 'Resultado: 50.000 cm', but got {result_container.text}"
        
        clear_form()

        report_content.append("<li>Test Clear Form: <span style='color: green;'>PASSED</span></li>")
    except Exception as e:
        take_screenshot("test_clear_form_error")
        report_content.append(f"<li>Test Clear Form: <span style='color: red;'>FAILED - {str(e)}</span></li>")

# Prueba 3: Verificar que el campo de valor se deshabilita después de una conversión
def test_disable_value_input_after_conversion():
    try:
        driver.get("file:///D:/algoritmos/selenium-test/src/index.html")

        clear_form()

        value_input = wait_for_element(By.ID, "value")
        value_input.clear()
        value_input.send_keys("100")

        convert_button = wait_for_element(By.ID, "convert-button")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "convert-button"))) 
        convert_button.click()

        WebDriverWait(driver, 10).until(
            lambda driver: not driver.find_element(By.ID, "value").is_enabled()
        )

        value_input = driver.find_element(By.ID, "value")
        take_screenshot("test_disable_value_input_after_conversion")
        assert not value_input.is_enabled(), "El campo de valor no se deshabilitó después de la conversión"
        
        clear_form()
        
        report_content.append("<li>Test Disable Value Input: <span style='color: green;'>PASSED</span></li>")
    except Exception as e:
        take_screenshot("test_disable_value_input_after_conversion_error")
        report_content.append(f"<li>Test Disable Value Input: <span style='color: red;'>FAILED - {str(e)}</span></li>")

# Prueba 4: Verificar si el mensaje de error aparece cuando el valor está vacío
def test_show_error_for_empty_value():
    try:
        driver.get("file:///D:/algoritmos/selenium-test/src/index.html")

        clear_form()

        convert_button = wait_for_element(By.ID, "convert-button")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "convert-button"))) 
        convert_button.click()

        wait_for_element(By.ID, "value")
        wait_for_result_container_update()

        result_container = driver.find_element(By.ID, "result-container")
        take_screenshot("test_show_error_for_empty_value")
        assert "El campo 'Valor' no puede estar vacío." in result_container.text, "No se mostró el mensaje de error esperado"
        
        clear_form()
        
        report_content.append("<li>Test Empty Value Error: <span style='color: green;'>PASSED</span></li>")
    except Exception as e:
        take_screenshot("test_show_error_for_empty_value_error")
        report_content.append(f"<li>Test Empty Value Error: <span style='color: red;'>FAILED - {str(e)}</span></li>")

# Prueba 5: Verificar si el valor ingresado es mayor al máximo permitido
def test_show_error_for_large_value():
    try:
        driver.get("file:///D:/algoritmos/selenium-test/src/index.html")

        clear_form()

        value_input = wait_for_element(By.ID, "value") 
        value_input.clear()
        value_input.send_keys("1e+101")

        convert_button = wait_for_element(By.ID, "convert-button")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "convert-button"))) 
        convert_button.click()

        wait_for_element(By.ID, "value")
        wait_for_result_container_update()

        result_container = driver.find_element(By.ID, "result-container")
        take_screenshot("test_show_error_for_large_value")
        assert "El valor es demasiado grande para ser procesado." in result_container.text, "No se mostró el mensaje de error esperado"
        
        clear_form()

        report_content.append("<li>Test Large Value Error: <span style='color: green;'>PASSED</span></li>")
    except Exception as e:
        take_screenshot("test_show_error_for_large_value_error")
        report_content.append(f"<li>Test Large Value Error: <span style='color: red;'>FAILED - {str(e)}</span></li>")

# Ejecutar todas las pruebas
def run_all_tests():
    test_mm_to_cm()
    test_clear_form()
    test_disable_value_input_after_conversion()
    test_show_error_for_empty_value()
    test_show_error_for_large_value()

run_all_tests()

driver.quit()

# Generar reporte
report_content.append("</ul></body></html>")
with open(report_path, "w", encoding="utf-8") as report_file:
    report_file.writelines(report_content)



