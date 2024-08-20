from class_1 import InstaFollower
SIMILAR_ACCOUNT = "thedogist"
USERNAME = "tanvir.python.test@gmail.com"
PASSWORD = "v%Fyr8Ea$o4y6X8(Y"

instabot = InstaFollower()

instabot.login()
instabot.find_followers()
instabot.follow()
