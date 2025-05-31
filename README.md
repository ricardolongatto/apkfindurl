# apkfindurl

Extraia rapidamente **URLs embutidas** em APKs Android para uso em **reconhecimento**, **análise estática** e **pentest mobile**.

Desenvolvido para agilizar a fase de enumeração e descobrir endpoints diretamente no código decompilado de um APK.

---

## Funcionalidades

- Decompila o APK usando `apktool`
- Varre todo o código fonte por **URLs hardcoded**
- Remove resultados irrelevantes (ex: domínios genéricos)
- Suporte a busca em diretórios já decompilados (`--search-only`)
- Saída colorida e clara no terminal

---

## Uso

```bash
python3 apkfindurl.py -a caminho_do_apk.apk
```

### Argumentos disponíveis

| Flag                 | Descrição                                                 |
|----------------------|-----------------------------------------------------------|
| `-a`, `--apk`        | Caminho do arquivo APK a ser analisado                    |
| `-o`, `--output`     | Nome do diretório de saída da decompilação (default: output) |
| `-s`, `--search-only`| Usar pasta decompilada existente sem rodar `apktool`     |

---

## Exemplos

### Decompilar e buscar URLs:
```bash
python3 apkfindurl.py -a myapp.apk
```

### Apenas buscar em uma pasta já decompilada:
```bash
python3 apkfindurl.py -s -o output
```

---

## Requisitos

- Python 3.6 ou superior
- `apktool` instalado e acessível no terminal (requisito obrigatório)

---

Parte do projeto educacional [Pentest Mobile v2](https://desecsecurity.com/curso/pentest-android)
© Desec Security · [desecsecurity.com](https://desecsecurity.com)
