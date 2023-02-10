def exists_word(word, instance):
    result = []
    for file_data in instance.queue:
        lines = [index + 1 for index,
                 line in enumerate(file_data['linhas_do_arquivo'])
                 if word.lower() in line.lower()]
        if lines:
            result.append({
                'palavra': word,
                'arquivo': file_data['nome_do_arquivo'],
                'ocorrencias': [{'linha': line_number}
                                for line_number in lines]
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
