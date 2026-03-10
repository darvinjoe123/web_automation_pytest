import inspect

#CONSTANTS

URL = "YOUR WEBSITE URL"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

def whoami():
    return inspect.stack()[1][3]