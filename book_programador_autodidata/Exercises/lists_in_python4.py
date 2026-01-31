rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }

n = input("Selecione um número de 1 a 5: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Não funcionou, tente novamente...")