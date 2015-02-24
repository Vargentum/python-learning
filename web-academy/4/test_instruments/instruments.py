class Instrument(object):
  """docstring for Instrument"""
  def __init__(self, name):
    self.name = name

  def play(self):
    return 'Playing on %s' % self.name

  def __str__(self):
    return 'Instrument: %s' % self.name


class Guitar(Instrument):
  """docstring for Guitar"""
  def __init__(self, name, strings):
    self.name = name
    super().__init__(name)

  def play(self):
    if self.strings > 0:
      return 'Playing on %s' % self.name  
    else:
      return 'Can not play, no strings :('

    break_string_chance = random.randint(1,100)

    if break_string_chance == 1 and self.string != 0:
      self.string -= 1


class Ukulele(Guitar):
  """docstring for Ukulele"""
  def __init__(self, name):
    self.strings = 4
    super().__init__(name)

    