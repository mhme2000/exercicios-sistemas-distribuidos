import socket
HOST = '192.168.18.153'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
opt = 1
msgEnum = print(
    '''
========================================================
23. Faça um algoritmo que verifique se duas cadeias
lidas do usuários são o anagrama uma da outra,
e informe ao usuário o resultado.
========================================================
    '''
    )
while opt != 0:
    msg = str(input("Digite uma palavra: ")).encode()
    tcp.send (msg)
    msg = str(input("Digite outra palavra: ")).encode()
    tcp.send (msg)
    resp = str(tcp.recv(1024).decode())
    if(resp == 'True'):
        print('As palavras são anagramas.')
    else:
        print('As palavras NÃO são anagramas.')
    opt = int(input("Digite [0] para interromper a execução do programa ou [1] para continuar: "))
    if(opt == 0):
        tcp.send(str(opt).encode())
        break
tcp.close()
print('Conexão interrompida pelo client!')