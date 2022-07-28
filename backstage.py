# Evaluate User name
def evaluate(name):
  if name == 'Morty' :
    user = {
      "key": "happy-user",
      "name": "Morty"
    }
    return user
  elif name == 'Rick' :
    user = {
      "key": "grumpy-user",
      "name": "Rick"
    }
    return user
  else:
    print("You do not exist. :/ ")
    cogito = input('Would you like to exist? Y / N \n')
    if cogito == "Y" :
      print("Cogito ergo sum\n")
      user = createNew(name)
    else:
      print("BYYYYYYYYEEEEE")
      quit()
    return user

# Create a helper function for rendering messages.
def show_message(s):
  print("*** %s" % s)
  print()

# Simple Factorial Function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def createNew(name):

  key = ""

  check = False
  while check == False :
    key = input("Choose key | format xxxx-user where xxxx is your key \n")
    if (len(name) == 0 or len(key) == 0) :
      check = False
    else:
      check = True
  user = {
    "key": key,
    "name": name
  }
  return user