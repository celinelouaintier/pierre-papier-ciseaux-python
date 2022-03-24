from unicodedata import name


class Participant:
# _init_ = première méthode définie de la classe, se comporte un peu comme un constructor. 
    # on définit un état à chaque instance qui se mettra à jour au cours du jeu
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
# "rempli" self.choice avec une string dans laquelle on intègre le nom du joueur pour le faire choisir.
    # toujours préciser le .format lorsqu'on intègre une variable avec des accolades.
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name=self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))
# on transforme les signes en chiffres avec l'obj switcher auquel on assigne self.choice (l.10)
    def toNumericalChoice(self):
        switcher = {
            "rock":0,
            "paper":1,
            "scissor":2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1

class GameRound:
# définition des règles via une matrice (cf compareChoices l.48) 
    def __init__(self, p1, p2):
        self.rules= [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
# pour print, on crée une variable result1 qui rapelle la fonction compareChoices l.48 (qui compare et retourne un chiffre entre -1 et 1)
    # on crée une variable result pour passer result 1 en paramètres de la fonction getResultAsString l.51 (transforme le chiffre en résultat string)
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result}".format(result= self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
        else:
            print("No points for anybody")
    def awardPoints(self):
        print("implement")
# le p1 choisi l'index du tableau self.rules (l.30) PUIS le p2 choisi un index du tableau que le p1 a choisi (on obtient donc -1, 1 ou 0)
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
# le résultat du tour est re-transformé en string pour afficher égalité / gagné / perdu 
    def getResultAsString(self, result):
        res = {
            0:"draw",
            1:"win",
            -1:"loss"
        }
        return res[result]

class Game:
# on définit un état à chaque instance. On met les prénoms en paramètres de la classe Participant (l.4)
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Henry")
        self.secondParticipant = Participant("Dalida")
# Tant que le jeu n'est pas terminé (self.EndGame = False) la classe GameRound (l.27) continue à tourner puis on appelle checkEndCondition (l.73) à chaque fin de tour
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
# Rajoute une phrase pour continuer le jeu ou pas (le joueur choisi)
    # Condition en fonction du choix du joueur : si oui on relance GameRound (l.27) + checkEndCondition (l.73)
                                               # si non on print une phrase bilan du jeu qui annonce le gagnant + changer l'état de self.endGame (l.62)
    def checkEndCondition(self):
        answer = input("Continue game y/n")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name= self.secondParticipant.name, p2points = self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
# Création d'une instance avec état modifiable qu'on print à la fin des conditions:
    # si points p1 > points p2 l'état de self.resultString (l.86) change pour annoncer p1 gagnant 
    # exactement l'inverse
    def determineWinner(self):
        resultString = "It's a draw !"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

# On crée une variable game pour pouvoir appeler la méthode start (l.66) de la classe Game (l.59) et démarrer le jeu
game = Game()
# pas besoin de préciser self dans les paramètres même si précisé avant, python est smart
game.start() 