from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if len(instance) > 0:
        for index in range(len(instance)):
            if instance.search(index)["nome_do_arquivo"] == path_file:
                return

    result_list = txt_importer(path_file)
    infos = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(result_list),
        "linhas_do_arquivo": result_list,
    }
    print(infos)
    instance.enqueue(infos)


def remove(instance):
    if len(instance) <= 0:
        print("Não há elementos")
    else:
        result = instance.dequeue()
        print(f"Arquivo {result['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        return print(result)
    except Exception as error:
        print(error, file=sys.stderr)
