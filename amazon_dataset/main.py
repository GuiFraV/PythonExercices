# r : lire fichier
# w : créer le fichier
# a : rajouter dez choses 
# liste = [" Hello EEMI\n", "Cours de Python\n"]
# # with open("mon_fichier.txt", "w") as file:
# #     # f.write("Hello EEMI")
# #     file.writelines(liste)

# with open("mon_fichier.txt", "r") as f:
#     data = f.readlines()

# print(data)

import csv

# data = [
#     {"name": "Younes", "Note": 15},
#     {"name": "Arnaud", "Note": 20},
#     {"name": "Adama", "Note": 14},
# ]
# with open('names.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)

import csv

data = []
cat = {} 
uniq = set() 

with open('Amazon-Products.csv', newline='',  encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        data.append(row)
        category = row['main_category']

        if category in cat:
            cat[category] += 1
        else:
            cat[category] = 1


    for row in reader:
        uniq.add(row['name'])
        
        # counter += 1
        # if counter == 10:
        #     break
total_items = sum(cat.values())

# Calculer et afficher le pourcentage pour chaque catégorie
for category, count in cat.items():
    percentage = (count / total_items) * 100
    print(f"{category}: {percentage:.2f}%")

print(cat)
print(len(uniq))
print(total_items)



    
    
#  Lire le fichier et afficher les 10 premiers éléments
#  Chercher le nombre total de produits et le nombre de produiyts par catégorie
#  Combien de produits unique
#  C'est quoi le pourcentage de produits par catégorie
#  Avoir le 20 produits les plus cher (et les moins cher)
#  chercher les 15 prduits les mieux notés
#  Checker si l'image existe sur internet