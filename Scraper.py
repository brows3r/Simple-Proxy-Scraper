# update - my friend wanted to use it so i fixed it

import urllib.request
import os
import pyfiglet
import shutil

os.system("cls")
ascii_banner = pyfiglet.figlet_format("Scraper")
print(ascii_banner)

print('''Options
-----------------------------------------
HTTP
SOCKS4
SOCKS5
''')

type = input("Which type of proxy would you like to scrape?: ")
if type == "HTTP":
    url_http = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=alls"
    output_file = "HTTPlist.txt"
    with urllib.request.urlopen(url_http) as response, open(output_file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print("Finished, check HTTPlist.txt in folder.")
else:
    if type == "SOCKS4":
        url_socksfour = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
        output_file = "SOCKS4list.txt"
        with urllib.request.urlopen(url_socksfour) as response, open(output_file, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Finished, check SOCKS4list.txt in folder.")
    else:
        if type == "SOCKS5":
            urlsocksfive = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
            output_file = "SOCKS5list.txt"
            with urllib.request.urlopen(url_socksfive) as response, open(output_file, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            print("Finished, check SOCKS5list.txt in folder.")
        else:
            print("Wrong Command!")
            exit()

Clear = int(input("Press 1 to quit: "))

if Clear == 1:
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
else: exit()
