from cgi import print_form


nome = "Adalmando"
idade = 21
altura = 1.75

def imprimeInfos(nome, idade, altura):
    print_form("Nome: %s\nIdade: %d\nAltura: %.2f", nome, idade, altura)

imprimeInfos()
    
