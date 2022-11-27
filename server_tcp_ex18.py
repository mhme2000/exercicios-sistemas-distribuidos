import socket

HOST = ''           # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

def pesquisa_binaria(vetor, esquerda, direita, item):  # funcao que realiza a busca binaria
    if direita < esquerda:
        return "elemento não encontrado"
    meio = (esquerda + direita) // 2
    if vetor[meio] == item:
        return "\nExiste o item '" + str(vetor[meio]) + "' na posição: " + str(meio+1)
    elif vetor[meio] > item:
        return pesquisa_binaria(vetor, esquerda, meio - 1, item)
    else:
        return pesquisa_binaria(vetor, meio + 1, direita, item)

print("Servidor iniciado\n")  # mensagem para confirmar que o servidor funcionou
con, cliente = tcp.accept()  # realiza a conexão tcp
print(f'Conectado por {cliente}')  # mostra qual cliente foi conectado
msg = (con.recv(1024)).decode()  # recebe a mensagem do cliente
msg = eval(msg)  # volta a mensagem recebida para o formato desejado(lista)
list.sort(msg)  # ordena a lista
result1 = bytes(str(msg), 'utf-8')  # converte a lista para string e em seguida para bytes
con.send(result1)  # enviada o resultado para o cliente
while True:
    aux = (con.recv(1024)).decode()
    if aux == 'n':
        item = (con.recv(1024)).decode()  # recebe a mensagem do cliente e decodifica
        item = eval(item)  # eval usado para voltar ao formato inteiro

        # pré verifica se o valor passado está no escopo da lista (nesse caso maior que o maior número da lista)
        if item > msg[19]:
            result2 = bytes("Não existe o item, maior que o maior numero da lista!", 'utf-8')
            con.send(result2)

        # pré verifica se o valor passado está no escopo da lista (nesse caso menor que o menor número da lista)
        elif item < msg[0]:
            result2 = bytes("Não existe o item, menor que o menor numero da lista!", 'utf-8')
            con.send(result2)

        else:  # caso passe é chamado a função de busca binaria com a lista ordenada e o item a ser buscado na lista
            # armazena o resultado em uma variável e converte para string e em seguida para bytes
            result2 = bytes(str(pesquisa_binaria(msg, 0, len(msg), item)), 'utf-8')
            con.send(result2)  # envia para o cliente
    else:
        break
tcp.close()  # fecha conexão com o cliente
