import os

def get_folder_size(folder):
    """
    Calcula recursivamente o tamanho total (em bytes) de todos os arquivos dentro da pasta especificada.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Verifica se o arquivo existe para evitar erros de links quebrados, etc.
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

def main():
    # Defina o caminho da pasta principal que contém as pastas internas.
    pasta_principal = "C:/Users/T-Gamer/Desktop/Junho"  # altere para o caminho desejado

    # Defina o nome do arquivo de saída
    arquivo_saida = "tamanho_pastas.txt"
    
    with open(arquivo_saida, "w", encoding="utf-8") as f_out:
        # Lista todos os itens dentro da pasta principal
        for item in os.listdir(pasta_principal):
            caminho_item = os.path.join(pasta_principal, item)
            # Se for uma pasta, calcula o tamanho total dos arquivos contidos nela
            if os.path.isdir(caminho_item):
                tamanho = get_folder_size(caminho_item)
                # Escreve no arquivo de saída
                f_out.write(f"Pasta: {item} - Tamanho: {tamanho} bytes\n")
    
    print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

if __name__ == "__main__":
    main()
