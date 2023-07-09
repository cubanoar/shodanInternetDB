import os
import requests
import argparse

# Colores y estilos en código de escape ANSI
color_reset = "\033[0m"
color_red = "\033[31m"
color_green = "\033[32m"
color_blue = "\033[34m"
color_black = "\033[30m"
color_yellow = "\033[33m"
color_magenta = "\033[35m"
color_cyan = "\033[36m"
color_white = "\033[37m"
style_bold = "\033[1m"
style_bright = "\033[1;94m"
  
parser = argparse.ArgumentParser(description='Info by IP')
parser.add_argument("-t","--target",help="IP [default, your IP]",default='')
params = parser.parse_args()


def main():
   print("\33[2J\33[H")
   print('-'*os.get_terminal_size().columns)
   print("\tThe InternetDB API provides a fast way to see the open ports for an IP address.")
   print('-'*os.get_terminal_size().columns)
   try:
        host = requests.get(f"https://internetdb.shodan.io/{params.target}").json()
        for key, value in host.items():
            print(f'\n{color_blue}{style_bold}{style_bright}{key.upper()}:{color_reset}')
            if isinstance(value,list):
                for item in value:
                    print(f'\t{color_red}{style_bold}{item}{color_reset}')
            else:
                print(f'\t{color_red}{style_bold}{value}{color_reset}')
        print('-'*os.get_terminal_size().columns)
   except Exception as e:
        print(f'{color_red}{e}{color_reset}')


if __name__ == '__main__':
    main()
