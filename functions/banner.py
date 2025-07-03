from colorama import Fore, Style, init
from datetime import datetime
from functions.thanhngang import thanhngang

init(autoreset=True)

def banner():
    print(
        f"{Fore.YELLOW}╔══════════════════════════════════════════════════════╗\n"
        f"{Fore.YELLOW}║                                                      ║\n"
        f"{Fore.YELLOW}║  {Fore.WHITE} █████╗ ███╗  ██╗██╗  ██╗ ██████╗ ██████╗ ███████╗ {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║ {Fore.WHITE} ██╔══██╗████╗ ██║██║ ██╔╝██╔════╝ ██╔══██╗██╔════╝ {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║ {Fore.WHITE} ███████║██╔██╗██║█████═╝ ██║     ██████╔╝█████╗   {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║ {Fore.WHITE} ██╔══██║██║╚████║██╔═██╗ ██║     ██╔═══╝ ██╔══╝   {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║ {Fore.WHITE} ██║  ██║██║ ╚███║██║ ╚██╗╚██████╗██║     ███████╗ {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║ {Fore.WHITE} ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝╚═╝     ╚══════╝ {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║                                                      ║\n"
        f"{Fore.YELLOW}║      \x1b[1;36mAdmin: Anh Code | YouTube: @anhhcode     {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║         {Fore.WHITE}Box Zalo: https://zalo.me/g/nsilph288        {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║\n"
        f"{Fore.YELLOW}╚══════════════════════════════════════════════════════╝\n"
    )
    thanhngang(55)
