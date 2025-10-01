import requests

def enviar_arquivo():
    # caminho para upload
    caminho = 'C:/Users/rodri/Desktop/EBAC/SQL/pdf/Profissao_ Analista de Dados M16 De olho no codigo.pdf'

    # enviar arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file':open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso: ",url)

#enviar_arquivo()

def receber_arquivo(file_url):
    # receber o arquivo
    requisicao = requests.get(file_url)

    # salvar o arquivo
    if requisicao.ok:
        with open ('arquivo_baixado.pdf', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo Baixado com Sucesso.')
    else:
        print('Erro ao baixar o arquivo: ', requisicao.json())

url_arquivo = 'https://gofile.io/myprofile'
#receber_arquivo(url_arquivo)



