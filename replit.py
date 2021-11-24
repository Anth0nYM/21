import random

print("\n" * 100)
print('''
Jogo 21
--------------------------
Consiga 21 pontos no total!
''')

repetir = "s"
pontuacao = 0
cartasTotal = 0
tipos = ["♣", "♠", "♥", "♦"]
cartasAnteriores = {
"l1": "", "l2": "", "l3": "", "l4": "", 
"l5": "", "l6": "", "l7": "", "l8": "", 
"l9": ""
}

nome = str(input("Qual seu nome (Somente o primeiro nome)? Com ele suas vitórias serão salvas\n"))
nome = nome.replace(" ", "")

tabela = open("pontuacao.txt", "r").read()
tabela = tabela.splitlines()
for u in tabela:
    nomeSalvo, pontuacaoSalva = u.split("|")

    if (nomeSalvo == nome):
        pontuacao = int(pontuacaoSalva)

while repetir == "s":

    continuar = "s"
    while continuar == "s":
      numero = random.randint(1, 10)
      cartasTotal += numero
      tipo = random.choice(tipos)

      if numero == 10:
        espaco = ""
      else:
        espaco = " "
        
      print("\n"*100)

      cartasAnteriores["l1"] = str(cartasAnteriores.get("l1"))+"┌─────────┐"
      cartasAnteriores["l2"] = str(cartasAnteriores.get("l2"))+"│{}{}       │".format(espaco, numero)
      cartasAnteriores["l3"] = str(cartasAnteriores.get("l3"))+"│         │"
      cartasAnteriores["l4"] = str(cartasAnteriores.get("l4"))+"│         │"
      cartasAnteriores["l5"] = str(cartasAnteriores.get("l5"))+"│    {}    │".format(tipo)
      cartasAnteriores["l6"] = str(cartasAnteriores.get("l6"))+"│         │"
      cartasAnteriores["l7"] = str(cartasAnteriores.get("l7"))+"│         │"
      cartasAnteriores["l8"] = str(cartasAnteriores.get("l8"))+"│       {}{}│".format(numero, espaco)
      cartasAnteriores["l9"] = str(cartasAnteriores.get("l9"))+"└─────────┘"

      print("{}, Você já possuía {} vitórias\n".format(nome, pontuacao))

      print(        
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'
        '{}\n'.format(
          cartasAnteriores.get("l1"),
          cartasAnteriores.get("l2"),
          cartasAnteriores.get("l3"),
          cartasAnteriores.get("l4"),
          cartasAnteriores.get("l5"),
          cartasAnteriores.get("l6"),
          cartasAnteriores.get("l7"),
          cartasAnteriores.get("l8"),
          cartasAnteriores.get("l9"),
          ))

      if cartasTotal > 21:
        print("Não foi dessa vez! :(")
        continuar = "n"
        break
      
      elif cartasTotal == 21:
        print("Parabéns, 1 vitória será adicionada ao seu histórico!")
        pontuacao += 1
        continuar = "n"
        break

      else:
        print("Você está com {} pontos\n".format(cartasTotal))
        continuar = str(input('Deseja mais uma carta? (s/n)\n'))


    repetir = str(input("Deseja jogar novamente? (s/n)\n"))

    if repetir != "s":
        tabela = open("pontuacao.txt", "r").read()
        tabela = tabela.splitlines()

        novaTabela = open("pontuacao.txt", "w")

        if len(tabela) > 0:
            tabelaModificada = str()
            jaSalvo = False

            for u in tabela:
                nomeSalvo, pontuacaoSalva = u.split("|")

                if (nomeSalvo == nome):
                    jaSalvo = True
                    tabelaModificada += "{}|{}\n".format(nome, pontuacao)
                else:
                    tabelaModificada += "{}|{}\n".format(
                        nomeSalvo, pontuacaoSalva)

            if not jaSalvo:
                tabelaModificada += "{}|{}\n".format(nome, pontuacao)

            novaTabela.write(tabelaModificada)
            novaTabela.close()
        else:
            novaTabela.write("{}|{}".format(nome, pontuacao))
            novaTabela.close()
    else:
      print("\n"*100)
      cartasTotal = 0
      cartasAnteriores = {
      "l1": "", "l2": "", "l3": "", "l4": "", 
      "l5": "", "l6": "", "l7": "", "l8": "", 
      "l9": ""
      }