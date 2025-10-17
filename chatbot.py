import re


# Return a list of lower case tokens consisting of alphanumeric chars
def parse_string(s):
    words = s.lower().split()
    return words

# Checks for valid product number
def valid_prodnum(x):
    return (re.search(r"\d{4}", x) is not None) and (len(x) == 4)

def main():

    responses = [
        "Type \'product\' for help with choosing a product,  \'lost\'  for help with a lost package,  \'trouble\'  for help with a technical problem or \'end\' to finish this session\n",
        "For further assistance, contact customer support at XXX-XXXX \n",
        "For further assistance, contact technical support at XXX-XXXX \n",

    ]
    products = [
        "What type of product are you interested in? \n",
        "Here is a link for more information phone plans {URL} \n",
        "Here is a list of available laptops {LAPTOP LIST} \n",
     "Would you like to purchase laptop? If there is an item that you are interested in, please type the 4 digit product number here, or type \'0\' for help in a different query: \n",
     "Here is a link for ordering product number: XXXXX \n"
    ]

    end = "Thank you, I hope we were able to be of assistance \n"

    user = ""

    # Main Chat loop
    while (True):
        print("What can I help you with?")
        step = 1
        while (step == 1):
            user = input(responses[0])
            words = parse_string(user)
            if ("end" in words):
                print(end)
                return
            elif ("product" in words) or ("1" in words):
                print("Need help with choosing a product? \n")
                step = 2
            elif ("lost" in words) or ("2" in words):
                print("Need help with a lost package?", responses[1])
                step = 0
                break
            elif ("trouble" in words):
                print("Need help with troubleshooting?", responses[2])
                step = 0
                break
            else:
                print(responses[0])
                user = ""
                step = 0
                break

        while (step == 2):
            user = input(products[0])
            words = parse_string(user)

            if ("laptop" in words):
                print(products[2])
                step += 1

            elif ("phone" in words):
                print(products[1])
                step = 0
                break
            else:
                print("Type \'laptop \' for help with selecting a laptop, or type \'phone\' for a list of phone plans")

        while (step == 3):
            words = input(products[3])
        
            if valid_prodnum(words):
                step += 1

            elif (words == "0"):
                step = 0
                break

            else:
                print("Please type a valid product number.")

        if (step == 4):
            print(products[4])





if __name__ == "__main__":
    main()


