#sem with 
arquivo = open("meuarquivo.txt","w",encoding="utf-8")
arquivo.write("fala eita tudo certo")
arquivo.close

#com with 

with open("meuarquivo.txt","w",encoding="utf-8") as arquivo:
    arquivo.write("fala eita tudo certo maninho como vai?")

#ler com with
with open("meuarquivo.txt","r",encoding="utf-8") as arquivo:
    print(arquivo.read())