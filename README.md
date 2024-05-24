<h1 align="center">Théorie de la Complexité</h1>

![time-complexity](https://github.com/mohamedtalhaouii/Complexity/assets/144726758/e63a513f-6f06-4a30-af8e-8a17d7087e4a)

<hr>

<h2 align="center"> Notation Big O : </h2>

**Définition :** Décrit la borne supérieure du temps d'exécution d'un algorithme. Elle donne le pire des cas de la manière dont le temps d'exécution augmente avec la taille de l'entrée.

   **Notations Big O courantes :**
- $`O(1)`$ : Temps constant.
-  $`O(\log n)`$ : Temps logarithmique.
-  $`O(n)`$ : Temps linéaire.
-  $`O(n \log n)`$ : Temps linéarithmique.
-  $`O(n^2)`$ : Temps quadratique.
-  $`O(2^n)`$ : Temps exponentiel.
-  $`O(n!)`$ : Temps factoriel.

![Big O](https://github.com/mohamedtalhaouii/Complexity/assets/144726758/0e1d6c72-1324-42a6-8e00-6db4d8e47d03)


<h2 align="center"> Complexité temporelle : </h2>

   - **Définition :** Mesure la quantité de temps qu'un algorithme prend pour s'exécuter en fonction de la longueur de l'entrée.
   - **Classes :**
-  **P :** Problèmes résolubles en temps polynomial.
-  **NP :** Problèmes pour lesquels une solution donnée peut être vérifiée en temps polynomial.
-  **NP-difficile :** Problèmes aussi difficiles que les problèmes les plus difficiles de NP ; pas nécessairement dans NP.
-  **NP-complet :** Problèmes de NP qui sont NP-difficiles.

<h2 align="center"> Complexité spatiale : </h2>

   - **Définition :** Mesure la quantité de mémoire qu'un algorithme utilise en fonction de la longueur de l'entrée.
   - **Classes courantes :**
-  **PSPACE :** Problèmes résolubles en utilisant une quantité polynomiale d'espace.
-  **L :** Problèmes résolubles en espace logarithmique.
-  **NL :** Problèmes résolubles en espace logarithmique non déterministe.

<h2 align="center"> Réduction et complétude : </h2>

   - **Réduction :** Transformation d'un problème en un autre. Utile pour prouver la difficulté d'un problème.
   - **Réduction en temps polynomial :** Utilisée pour montrer que si un problème peut être résolu en temps polynomial, un autre peut l'être aussi.

<h2 align="center"> Théorèmes de hiérarchie : </h2>

   - **Théorème de hiérarchie temporelle :** Il existe des problèmes qui peuvent être résolus en temps $`O(n^k)`$ qui ne peuvent pas être résolus en temps $`O(n^j)`$ pour $`j < k`$.
   - **Théorème de hiérarchie spatiale :** Il existe des problèmes qui peuvent être résolus en espace $`O(s(n))`$ qui ne peuvent pas être résolus en espace $`o(s(n))`$.

<h2 align="center"> Problèmes importants :</h2>

   - **Problème du voyageur de commerce (TSP) :** Trouver l'itinéraire le plus court possible visitant chaque ville une fois et revenant à la ville d'origine. NP-difficile.
   - **Problème du sac à dos :** Étant donné un ensemble d'objets avec des poids et des valeurs, déterminer le sous-ensemble le plus précieux qui rentre dans une limite de poids. NP-complet.
   - **Problème de satisfiabilité (SAT) :** Déterminer s'il existe une interprétation qui satisfait une formule booléenne donnée. NP-complet.

<h2 align="center"> Algorithmes d'approximation : </h2>

   - **Définition :** Algorithmes qui trouvent des solutions proches de l'optimal pour des problèmes d'optimisation.
   - **Exemples :** Algorithmes gloutons pour le TSP, méthodes heuristiques pour le sac à dos.

<h2 align="center"> Algorithmes randomisés : </h2>

   - **Définition :** Algorithmes qui utilisent des nombres aléatoires pour influencer le chemin d'exécution.
   - **Classes :**
-  **RP (Randomized Polynomial Time) :** Problèmes pour lesquels il existe un algorithme randomisé qui s'exécute en temps polynomial et a une probabilité d'au moins 1/2 de donner la bonne réponse.
-  **BPP (Bounded-error Probabilistic Polynomial Time) :** Problèmes pour lesquels il existe un algorithme randomisé qui s'exécute en temps polynomial et a une probabilité d'erreur bornée inférieure à 1/3.



<hr>
<h3 align="center"> 🧑🏻‍💻 | Made By : <a href="https://github.com/mohamedtalhaouii" target="_blank">Mohamed Talhaoui</a></h3>
