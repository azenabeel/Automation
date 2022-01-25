import sys
import clipboard        #import sys
import json



SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:  #overwrite file if already exsists or craete a new one
        json.dump(data, f)

#save_items("test.json", {"key":"value"})
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f) #json returns data in form of py dict
            return data
    except:
        return {} #return empty dict

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA) #data dict

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved!")

    elif command == "load":
        key= input("Enter the key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key doesnot exsist.")
    
    elif command == "list":
        print(data)
    
    else:
        print("Unknown command")

else:
    print("Please pass exactly one command")
