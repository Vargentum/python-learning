def revertToMetric(num, type):
  if type == 'inch':
    return num * 2.54

  elif type == 'lbs':
    return num * 0.453592



name = 'Zed A. Shaw'
age = 35 # not a lie
height = revertToMetric(74, 'inch')
weight = revertToMetric(180, 'lbs')
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d meters tall." % height)
print("He's %d kilogramms heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))
