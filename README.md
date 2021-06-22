# Hangman
Hangman in Python

CUM SE JOACA:
1- Se ruleaza HangmanGame.py
2- Se scrie 1 pentru 1 player mode sau 2 pentru 2 player mode
3.1- Penru 1 player mode se fac ghiciri pana cand se opreste jocul (ca a castigat sau pierdut)
3.2- Pentru 2 player mode, player 1 sccrie cuvantul pe care o sa il aiba de citit player 2 dupa care se executa pasul 3.1)

EXPLICATIE COD:

1) HangmanDrawings.py
Aici sunt 7 metode de afisare a spanzuratorii (initialize() - de la care se pleaca, head() - prima greseala, body() - a doua greseala, leftArm() - a treia greseala, rightArm() - a patra greseala, leftLeg() -  a cincea greseala, rightLeg() - a sasea si ultima greseala)

2) HangmanGame.py
Acest joc are 2 moduri:
- unul in care se alege un cuvant aleator din lista de cuvinte (listOfWords) (1 player mode)
- unul in care cuvantul ales este cel scris de unul dintre cei 2 jucatori    (2 players mode)

Mai intai se citeste de la tastatura modul in care se doreste sa fie jucat spanzuratoarea (1 - 1 player mode, 2 - 2 players mode)
Dupa se testeaza daca 'mode' este egal cu 2, iar in caz afirmativ se citeste de la tastatura cuvantul. Daca 'mode' este 1 atunci se stocheaza in variabila 'word' un cuvant aleator din lista de cuvinte 'listOfWords'.

In lista 'lettersGuessed' se retine literele ghicite de catre player.
In lista 'wordLetters' se stocheaza mai intai atatea - cate litere are cuvantul ghicit, iar pe masura ce se face o ghicire corecta a uneia dintre litere atunci o sa se inlocuiasca '-' cu litera corespunzatoare (ex: cuvantul este 'masina', iar daca se ghiceste 'a' atunci in loc de '------' se afiseaza '-a---a')

2.1) Metoda checkWinner()
Se verifica daca jocul este pierdut (numarul de greseli retinute in variabila 'wrong' este 6 - se returneaza 0), se poate continua (daca mai sunt '-' in lista 'wordLetters' - se returneaza 1) sau daca este castigat (se returneaza 2)

2.2) Metoda letterGuessedorNot(letter)
Se verifica daca s-a facut o ghicire corecta a literei 'letter'.
Se parcurge fiecare litera a variabilei 'word', iar daca este o potrivire atunci se inlocuieste in 'wordLetters' cratima cu litera, se adauga la final litera ghicita in 'lettersGuessed' si contorul 'ok' se face 1.
Daca 'ok' este 1 atunci s-a facut o ghicire corecta si se returneaza 0, iar in caz contrar se incrementeaza variabila 'wrong', se adauga litera in 'lettersGuessed' si se returneaza 0

2.3) whatToDraw()
In functie de numarul de greseli se apeleaza metodele din HangmanDrawings.py

2.4) letters()
Aceasta metoda face afisarea listelor 'lettersGuessed' si 'wordLetters'

In bucla infinita de la linia 77:
Se verifica daca checkWinner() returneaza 0 (daca da atunci player 2 a pierdut si se da break) sau 2 (player 2 a castigat si se da break), daca returneaza 1 atunci se citeste iar o litera si se apeleaza metodele de letterGuessedorNot(guess), whatToDraw() si letters()

