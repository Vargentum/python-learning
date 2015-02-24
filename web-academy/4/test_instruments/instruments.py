class Instrument(object):
  def __init__(self, name):
    self.name = name

  def play(self):
    return 'Playing on {}'.format(self.name)

  def __str__(self):
    return 'Instrument: {}'.format(self.name)


class Guitar(Instrument):
  def __init__(self, name, strings):
    self.name = name
    self.strings = strings
    super().__init__(name)

  def play(self):    
    import random
    break_string_chance = random.randint(0,100)

    if break_string_chance == 1 and self.strings != 0:
      self.strings -= 1

    if self.strings > 0:
      # super().play()
      return 'Playing on %s' % self.name
    else:
      return 'Can not play, no strings :('


class Ukulele(Guitar):
  def __init__(self, name):
    self.strings = 4
    super().__init__(name, self.strings)
