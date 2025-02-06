import json
import random
import sys
import time
import tkinter as tk

import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tlg import send_telegram_update, SUCCESS_MESSAGE_TELEGRAM, FAIL_MESSAGE_TELEGRAM

MFA_GOV_HU = "https://konzinfobooking.mfa.gov.hu"
SLEEP_SECONDS = 18000

driver = uc.Chrome()
action_chains = ActionChains(driver)
option = driver.options


def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {path} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {path}.")
    return None

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def belgrade (applicant_name, applicant_dob, applicant_count, applicant_phone, applicant_email, applicant_passport, applicant_country, applicant_residence):
    
    if driver.current_url == ("%s" % MFA_GOV_HU):
         driver.close()
         driver.get("%s" % MFA_GOV_HU)
    else:
         driver.get("%s" % MFA_GOV_HU)

    locationElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"label1\"]/button")))
    action_chains.move_to_element(locationElement).click().perform()

    input_location_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/input")))
    action_chains.move_to_element(input_location_element).click().send_keys("serbia").perform()
    belgrade_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modal2\"]/div/div/div[2]/div[83]/label")))
    action_chains.move_to_element(belgrade_element).click().perform()

    visa_type_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-target, '#modalCases')]")))
    action_chains.move_to_element(visa_type_element).click().perform()

    input_visa_type_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/input")))
    action_chains.move_to_element(input_visa_type_element).click().send_keys("Visa").perform()
    visa_c_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[2]/div[40]/label")))
    action_chains.move_to_element(visa_c_element).click().perform()

    save_type_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[3]/button[2]")))
    action_chains.move_to_element(save_type_element).click().perform()

    nameElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label4']")))
    action_chains.move_to_element(nameElement).click().send_keys(applicant_name).perform()

    birth_date_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='birthDate']")))
    action_chains.move_to_element(birth_date_element).click().send_keys(applicant_dob).perform()

    applicants_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label6']")))
    driver.find_element(By.XPATH, "//*[@id='label6']").clear()
    action_chains.move_to_element(applicants_element).click().send_keys(applicant_count).perform()

    phone_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label9']")))
    action_chains.move_to_element(phone_element).click().send_keys(applicant_phone).perform()

    email_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label10']")))
    action_chains.move_to_element(email_element).click().send_keys(applicant_email).perform()

    passportNumberElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1000']")))
    action_chains.move_to_element(passportNumberElement).click().send_keys(applicant_passport).perform()

    countryElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1001']")))
    action_chains.move_to_element(countryElement).click().send_keys(applicant_country).perform()

    residenceElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label1002']")))
    action_chains.move_to_element(residenceElement).click().send_keys(applicant_residence).perform()

    checkbox1Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='slabel13']")))
    action_chains.move_to_element(checkbox1Element).click().perform()

    checkbox2Element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='label13']")))
    action_chains.move_to_element(checkbox2Element).click().perform()

    saveElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100']")))
    action_chains.move_to_element(saveElement).click().perform()

    errorElement = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Torles\"]/div/div/div[1]/div")))

def subotica(applicant_name, applicant_dob, applicant_count, applicant_phone, applicant_email, applicant_passport, applicant_country,
             applicant_residence_permit):
    try:
        if driver.current_url == "https://konzinfobooking.mfa.gov.hu":
             driver.close()
             driver.get("https://konzinfobooking.mfa.gov.hu")
        else:
             driver.get("https://konzinfobooking.mfa.gov.hu")

        locationElement = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"label1\"]/button")))
        action_chains.move_to_element(locationElement).click().perform()
        input_location_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/input")))
        action_chains.move_to_element(input_location_element).click().send_keys("serbia").perform()
        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Subotica")]')) )
        parent = label.find_element(By.XPATH, './..')
        checkbox = parent.find_element(By.XPATH, './/input[@class="form-check-input"]')
        action_chains.move_to_element(checkbox).click().perform()
        visa_type_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(@data-target, '#modalCases')]")))
        action_chains.move_to_element(visa_type_element).click().perform()
        input_visa_type_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app/div/div/div[4]/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div/div[2]/div[1]/input")))
        action_chains.move_to_element(input_visa_type_element).click().send_keys("Visa").perform()
        label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Schengen")]'))
        )
        parent = label.find_element(By.XPATH, './..')
        checkbox = parent.find_element(By.XPATH, './/input[contains(@class, "form-check-input")]')
        checkbox.click()
        emulate_human()

        save_type_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"modalCases\"]/div/div/div[3]/button[2]")))
        action_chains.move_to_element(save_type_element).click().perform()
        emulate_human()

        name_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='label4']")))
        action_chains.move_to_element(name_element).click().send_keys(applicant_name).perform()
        emulate_human()

        birth_date_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='birthDate']")))
        action_chains.move_to_element(birth_date_element).click().send_keys(applicant_dob).perform()
        emulate_human()

        try:
            applicants_element = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='label6']")))
            driver.find_element(By.XPATH, "//*[@id='label6']").clear()
            action_chains.move_to_element(applicants_element).click().send_keys(applicant_count).perform()
        except(Exception,):
            print("")

        phone_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Phone")]')) )
        action_chains.move_to_element(phone_element).click().send_keys(applicant_phone).perform()
        emulate_human()

        email_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='label10']")))
        action_chains.move_to_element(email_element).click().send_keys(applicant_email).perform()
        emulate_human()

        label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Re-enter")]')) )
        action_chains.move_to_element(label).click().send_keys(applicant_email).perform()
        emulate_human()

        country_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='label1001']")))
        action_chains.move_to_element(country_element).click().send_keys(applicant_country).perform()
        emulate_human()

        residence = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "residence")]')) )
        action_chains.move_to_element(residence).click().send_keys(applicant_residence_permit).perform()
        emulate_human()

        passport_number_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Passport number")]')) )
        action_chains.move_to_element(passport_number_element).click().send_keys(applicant_passport).perform()
        emulate_human()


        checkbox1_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='slabel13']")))
        action_chains.move_to_element(checkbox1_element).click().perform()
        time.sleep(3)

        checkbox2_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='label13']")))
        action_chains.move_to_element(checkbox2_element).click().perform()
        time.sleep(3)

        save_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100']")))
        action_chains.move_to_element(save_element).click().perform()
    except(Exception,):
        send_telegram_update(FAIL_MESSAGE_TELEGRAM)
        print("FAIL_MESSAGE_TELEGRAM")
    error_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"Torles\"]/div/div/div[1]/div")))

def startbg():
    belgrade(ent_name.get(), ent_dob.get(), ent_count.get(), ent_phone.get(), ent_email.get(), ent_passport.get(), ent_country.get(), ent_residence.get())
    time.sleep(5)
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
            time.sleep(random.randint(80, 100))
            startbg()
    else:
        time.sleep(1800)

def startsb():
    option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
    option.add_argument("Accept-Language=en-US,en;q=0.9")
    print("run: " + time.ctime())
    if var.get():
        json_data = read_json(ent_path.get())
        subotica(json_data.get("name"), json_data.get("birth_date"), json_data.get("count"),
                 json_data.get("phone"), json_data.get("email"), json_data.get("passport"),"Russian Federation",json_data.get("residence_permit"))
    else:
        subotica(ent_name.get(), ent_dob.get(), ent_count.get(), ent_phone.get(), ent_email.get(), ent_passport.get(), ent_country.get(), ent_residence)
    time.sleep(5)
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button"):
            time.sleep(random.randint(200, 300))
            startsb()
    else:
        send_telegram_update(SUCCESS_MESSAGE_TELEGRAM)
        time.sleep(15000)

def startbgsb():
    belgrade(ent_name.get(), ent_dob.get(), ent_count.get(), ent_phone.get(), ent_email.get(), ent_passport.get(), ent_country.get(), ent_residence.get())
    if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
            time.sleep(random.randint(80, 100))
            subotica(ent_name.get(), ent_dob.get(), ent_count.get(), ent_phone.get(), ent_email.get(), ent_passport.get(), "Russian Federation", ent_residence.get())
            if check_exists_by_xpath("//*[@id=\"Torles\"]/div/div/div[2]/button") == True:
                time.sleep(random.randint(80, 100))
                startbgsb()
            else:
                time.sleep(SLEEP_SECONDS)
    else:
        time.sleep(SLEEP_SECONDS)

def emulate_human():
    time.sleep(1)
    action_chains.move_by_offset(random.randint(3, 20), random.randint(2, 10)).perform()
    time.sleep(1)

def stop():
    driver.close()
    sys.exit()

window = tk.Tk()
window.title("Embassy Slot Requester")
window.resizable(width=False, height=False)

frmEntry = tk.Frame(master=window)
lbl_name = tk.Label(master=frmEntry, text="Имя и Фамилия")
ent_name = tk.Entry(master=frmEntry, width=30)
lbl_dob = tk.Label(master=frmEntry, text="Дата рождения ДД.ММ.ГГГГ")
ent_dob = tk.Entry(master=frmEntry, width=30)
lbl_count = tk.Label(master=frmEntry, text="Количество подающих")
ent_count = tk.Entry(master=frmEntry, width=30)
lbl_phone = tk.Label(master=frmEntry, text="Номер телефона")
ent_phone = tk.Entry(master=frmEntry, width=30)
lbl_email = tk.Label(master=frmEntry, text="Email")
ent_email = tk.Entry(master=frmEntry, width=30)
lbl_passport = tk.Label(master=frmEntry, text="Номер паспорта | XXXXXXXXX")
ent_passport = tk.Entry(master=frmEntry, width=30)
lbl_country = tk.Label(master=frmEntry, text="Гражданство | Russian Federation")
ent_country = tk.Entry(master=frmEntry, width=30)
lbl_residence = tk.Label(master=frmEntry, text="Номер и дата окончания ВНЖ | A000000 ДД.ММ.ГГГГ")
ent_residence = tk.Entry(master=frmEntry, width=30)

lbl_path = tk.Label(master=frmEntry, text="Absolute file path(optional)")
ent_path = tk.Entry(master=frmEntry, width=30)

lbl_name.grid(row=0, column=0, sticky="e")
ent_name.grid(row=0, column=1, sticky="w")
lbl_dob.grid(row=1, column=0, sticky="e")
ent_dob.grid(row=1, column=1, sticky="w")
lbl_count.grid(row=2, column=0, sticky="e")
ent_count.grid(row=2, column=1, sticky="w")
lbl_phone.grid(row=3, column=0, sticky="e")
ent_phone.grid(row=3, column=1, sticky="w")
lbl_email.grid(row=4, column=0, sticky="e")
ent_email.grid(row=4, column=1, sticky="w")
lbl_passport.grid(row=5, column=0, sticky="e")
ent_passport.grid(row=5, column=1, sticky="w")
lbl_country.grid(row=6, column=0, sticky="e")
ent_country.grid(row=6, column=1, sticky="w")
lbl_residence.grid(row=7, column=0, sticky="e")
ent_residence.grid(row=7, column=1, sticky="w")

lbl_path.grid(row=8, column=0, sticky="e")
ent_path.grid(row=8, column=1, sticky="w")

var = tk.BooleanVar(value=False)

chk_read_json = tk.Checkbutton(
    master=window,
    text="Read json",
    variable=var
)

btn_belgrade = tk.Button(
    master=window,
    text="Start Belgrade",
    command=startbg
)
btn_subotica = tk.Button(
    master=window,
    text="Start Subotica",
    command=startsb
)
btn_belgrade_subotica = tk.Button(
    master=window,
    text="Start Belgrade and Subotica",
    command=startbgsb
)
btn_stop = tk.Button(
    master=window,
    text="Exit",
    command=stop
)

frmEntry.grid(row=0, column=0, padx=10)
btn_subotica.grid(row=0, column=2, pady=10)
chk_read_json.grid(row=1, column=4, pady=10)
btn_stop.grid(row=0, column=4, padx=10)

window.mainloop()


