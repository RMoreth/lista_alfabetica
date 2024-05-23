# lista

nomes = ["alex", "simone", "Bernardo", "César", "Alexandra"]
nomes.sort(reverse=True)
for c, i in enumerate(nomes):
    print(f"{c + 1}º nome: {i}")

for i in range(len(nomes)):
    print(f'{i + 1} º nome da lista: {nomes[i]}')
