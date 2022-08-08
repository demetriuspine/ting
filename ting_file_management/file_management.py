import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if '.txt' not in path_file:
            print("Formato inválido", file=sys.stderr)

        with open(path_file, mode="r") as file:
            content = file.read()
            formatted_content = content.split("\n")
            return formatted_content

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
