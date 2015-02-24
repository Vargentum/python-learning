class Instrument(object):
  """docstring for Instrument"""
  def __init__(self, name):
    self.name = name
    return 'Instrument: %s' % self.name

  def play(self):
    return 'Playing on %s' % self.name



class Guitar(Instrument):
  """docstring for Guitar"""
  def __init__(self, strings):
    super(Guitar, self).__init__()
    self.strings = strings

  def play(self):
    if self.strings > 0:
      super(Guitar, self).play()
    else:
      return 'Can not play, no strings :('

    break_string_chance = random.randint(1,100)

    if break_string_chance == 1 and self.string != 0:
      self.string -= 1


class Ukulele(Guitar):
  """docstring for Ukulele"""
  def __init__(self):
    super(Ukulele, self).__init__()
    self.strings = 4

    