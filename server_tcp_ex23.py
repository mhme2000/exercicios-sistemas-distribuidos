import socket

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
def isAnagram(word1, word2):
    if(len(word1) != len(word2)):
        return False
    list1 = list(word1)
    list1.sort()
    list2 = list(word2)
    list2.sort()
    position = 0

    while position < len(word1):
        if list1[position] == list2[position]:
            position = position + 1
        else:
            return False

        return True
con, cliente = tcp.accept()
print ('Conectado por', cliente)
while True:
    word = str(con.recv(1024).decode())
    if (word == "0"):
        con.close()
        break
    otherWord = str(con.recv(1024).decode())
    anagramResult = isAnagram(word, otherWord)
    result = bytes(str(anagramResult), 'utf-8')
    con.send(result)
