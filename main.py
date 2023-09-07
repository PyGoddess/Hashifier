import re
import os
def ascii_art():
    print("""

 ██░ ██  ▄▄▄        ██████  ██░ ██  ██▓  █████▒██▓▓█████  ██▀███  
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒▓██   ▒▓██▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▒████ ░▒██▒▒███   ▓██ ░▄█ ▒
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░░▓█▒  ░░██░▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░░▒█░   ░██░░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓   ▒ ░   ░▓  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░      ▒ ░ ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░ ░ ░    ▒ ░   ░     ░░   ░ 
 ░  ░  ░      ░  ░      ░   ░  ░  ░ ░          ░     ░  ░   ░     
https://discord.gg/ecSsjhJreY
Hash identifier
    """)
def main():
    os.system("cls && title Hashifier")
    ascii_art()
    hash_patterns = {
        'MD5': r'[0-9a-fA-F]{32}',
        'SHA-1': r'[0-9a-fA-F]{40}',
        'SHA-256': r'[0-9a-fA-F]{64}',
        'SHA-512': r'[0-9a-fA-F]{128}',
        'RIPEMD-160': r'[0-9a-fA-F]{40}',
        'Tiger': r'[0-9a-fA-F]{64}',
        'Whirlpool': r'[0-9a-fA-F]{128}',
        'GOST R 34.11-94': r'[0-9a-fA-F]{64}',
        'LM Hash': r'[0-9a-fA-F]{32}:[0-9a-fA-F]{32}',
        'NTLM Hash': r'[0-9a-fA-F]{32}',
        'CRC32': r'[0-9a-fA-F]{8}',
        'CRC16': r'[0-9a-fA-F]{4}',
        'Adler-32': r'[0-9a-fA-F]{8}',
        'Haval-128': r'[0-9a-fA-F]{32}',
        'Whirlpool-T': r'[0-9a-fA-F]{64}',
        'Base64': r'[\w\+\/]+={0,2}',
    }

    def identify_hash(hash_text):
        for hash_type, pattern in hash_patterns.items():
            if re.fullmatch(pattern, hash_text):
                return hash_type
        return "Unknown"

    if __name__ == "__main__":
        hash_input = input("Input hash >> ").strip()
        hash_type = identify_hash(hash_input)
        if hash_type == "Unknown":
            print("Couldnt find the hashtype..")
            input("Press ENTER to go back...")
            main()
        else:
            print(f"The input is of type: {hash_type}")
            input("Press ENTER to go back...")
            main()
main()
