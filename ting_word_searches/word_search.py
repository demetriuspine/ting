def exists_word(word, instance):
    """Aqui irá sua implementação"""
    stack_len = instance.__len__()
    data_list = []

    for file_index in range(stack_len):
        occurrences = []
        file = instance.search(file_index)

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if len(occurrences) > 0:
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            }
            data_list.append(data)

    return data_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
