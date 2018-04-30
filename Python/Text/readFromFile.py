# from https://repl.it/@abdullahkobir/Read-From-Text-File


def readfile():
  file = open("inventory.txt","r")
#Repeat for each item in the inventory text file
  for line in file:

  #Let's split the line into an array called "fields" using the ";" as a separator:
    fields = line.split(",")
    if len(fields) == 4:
  #and let's extract the data:
        item = fields[0]
        attack = fields[1]
        defense = fields[2]
        gold=fields[3]
        #Print the Item
        print("Item: "+item+" Attack: "+attack+" Defense: "+defense+" Gold:"+gold)
  file.close()

def writefile():
  file = open("inventory.txt","a")
  country = raw_input("Name the country you are attacking:")
  economy = raw_input("How much does it increase your economy?")
  population = raw_input("How much does it increase your army/population?")
  gold = raw_input("How much gold will you get?")

  file.write('\n'+country+", "+economy+", "+population+", "+gold)
  file.close()
#It is good practice to close the file at the end to free up resources

#Main Program
choice="blank"
while choice != "end":
  choice = raw_input("Would you like to read from war stats, write to war stats, or confirm war stats?")
  if choice == "read":
    readfile()

  elif choice == "write":
    writefile()

  elif choice == "end":
    print("we will see you at the war sergentend")
    break

  else:
    print("Please choose read, write or end.")
