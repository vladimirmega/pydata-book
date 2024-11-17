import os

# Diretório base do projeto (raiz)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_data_path(filename: str) -> str:
    """
    Retorna o caminho absoluto para um arquivo dentro da pasta 'data'.

    Args:
        filename (str): Nome ou caminho relativo do arquivo dentro de 'data'.

    Returns:
        str: Caminho absoluto para o arquivo.
    """
    return os.path.join(BASE_DIR, "data", filename)

