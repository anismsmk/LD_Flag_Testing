# Hello! =)
import ldclient
from ldclient.config import Config

# Simple Factorial Function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Create a helper function for rendering messages.
def show_message(s):
  print("*** %s" % s)
  print()
    
# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-544ef775-28b1-4857-843c-5d4eb4799cbe"))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  show_message("SDK successfully initialized!")
else:
  show_message("SDK failed to initialize")
  exit()

# Set up the user properties. This user should appear on your LaunchDarkly users dashboard
# soon after you run the demo.
user = {
  "key": "happy-user",
  "name": "Morty"
}
# user = {
#   "key": "grumpy-user",
#   "name": "Rick"
# }

# Call LaunchDarkly with the feature flag key you want to evaluate.
flag_value = ldclient.get().variation("FirstFlag", user, False)

if flag_value :
  show_message("Feature flag 'FirstFlag' is %s for this user" % (flag_value))
  show_message("Your name is %s " % (user['name']))
  show_message("You are %s" % (flag_value))

# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. If analytics events are not delivered,
# the user properties and flag usage statistics will not appear on your dashboard. In a
# normal long-running application, the SDK would continue running and events would be
# delivered automatically in the background.
ldclient.get().close()