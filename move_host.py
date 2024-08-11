from pathlib import Path
import shutil as cm
from os import getcwd
import sys
import ctypes

file = str(getcwd() + "\\move_host.py")

bakub = Path("hosts")
curent = Path(r"C:\Windows\System32\drivers\etc\hosts")

def main():
    print("exit beendet das programm und restore laed die bachup datei.")
    run = True
    while run:
        if not bakub.is_file():
            cm.copyfile(curent, bakub)
        if not curent.is_file():
            cm.copyfile(bakub, curent)

        first_sentence_prozess = input("host umleitung eintragen (z.B. 0.0.0.0  www.google.com): ")
        if first_sentence_prozess == "exit":
            run = False
            return
        if first_sentence_prozess == "restore":
            cm.copyfile(bakub, curent)
        else:
            with open(curent, "a") as prozess_file:
                prozess_file.write("\n" + first_sentence_prozess + "\n")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("Das Skript läuft mit Administratorrechten.")
        main()
        input("Drücke Enter, um das Fenster zu schließen...")  # Halte das Fenster offen
    else:
        print("Starte das Skript neu mit Administratorrechten.")
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            file,
            None,
            1
        )
        print("Das Skript wurde neu gestartet.")
        sys.exit()
