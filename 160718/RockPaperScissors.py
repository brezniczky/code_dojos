import unittest;

# 3 classes
# superclass Thing
# all have a method "beats" takes an object
# of class Thing (or a subclass) and returns
# True, False or None

class Thing:
  def beats(self, another_thing):
    return(Thing.__who_beats_who__[(self.__class__, \
                                    another_thing.__class__)])


class Rock(Thing): pass

class Scissors(Thing): pass 

class Paper(Thing): pass

# class Spock(Thing): pass

# class Lizard(Thing): pass

# remarks:
# we don't actually need classes for this - these are simply enums
# we could just test the "beats" method in isolation

Thing.__who_beats_who__ = \
  {(Thing, Thing): None,
   (Rock, Rock): None,
   (Rock, Scissors): True,
   (Scissors, Rock): False,
   (Rock, Paper): False,
   (Paper, Rock): True,

   (Scissors, Scissors): None,
   (Scissors, Paper): True,
   (Paper, Scissors): False,

   (Paper, Paper): None}


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

# class Rock(Thing):
#   def beats(another_thing)
#     if another_thing ==

# {(Rock, Rock): None,
#  (Rock, Paper): False,
#  (Rock, Scissor): True]


