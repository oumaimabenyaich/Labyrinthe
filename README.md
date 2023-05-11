# $$\color{purple}\boxed{\mathbb{ Road \space Poneglyphe}}$$

## $Deux \space joueurs \space s'affrontent. \space L'objectif \space ? \space Récolter \space un \space maximum \space de \space trésor \space avant \space l'adversaire.$

*Vous disposez d'une tuile permettant de déplacer le plateau afin de trouver un chemin vers votre trésor. Chaque trésor a une position précise qui vous est fourni, les joueurs ont un nombre de trésor qui décroit à chaque fois qu'ils en attrapent un.*

![Ceci n'est pas une image](https://64.media.tumblr.com/d81bbceaa25de79b5308d42c24b967f3/tumblr_nidl3wAx3t1twwodoo3_r1_500.gifv)

## $\color{red}> \space Règles \space du \space jeu \space < $

- Chaque tour est composé de deux actions : 
  - insérer la tuile supplémentaire
  - déplacer le pion
- La tuile ne peut être insérer que là où il y a des flèches
- La nouvelle tuile est passée au joueur suivant
- Le pion doit se déplacer vers le trésor par le chemin le plus rapide
- Il faut respecter les chemins 
- Le joueur peut s'arrêter sur n'importe quelle case, il peut traverser une case où un pion est déjà présent et même s'arrêter dessus
- Si un joueur sort du plateau, il réapparait de l'autre côté du plateau sur la même ligne
                           
$$\color{lightpink}<sub> Pour \space la \space bibliothèque \space du \space jeu \space : \space voir \space requirements$$

Le jeu fonctionne en commencant par generer les portes ou on peut jouer
il s agit des portes qui n exclue pas la tuile contenant le tresor
ensuite il genere une map porte par porte afin de simuler le poussage de tuile(la tuile utiliser est une tuile ouverte sur les 4 coté)
le jeu gener un chemin pour ttes les porte essayer
on regarde quel chemin mene a la position la plus proche du tresor
enfin on genere la tuile qui sera placer a la place de la tuile ouverte de partout


pour lancer le jeu entree la commande "python Client_avenir.py"