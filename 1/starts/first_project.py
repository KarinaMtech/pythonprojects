# madlibs.py
# entender como receber entradas do usuário, trabalhar com f-strings (strings com formatação) e ver seus resultados impressos no console

# youtuber = "Cold Play"

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madLib = f"Computer programming is so {adj}! Its makes me excited all the time because \n I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}"

print(madLib)
