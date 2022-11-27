import socket

HOST = ''          # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    print("Servidor iniciado\n")  # mensagem para confirmar inicio do servidor
    con, cliente = tcp.accept()  # conexao com cliente via tcp
    print(f'Conectado por {cliente}')  # mostra qual cliente foi conectado
    while True:
        a = 0  # menor caracter unicode inteiro
        z = 65533  # maior caracter unicode inteiro
        valores = ''  # variável para guardar a resposta
        aux = []  # variável para guardar a resposta parte 2
        msg = (con.recv(1024)).decode()  # recebe string do usuario
        while a != z:  # loop para percorrer a string
            if msg.count(chr(a)) != 0:  # toda vez que ocorrer um caracter ira ser incrementado
                valores = str(chr(a)) + " = " + str(msg.count(chr(a)))  # guarda em uma string a quantidade do caracter
                aux.insert(0, valores)  # insere o resultado de cada caracter em uma das posições da lista
            a = a + 1  # incrementa o valor de a
        if not msg:  # se não existir mensagem
            break
        result = bytes(str(aux), 'utf-8')  # transforma a lista em string e depois para bytes
        con.send(result)  # envia o resultado para cliente
    print(f'Finalizando conexao do cliente {cliente}')  # mostra que a conexão foi finalizada com o cliente x
    aux = input('Deseja manter servidor ativo? (s/n)')  # decidir se manter ou não o servidor de pé
    if aux == 'n':
        break
tcp.close()
