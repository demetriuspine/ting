import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    """Aqui irá sua implementação"""
    instance_len = instance.__len__()
    paths_list = []
    if instance_len > 0:
        for index in range(instance_len):
            paths_list.append(instance.search(index)["nome_do_arquivo"])

    if path_file not in paths_list:
        content = txt_importer(path_file)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(content),
            "linhas_do_arquivo": content
        }
        instance.enqueue(result)
        print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
