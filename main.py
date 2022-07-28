# Hello! =)

import ldclient
from ldclient.config import Config
from backstage import * 
from rps import *
  
# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-544ef775-28b1-4857-843c-5d4eb4799cbe"))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  show_message("SDK successfully initialized!")
else:
  show_message("SDK failed to initialize")
  exit()

########## Main Stuff ##########
# Get User input
name = input('What is your name? (Rick, Morty or Other)\n') 

# Evaluate user
user = evaluate(name)

# Call LaunchDarkly with the feature flag key you want to evaluate.
flag_value = ldclient.get().variation("FirstFlag", user, False)
show_message("Feature flag 'FirstFlag' is %s for this user" % (flag_value))
game_value = ldclient.get().variation("GameFlag", user, False)
show_message("Feature flag 'GameFlag' is %s for this user" % (game_value))

if flag_value :
  show_message("Your name is %s " % (user['name']))
  show_message("You are %s" % (game_value))
  rps()

if not flag_value :
  show_message("Your name is %s " % (user['name']))
  show_message("You are %s" % (game_value))
  rps_crazy()

ldclient.get().close()
########## End of Main Stuff ###########