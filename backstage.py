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
    print("BYYYYE")
    quit(1)
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
