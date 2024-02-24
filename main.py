import requests

flags = ["nsfw", "religious", "political", "racist", "sexist", "explicit"]
catagories = ["Programming", "Misc", "Dark", "Pun", "Spooky", "Christmas"]

print("Enter numbers of flags to blacklist (seperated by commas):")
for elem in range(len(flags)):
  print(f"{elem+1}) {flags[elem]}")

choice = input()
flagsList = []
for elem in choice.split(","):
  if len(choice.split()) == 0:
    break
  flagsList.append(flags[int(elem) - 1])

print("Enter a catagory of joke (no value is any type)")
for elem in range(len(catagories)):
  print(f"{elem+1}) {catagories[elem]}")

catagory = input()

catagory = "Any" if catagory == "" else catagories[int(catagory) - 1]

outputFlags = ', '.join(
    flagsList) if len(flagsList) > 0 else "No blacklisted flags"

#print(f"Preparing a joke of type {catagory} with blacklisted flags being: {outputFlags}")

url = f"https://v2.jokeapi.dev/joke/{catagory}"

if len(flagsList) > 0:
  url += "?ablacklistFlags="
  url += ",".join(flagsList)
#print(url)

response = requests.get(url)
response = response.json()
#print(response)

if response["error"] == "true":
  print("An error occured, try again")
else:
  if response["type"] == "single":
    print(response["joke"])
  else:
    setup = response["setup"]
    delivery = response["delivery"]
    import time
    print(setup)
    time.sleep(2)
    print(delivery)
