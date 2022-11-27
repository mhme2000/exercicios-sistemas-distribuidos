import socket

HOST = '192.168.18.153'   # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print(
    '''
===========================================================
18. Faça um algoritmo que leia um vetor de 20 elementos, 
em seguida ordene-os (por um, e apenas
um, dos métodos vistos em aula) e, em seguida,
faça uma busca binária de um elemento lido do
usuário, escrevendo se o elemento foi ou não encontrado na lista.
===========================================================
    '''
)
msg = []  # declarando vetor
i = 0  # contador
aux = 'n'

# loop para receber até 20 elementos
while i < 20:
    msg.insert(0, int(input(f"{i+1} elemento: ")))
    i += 1

while True:
    msg = str(msg)  # converte o input para string
    msg = msg.encode()  # encode da string
    tcp.send(msg)  # envia a mensagem para o servidor
    print('vetor enviado!')  # confirma envio
    resp1 = (tcp.recv(1024)).decode()  # recebe o vetor ordenado
    print("vetor ordenado: ", resp1)  # imprime o vetor ordenado
    while True:
        aux = aux.encode()
        tcp.send(aux)
        item = input("\nDigite o item a ser pesquisado na lista: ").encode()  # recebe o item a ser buscado na lista
        tcp.send(item)  # envia o item
        print('item enviado')  # confirma envio
        resp2 = (tcp.recv(1024)).decode()  # recebe o resultado da busca
        print(resp2)  # imprime o resultado da busca
        aux = input('\nDeseja se desconectar?:(s/n) ')  # entrar com parada ou continuação do programa
        if aux != 's':
            aux = 'n'
        if aux == 's':
            aux = aux.encode()
            tcp.send(aux)
            print('Conexão com servidor terminada')
            break
    break
tcp.close()
