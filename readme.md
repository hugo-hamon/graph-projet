# Quelques algorithmes d’approximation pour le problème du voyageur de commerce

## Introduction
Le problème du voyageur de commerce est un problème d’optimisation combinatoire. Il consiste à trouver le plus court chemin qui passe par toutes les villes d’un ensemble donné. Il est NP-complet, c’est-à-dire qu’il n’existe pas de solution exacte en temps polynomial. Cependant, il existe des algorithmes d’approximation qui permettent de trouver une solution en un temps raisonnable.

### Algorithme du plus proche voisin
L’algorithme du plus proche voisin est un algorithme glouton. Il consiste à commencer par une ville quelconque, puis à choisir à chaque étape la ville la plus proche de la ville précédente. L’algorithme est très simple à implémenter, mais il n’est pas optimal. En effet, il peut trouver des solutions qui sont plus longues que la solution optimale.

### Algorithme du plus proche voisin amélioré
L’algorithme du plus proche voisin amélioré est basé sur le résultat de l'algorithme du plus proche voisin. Il consiste à défaire les croisements de chemins, c’est-à-dire à inverser les segments de chemins qui se croisent. L’algorithme est plus complexe à implémenter, mais il est plus efficace que l'algorithme du plus proche voisin.

### Algorithme de l'arête de poids minimum
L’algorithme de l'arête de poids minimum est un algorithme glouton. Il consiste à commencer par une arête quelconque, puis à choisir à chaque étape l’arête de poids minimum qui n’a pas encore été choisie. L’algorithme est très simple à implémenter, mais il n’est pas optimal.

### Algorithme de prim
L’algorithme de prim construit un arbre couvrant de poids minimum. Il consiste à commencer par une arête quelconque, puis à choisir à chaque étape l’arête de poids minimum qui n’a pas encore été choisie et qui ne referme pas le graphe prématurément. L’algorithme est très simple à implémenter, mais il n’est pas optimal.

### Algorithme branch and bound avec l'heuristique de la demi-somme

L'algorithme branch and bound avec l'heuristique de la demi-somme est une méthode efficace pour résoudre le problème du voyageur de commerce. Il combine l'utilisation de l'algorithme branch and bound pour éliminer les branches non prometteuses avec l'utilisation de l'heuristique de la demi-somme pour estimer la distance minimale entre les villes non visitées et la ville actuelle. Cette combinaison permet de réduire considérablement le nombre de branches explorées et d'améliorer les performances de l'algorithme, en augmentant la vitesse de résolution du problème.

## Exécution

### Prérequis

Pour exécuter le programme, il faut avoir installé Python 3.10 ou une version ultérieure.

### Installation

Pour exécuter le programme, il suffit de lancer le fichier `main.py` avec Python.

### Utilisation

Le programme dispose d'un fichier de configuration `config.json` qui permet de configurer les paramètres de l'algorithme. Il est possible de modifier les paramètres suivants :

- `city_numbers` : nombre de villes
- `iterations_numbers` : nombre d'itérations
- `show_graph`:  afficher la matrice des distances
- `show_info`: afficher les informations sur les villes
- `brute_force`: utiliser l'algorithme de brute force
- `execution_time`: afficher le temps d'exécution pour chaque algorithme

Les algorithmes tel que brute force et branch and bound avec l'heuristique de la demi-somme sont très longs à exécuter. C'est pour cela que ces derniers sont désactivés lorsque que `city_numbers` est supérieur à 10.

## Auteurs

- [@Hugo Hamon](https://github.com/hugo-hamon)
- [@Pierrep02](https://github.com/Pierrep02)
- [@Erwann27](https://github.com/Erwann27)
- [@Dyamen1411](https://github.com/Dyamen1411)

## License

[MIT](https://choosealicense.com/licenses/mit/)
