# Hello! =)

import ldclient
from ldclient.config import Config
from backstage import * 
  
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
name = input('What is your name?\n') 

# Evaluate user
user = evaluate(name)

# Call LaunchDarkly with the feature flag key you want to evaluate.
flag_value = ldclient.get().variation("FirstFlag", user, False)
show_message("Feature flag 'FirstFlag' is %s for this user" % (flag_value))

if flag_value :
  show_message("Your name is %s " % (user['name']))
  show_message("You are %s" % (flag_value))

if not flag_value :
  show_message("NOT")

ldclient.get().close()
########## End of Main Stuff ###########