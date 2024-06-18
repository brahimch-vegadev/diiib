import tkinter as tk
from tkinter import ttk
import requests
import random
import pandas as pd

class PhoneNumberValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Number Validator")

        self.country_codes = ["US", "UK", "FR", "ES", "AE"]
        self.api_key = "YOUR_API_KEY"
        self.api_secret = "YOUR_API_SECRET"

        self.phone_numbers_data = []
        self.phone_number_index = 0

        self.setup_ui()

    def setup_ui(self):
        self.country_label = ttk.Label(self.root, text="Select Country:")
        self.country_combobox = ttk.Combobox(self.root, values=self.country_codes)
        self.country_combobox.current(0)

        self.start_button = ttk.Button(self.root, text="Start Validation", command=self.start_validation)

        self.info_label = ttk.Label(self.root, text="")
        self.result_label = ttk.Label(self.root, text="")

        self.country_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.country_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.start_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.info_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def generate_random_phone_number(self, country_code):
        if country_code == "US":
            area_codes = ["201", "202", "203", "205", "206", "207", "208", "212", "213", "214"]
            random_area_code = random.choice(area_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(7)])
            return f"+1{random_area_code}{subscriber_number}"
        elif country_code == "UK":
            area_codes = ["20", "23", "24", "28", "29", "31", "33", "34", "44", "51"]
            random_area_code = random.choice(area_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+44{random_area_code}{subscriber_number}"
        elif country_code == "FR":
            area_codes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            random_area_code = random.choice(area_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+33{random_area_code}{subscriber_number}"
        elif country_code == "ES":
            area_codes = ["6", "7", "8"]
            random_area_code = random.choice(area_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+34{random_area_code}{subscriber_number}"
        elif country_code == "AE":
            operator_codes = ["50", "55", "56", "58"]
            random_operator_code = random.choice(operator_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(7)])
            return f"+971{random_operator_code}{subscriber_number}"

    def validate_phone_number(self, phone_number):
        url = "https://truecaller4.p.rapidapi.com/api/v1/getDetails"
        querystring = {"phone": "508737055", "countryCode" : "AE"}  
        headers = {
            "X-RapidAPI-Key": "cecd24cf5amsh0457b3c7fb4fe7bp1972c9jsndf435613763b",
            "X-RapidAPI-Host": "truecaller4.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            if data.get('name'):
                return data['data'][0]['name'],
       
    def start_validation(self):
        self.phone_numbers_data = []
        self.phone_number_index = 0

        country_code = self.country_combobox.get()
        num_numbers = 10
        self.info_label.config(text="Validation in progress...")

        for _ in range(num_numbers):
            phone_number = self.generate_random_phone_number(country_code)
            name = self.validate_phone_number("508737055")
            self.phone_numbers_data.append({"Phone Number": "508737055", "Name": name,})
            self.phone_number_index += 1
            self.update_result_label()

        self.info_label.config(text="Validation completed.")

    def update_result_label(self):
        if self.phone_number_index > len(self.phone_numbers_data):
            return

        phone_data = self.phone_numbers_data[self.phone_number_index - 1]
        phone_number = phone_data["Phone Number"]
        name = phone_data["Name"]

        self.result_label.config(text=f"Phone Number: {phone_number}, Name: {name}",)
        self.result_label.update()
        
    def save_to_csv(self):
        df = pd.DataFrame(self.phone_numbers_data)
        df.to_csv("validated_phone_numbers.csv", index=False)
        print("Phone numbers validated and stored in validated_phone_numbers.csv")    

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneNumberValidatorApp(root)
    root.mainloop()
