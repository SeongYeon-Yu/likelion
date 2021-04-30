dictionary = {"멋사": "멋쟁이 사자처럼", "파이썬": "지금 배우는 언어"}

def create_word():
  create = input("Enter word: ")
  mean = input("Eneter meaning: ")
  print("The word has been successfully registered!\n")
  dictionary[create] = mean

def read_dictionary():
  for key, value in dictionary.items():
    print(key,": ", value)
#    print(dictionary.get, ": ", dictionary, "\n")
   
def update_word():
  update = input("Enter word: ")
  if(update in dictionary):
    mean = input("Eneter meaning: ")
    dictionary[update] = mean
  else :
    return print("You don't have this word in your dictionary\n")

def delete_word():
  delete = input("Enter word: ")
  if(delete in dictionary):
    del dictionary[delete]
  else :
    return print("You don't have this word in your dictionary\n")

def console_help():
    print("Command list")
    print("---")
    print("C for create")
    print("R for read")
    print("U for update")
    print("D for delete")
    print("Q for quit")

def receive_input():
    command = input("Input command: ")
    if command == 'c' or command == 'C':
        create_word()
        return True
    if command == 'r' or command == 'R':
        read_dictionary()
        return True
    if command == 'u' or command == 'U':
        update_word()
        return True
    if command == 'd' or command == 'D':
        delete_word()
        return True
    if command == 'q' or command == 'Q':
        return False
    else:
        print("Please enter one of the letters above.")
        return True

def main():
    console_help()
    while receive_input():
        pass

if __name__ == "__main__":
    main()