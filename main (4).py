# define the base class player
class player:
  def player(self):
     print("the player is playing cricket")

#define the derived class batsman
class batsman(player):
  def play(self):
    print("the batsman is batting")

#define the derived class bowler
class Bowler(player):
   def play(self):
     print("the bowler is bowling")

#create objects of batsman and bowler classes
batsman=batsman()
bowler=Bowler ()

#call the play() method for each object
batsman.play()
bowler.play()