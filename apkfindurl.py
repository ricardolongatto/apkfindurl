import subprocess
import os
import re
import argparse

# ANSI cores
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def decompile_apk(apk_path, output_dir="output"):
    print(f"{GREEN}[+] Decompilando: {apk_path}{RESET}")
    try:
        subprocess.run(["apktool", "d", "-f", apk_path, "-o", output_dir],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"{GREEN}[+] Decompilação concluída.{RESET}")
    except Exception as e:
        print(f"{RED}[-] Erro ao decompilar o APK:{RESET}", e)

def extract_urls(output_dir):
    url_pattern = re.compile(r'https?://[a-zA-Z0-9./:_\-?=&#]+')
    ignora = ["schemas.android", "w3.org", "example.com", "googleapis", "mozilla", "publicsuffix"]
    urls = set()

    for root, _, files in os.walk(output_dir):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    content = f.read()
                    for match in url_pattern.findall(content):
                        if not any(i in match for i in ignora):
                            urls.add(match)
            except:
                continue
    return sorted(urls)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrai URLs de um APK.")
    parser.add_argument("-a", "--apk", help="Caminho do APK (obrigatório se não usar -s)")
    parser.add_argument("-o", "--output", default="output", help="Diretório de saída da decompilação")
    parser.add_argument("-s", "--search-only", metavar="DIR", help="Pular decompilação e usar pasta já decompilada")

    args = parser.parse_args()

    if args.search_only:
        if not os.path.isdir(args.search_only):
            print(f"{RED}[-] Pasta '{args.search_only}' não encontrada.{RESET}")
            exit(1)
        output_dir = args.search_only
    else:
        if not args.apk:
            parser.error("Você deve fornecer o caminho do APK com -a, ou usar -s para apenas buscar.")
        output_dir = args.output
        decompile_apk(args.apk, output_dir)

    print(f"\n{GREEN}[+] URLs encontradas:{RESET}")
    urls = extract_urls(output_dir)
    for u in urls:
        print(f"{CYAN}{u}{RESET}")
