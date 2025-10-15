import sys
from ascii_magic import AsciiArt
from colorama import Fore, Style, init

# Inisialisasi colorama untuk warna di terminal
init(autoreset=True)

def load_banner(image_source: str, from_url: bool = True):
    """Tampilkan banner ASCII berwarna"""
    try:
        if from_url:
            art = AsciiArt.from_url(image_source)
        else:
            art = AsciiArt.from_image_file(image_source)

        print(Fore.CYAN + Style.BRIGHT)
        art.to_terminal()
        print(Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[!] Gagal memuat banner: {e}" + Style.RESET_ALL)

def show_info(number: str, credit: int, premium_credit: int, sim_type: str):
    """Tampilkan info pengguna berwarna"""
    print(Fore.YELLOW + "=" * 60)
    print(Fore.GREEN + f"Nomor      : {number}")
    print(Fore.CYAN +  f"Tipe Kartu : {sim_type}")
    print(Fore.MAGENTA + f"Credit     : {credit}")
    print(Fore.BLUE + f"Premium    : {premium_credit}")
    print(Fore.YELLOW + "=" * 60 + Style.RESET_ALL)

# ✅ Alias agar kode lama tetap berfungsi
load = load_banner
