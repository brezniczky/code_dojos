import unittest;

# Task outline:

# First pomodoro
#
# 3 classes
# superclass Thing
# all have a method "beats" takes an object
# of class Thing (or a subclass) and returns
# True, False or None
#
# Second pomodoro
# 
# Change the classes so that of all the 
# conditionals are gotten rid of.
#
# Third pomodoro
#
# Extension: the "Lizard Spock" way.
# see https://en.wikipedia.org/wiki/Rock-paper-scissors#Additional_weapons

# remarks:
# we don't actually need classes for this - these are simply enums
#
# we could just test the "beats" method in isolation - as there are many test 
# cases, and there is a very simple implementation, it is probably more 
# reasonable to incorporate the 'beats' logic into the Thing class as 
# parameters, maybe a class, which 

class Thing:
  @classmethod
  def set_rules(cls, who_beats_who):

    things_1 = {pair[0] for pair in who_beats_who}
    things_2 = {pair[1] for pair in who_beats_who}
    things = things_1.union(things_2)

    # add asymmetry (if A beats B then B is beaten by A)
    for pair, beats in who_beats_who.items():
      if beats is not None:
        (A, B) = pair
        who_beats_who[(B, A)] = not beats

    # add "diagonal" (thing - thing: undecisive, i.e. tie)
    for thing in things:
      who_beats_who[(thing, thing)] = None

    # add tie against a generic Thing
    for thing in things:
      who_beats_who[(Thing, thing)] = None
      who_beats_who[(thing, Thing)] = None

    Thing.__who_beats_who__ = who_beats_who

  def beats(self, another_thing):
    return(Thing.__who_beats_who__[(self.__class__, \
                                    another_thing.__class__)])

class Rock(Thing): pass

class Scissors(Thing): pass 

class Paper(Thing): pass

# class Lizard(Thing): pass

# class Spock(Thing): pass

Thing.set_rules(
  {(Thing, Rock): None,
   (Rock, Scissors): True,
   (Paper, Rock): True,
   (Scissors, Paper): True}
)

class TestThings(unittest.TestCase):
  def assert_beats(self, class1, class2, result):
    t1 = class1()
    t2 = class2()
    self.assertEquals(t1.beats(t2), result)

  def test_Thing_beats_None(self):
    self.assert_beats(Thing, Thing, None)

  def test_Rock_not_beats_Rock(self):
    self.assert_beats(Rock, Rock, None)

  def test_Rock_beats_Scissors(self):
    self.assert_beats(Rock, Scissors, True)

  def test_Scissors_beatenby_Rock(self):
    self.assert_beats(Scissors, Rock, False)

if __name__ == "__main__":
  unittest.main()
