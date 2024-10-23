# Exercice 6 : Générateur de nombres

# Écris une fonction get_number() qui :

#    -Demande à l'utilisateur de saisir un nombre.
#    -Essaie de convertir l'entrée en entier.
#    -Si l'utilisateur saisit une chaîne non convertible en entier (par exemple, des lettres), 
#     attrape l'exception correspondante et demande une nouvelle entrée jusqu'à ce qu'un nombre valide soit saisi.
#    -Affiche un message dans le bloc finally après que l'utilisateur a saisi un nombre valide.

def get_number():
    while True :
        try :
            user_input = input("Saisir un entier svp : ")
            convert_user_input = int(user_input)
            print(f"Vous avez saisi : {convert_user_input}")
            break # Sortie de la boucle si un entier valide est saisi
        except ValueError as e :
            print(f"{e}\t(Vous devez saisir que des chiffres svp) ")
        finally :
            e = "execution terminé"
            print(e)
    
# application 

get_number()
        
    
