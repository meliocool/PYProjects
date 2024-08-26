class Human:
    alive = True
    def eat(self):
        print("This human could eat")
    def sleep(self):
        print("This human could sleep")
class NPC(Human):
    def yap(self):
        print("NPCs could yap nonsense")
class idol(Human):
    def sing(self):
        print("idols could sing")
class tripleS(idol):
    def objekt(self):
        print("This idol has an objekt Photocard")
class hyuna(idol,NPC):
    def loser(self):
        print("Im a failure of an idol")
