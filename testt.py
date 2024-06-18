import argparse
import os
import time
import sys
import random
import colorama
import requests
import pandas as pd
import pyfiglet
from colorama import init, Fore, Style

BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
NUMS = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
LETTS = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
color_list = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
CLEAR = 'cls' if os.name == 'nt' else 'clear'
FONTS = 'basic', 'o8', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
colorama.init(autoreset=True)



class PhoneNumberValidatorApp:

    def __init__(self, country_code):
        self.country_codes = ["US", "UK", "FR", "ES", "AE"]
        country_codes = ["US", "UK", "FR", "ES", "AE"]
        if country_code not in self.country_codes:
            raise ValueError(f"Invalid country code. Must be one of {self.country_codes}.")
        self.country_code =  random.choice(country_codes)
        self.phone_numbers_data = []
        self.phone_number_index = 0
     
    def generate_random_phone_number(self):
        if self.country_code == "US":
            area_codes = ["201", "202", "203", "205", "206", "207", "208", "212", "213", "214"]
            random_area_code = random.choice(area_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(7)])
            return f"+1{random_area_code}{subscriber_number}"
        elif self.country_code == "UK":
            operator_codes = ["70", "71", "72", "73", "74", "75", "76", "77", "78", "79"]
            random_operator_code = random.choice(operator_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+44{random_operator_code}{subscriber_number}"
        elif self.country_code == "FR":
            operator_codes = ["6", "7"]
            random_operator_code = random.choice(operator_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+33{random_operator_code}{subscriber_number}"
        elif self.country_code == "ES":
            operator_codes = ["6", "7"]
            random_operator_code = random.choice(operator_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
            return f"+34{random_operator_code}{subscriber_number}"
        elif self.country_code == "AE":
            operator_codes = ["50", "55", "56", "58"]
            random_operator_code = random.choice(operator_codes)
            subscriber_number = "".join([str(random.randint(0, 9)) for _ in range(7)])
            return f"+971{random_operator_code}{subscriber_number}"
        
    def validate_phone_number(self, phone_number):
        url = "https://truecaller4.p.rapidapi.com/api/v1/getDetails"
        querystring = {"phone": phone_number, "countryCode" : "AE"}  
        headers = {
            "X-RapidAPI-Key": "cecd24cf5amsh0457b3c7fb4fe7bp1972c9jsndf435613763b",
            "X-RapidAPI-Host": "truecaller4.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
    
            if 'data' in data and isinstance(data['data'], list) and len(data['data']) > 0:
                if 'name' in data['data'][0]:
                    name = data['data'][0]['name']
                    if name in data:
                        return data.get(name),
                    else:
                        print(f"{phone_number} - {name}")
                else:
                    print("Error: 'name' key not found in the first element of 'data'")
            else:
                print("Error: 'data' key is missing, not a list, or the list is empty")
        else:
            print(f"Error: {response.status_code}, {response.text}")

        return "Invalid", "red"

    def start_validation(self):
        self.phone_numbers_data = []
        self.phone_number_index = 0

        num_numbers = 10
        print("Validation in progress...")

        for _ in range(num_numbers):
            phone_number = self.generate_random_phone_number()
            name = self.validate_phone_number(phone_number)
            self.phone_numbers_data.append({"Phone Number": phone_number, "Name": name})
            self.phone_number_index += 1
            self.update_result_label()

        print("Validation completed.")
        self.save_to_csv()

    def update_result_label(self):
        if self.phone_number_index > len(self.phone_numbers_data):
            return

        phone_data = self.phone_numbers_data[self.phone_number_index - 1]
        phone_number = phone_data["Phone Number"]
        name = phone_data["Name"]
    
        print(f"Phone Number: {phone_number}, Name: {name}")

    def save_to_csv(self):
        df = pd.DataFrame(self.phone_numbers_data)
        df.to_csv("d_phone_numbers.csv", index=False)
        print("Phone numbers validated and stored in validated_phone_numbers.csv")

if __name__ == "__main__":
  
    os.system(CLEAR)
    logo = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⢹⣿⡿⠁⠈⠛⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠟⠁⠀⢻⣿⣿⠉⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠈⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠋⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢀⡾⠀⠀⠀⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠃⠀⠀⠸⣄⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠀⣼⡇⠀⠀⠀⠈⣿⣿⣷⡄⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⢿⠏⠀⠀⠀⠀⣿⡄⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⣿⡇⠀⠀⠀⠀⠙⠈⠻⣿⣾⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⠋⠘⠀⠀⠀⠀⢀⣿⣷⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⠉⣿⡄⠀⠀⠀⠀⠀⠀⠙⢿⡿⣿⣶⣤⣤⣀⣀⣀⣀⣤⣴⣿⡿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣼⡏⠙⢿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⠟⢹⣿⣿⠃⠀⠀⠈⠿⣆⡀⠀⠀⠀⠀⠀⠀⠙⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠐⠁⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠈⢻⣿⡏⠙⠳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠈⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠖⠀⠀⠀⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣄⡀⠀⠀⠀⢾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⡖⠀⣠⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠳⣼⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣤⣾⣿⠟⠀⠀⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣦⣼⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣠⣶⣿⣭⣤⣤⣴⣾⣆⣤⠀⠀⣾⣿⣿⡄⠀⢠⠀⣿⣷⣤⣬⣬⣽⣷⣤⡀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⡏⠀⠀⠀⢀⣾⣿⠟⠁⠈⠉⠛⠋⠹⣿⠚⣷⣼⣿⣿⣿⣿⣤⡿⣸⡟⠉⠛⠋⠉⠈⠙⢿⣿⣆⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣟⣿⡿⠿⣿⠿⢷⡶⣄⠀⢻⡆⣿⣿⣿⣿⣿⣿⣿⡇⣿⠁⢀⣴⣶⠿⣿⠿⠿⣿⣾⡆⠀⠀⠀⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⡿⠛⢱⣿⠃⠀⠀⠀⠀⢸⣿⣤⠀⠻⢷⣌⣉⣸⣧⣀⣧⣿⣿⣿⣿⣿⣿⣿⣧⣇⣠⣿⣈⣹⣶⠿⠃⣤⣽⣿⠻⠀⠀⠀⠀⢻⣧⠙⢿⣿⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⠋⠀⣰⣿⡇⠀⢀⣤⣾⠃⠈⠉⣽⣷⣤⠀⠈⠉⠉⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣉⠉⠉⠁⠤⣶⣿⡉⠉⠀⢻⣦⣀⠀⠈⣿⣧⡀⠘⢿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡿⠁⢀⣼⣿⣿⣠⣶⣿⣿⡇⠀⠐⠾⠿⠿⢶⣶⣾⠿⣶⣶⣿⡿⢿⣿⣿⣿⣿⣿⣿⠟⣿⣶⣤⠾⢿⣶⣶⠾⠿⠿⠖⠀⠈⣿⣿⣷⣦⣸⣿⣷⡄⠀⠹⣿⣧⠀⠀⠀
⠀⠀⢀⣾⡟⠁⢀⣾⣿⣿⠿⠋⢠⣿⣿⢀⡀⠀⠀⠀⠒⠋⠉⠁⠀⠘⣿⠟⠀⠀⢿⣿⣿⣿⣿⠃⠀⠙⣿⣿⠀⠀⠉⠙⠓⠂⠀⠀⠀⡀⢸⣿⣇⠉⠻⢿⣿⣿⣆⠀⠹⣿⡆⠀⠀
⠀⠀⢸⡟⠁⢀⣾⡿⠋⠁⠀⠀⢸⣿⣿⡟⠁⠀⢀⣀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠈⢿⣿⣿⠁⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠀⣀⠀⠀⠹⣾⣿⣿⠀⠀⠀⠉⠻⢿⡆⠀⠹⣷⡀⠀
⠀⠀⡿⠁⠀⡸⠋⠀⠀⠀⠀⠀⢸⣿⣿⢃⣤⣶⣿⠁⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⢿⠃⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⢹⣿⣿⠃⠀⠀⠀⠀⠈⢻⡄⠀⢹⡇⠀
⠀⢸⡇⠀⢀⣡⣤⣶⣶⣶⡇⠀⢸⣿⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣿⣿⡿⠀⠀⢷⣶⣶⣦⣄⡁⠀⠈⣇⠀
⠀⣸⠁⣰⣾⠟⠹⣿⣿⣿⠁⠀⠈⣿⡿⠁⠘⣿⣇⠀⠀⠀⠀⡀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣿⡟⠀⢹⣿⡇⠀⠀⢸⣿⣿⡟⠙⠿⣶⡀⢸⡀
⢀⣿⣾⠏⠀⠀⠀⢻⣿⣿⡄⠀⠀⢸⡇⠀⠀⠘⣿⣄⠀⠀⣸⡃⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⠀⠀⢀⣾⡟⠀⠀⠀⡿⠁⠀⠀⣸⣿⣿⠇⠀⠀⠈⠳⣾⡇
⣸⠟⠁⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠁⠀⠀⠀⠈⢿⣦⡀⢹⣧⠀⠀⠀⠘⠛⠛⠛⣿⣿⣿⡟⠛⠛⠟⠀⠀⠀⢀⣿⠀⣠⣿⠏⠀⠀⠀⠀⠁⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠙⢷
⠋⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⠀⠀⠀⣀⡀⠀⠀⠀⠀⠙⢿⣦⣿⣄⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢀⣾⣯⣾⠟⠁⠀⠀⠀⠀⢀⡀⠀⠀⢸⣿⡟⠁⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⢰⣿⠻⢦⣄⠀⠀⠀⠀⠙⣿⣿⣦⣀⠀⠀⠀⢈⣿⣿⣿⡋⠀⠀⠀⢀⣠⣾⣿⡟⠁⠀⠀⠀⢀⣴⡾⢻⡇⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣇⢸⣿⠀⠀⠙⢷⣄⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⠛⠛⠉⠙⠛⢻⣿⣿⣿⣿⣿⠋⠀⠀⠀⢀⡴⠛⠁⠀⢸⡇⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠘⢷⡀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⣿⣿⡏⠀⠀⢀⣴⠋⠀⠀⠀⠀⢸⣷⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡇⠀⠀⠀⠀⠀⠻⣦⠀⠀⠹⡟⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⡿⠀⠀⢠⡾⠁⠀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠁⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⠁⣄⠁⠀⣰⡿⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⣼⣧⠀⢿⠟⣿⣿⣿⡿⣿⠃⢀⣿⠀⣰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠈⣇⢻⣿⣿⠀⡟⠀⢸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠟⣿⡄⠀⠹⠘⣿⡿⠘⠀⠀⣿⡟⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢿⣷⠀⠀⠀⣿⡇⠀⠀⢠⣿⠁⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠈⣿⡄⠀⠀⢿⠀⠀⠀⣾⡏⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠹⣷⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⢀⡄⣄⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠀⣿⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣆⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡟⠀
    """
    os.system(CLEAR)
    font = random.choice(FONTS)
    color1 = random.choice(color_list)
    color2 = random.choice(color_list)
    while color1 == color2:
        color2 = random.choice(color_list)
    print(color2 + Style.BRIGHT + logo.center(200))    
    print('\n' * 2 + color2 + pyfiglet.figlet_format(' DIIIIIIB ', font=font, width=os.get_terminal_size().columns), end='\n')

    target_url = input(YEL + "Enter the target URL : ")
    hacking_words = [
        "Initializing...",
        "Accessing target URL...",
        "Bypassing firewall...",
        "Decrypting passwords...",
        "Extracting data...",
        "Compiling list of phone numbers...",
        "Connecting to Truecaller API...",
        "Validating phone numbers..."
    ]
    for word in hacking_words:
        color = random.choice(color_list)
        loading_time = random.uniform(150, 450) 
        print(color + Style.BRIGHT + f"{word} (will take {loading_time:.2f} seconds)")
        
        for i in range(int(loading_time)):
            time.sleep(1)
            sys.stdout.write(color + Style.BRIGHT + f"\rProgress: [{'#' * (i % 50)}{'-' * (50 - (i % 50))}] {i+1} seconds".center(80))
            sys.stdout.flush()
        print()
    app = PhoneNumberValidatorApp(random.choice(["US", "UK", "FR", "ES", "AE"]))
    app.csv_file_name = target_url
    app.start_validation()

    print(RED + "Simulating hacking activity...")
    for _ in range(10):
        print(random.choice(color_list) + ''.join(random.choices(LETTS + NUMS, k=random.randint(5, 15))))
        time.sleep(0.3)
    print(RED + "Hacking simulation completed.")
