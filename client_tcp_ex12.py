import socket
HOST = '192.168.18.153'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print(
    '''
===========================================================
12. Faça um algoritmo que leia uma frase e compute a 
frequência de ocorrência dos caracteres
nela contidos. Ao final imprima os caracteres e
suas respectivas frequências quando forem maiores que zero.
===========================================================
    '''
)
msg = ''
while True:
    msg = input("Digite uma string: ").encode()  # recebe input do usuario
    tcp.send(msg)  # manda a mensagem para o servidor
    print('msg enviada')  # confirma envio de mensagem
    resp = (tcp.recv(1024)).decode()  # recebe resposta do servidor
    print(resp)  # imprime resposta
    aux = int(input('Deseja continuar 0[nao] 1[sim]: '))  # entrar ou não com outra string
    if aux == 0:
        break
tcp.close()  # fecha conexao
print('Conexão interrompida pelo client!')

