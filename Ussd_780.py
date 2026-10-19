from re import fullmatch

import random


def shomenu(menu: dict) -> str:
    """It takes a dictionary and displays the key-value 
    pairs in an organized manner in the output.

    Args:
        menu (dict):

    Returns:
        str:
    """
    for key, value in menu.items():
        print(f"{key} : {value}")


def isvalid(value: str, pattern: str) -> bool:
    """It takes a value and a pattern,
     and returns `true` if the value matches the pattern.

    Args:
        value (str): can use for names numbers or ...
        pattern (str): Regex pattern (r"[a-zA-Z]+") 

    Returns:
        bool: true | false
    """
    from re import fullmatch

    if fullmatch(pattern, value):
        return True
    else:
        return False


def random_numbers(start: int = 1000, stop: int = 9999) -> str:
    try:
        int(start)
        int(stop)
    except Exception as error:
        raise error

    poya_password = random.randint(start, stop)
    return poya_password


# (get second password)
def gsp():
    user_chois = input("""if your information are correct 
    for get ramz poya Enter (1) for exit (2): """)
    if "1" in user_chois:
        password = random_numbers(100000, 999999)
        print(password, "\n")
        if input("plese Enter ramz poya: ") == str(password):
            return True
        else:
            print("your password is incorrct", "\n")
    else:
        return False


def information(menu: dict, paramert):
    user_phone_number = input("please add your phone number: ")
    if isvalid(user_phone_number, valid_number):
        shomenu(menu)
        user_chois2 = input("please Enter your chois: ")
        if isvalid(user_chois2, paramert):
            user_credit_card = input("please Enter your Credit card: ")
            if isvalid(user_credit_card, r"[0-9]{16}"):
                user_information = {
                    "phone number": user_phone_number,
                    "Your package": menu.get(user_chois),
                    "credit card": user_credit_card
                }
                return user_information
            else:
                return ("Error in input data", "\n")
        else:
            return ("Error in input data", "\n")
    else:
        return ("Error in input data", "\n")


def information_operator():
    shomenu(operator_menu)
    user_oprator = input("plese Enter your operator: ")
    if isvalid(user_oprator, r"[1-3]"):
        shomenu(shazh_mostaghim_menu)
        user_chois = input("plese Enter your chois: ")
        if isvalid(user_chois, r"[1-5]"):
            user_credit_card = input("please Enter your Credit card: ")
            if isvalid(user_credit_card, r"[0-9]{16}"):
                user_information = {
                    "operator": user_oprator,
                    "credit card": user_credit_card,
                    "sharzh(riyal)": shazh_mostaghim_menu.get(user_chois)
                }
                return user_information
            else:
                return ("Error in input data", "\n")
        else:
            return ("Error in input data", "\n")
    else:
        return ("Error in input data", "\n")


valid_number = r"(09\d{9}|\+989\d{9}|00989\d{9})"
score = 0

main_menu = {
    "1": "instal",
    "2": "sharzh",
    "3": "ghore keshi",
    "4": "internet",
    "5": "Exit",
    "score": score
}

sharzh_menu = {
    "1": "mostaghim",
    "2": "ramz sharzh",
    "3": "Exit",
}

shazh_mostaghim_menu = {
    "1": "10,000",
    "2": "20,000",
    "3": "50,000",
    "4": "100,000",
    "5": "200,000"
}

operator_menu = {
    "1": "hamerah aval",
    "2": "irancel",
    "3": "ritel"
}

ghore_keshi_menu = {

    "1": "Participating in the lucky draw",
    "2": "information",
    "3": "This month's winners",
    "4": "Exit"
}

select_menu = {
    "1": "Convert all points into chances.",
    "2": "Turning a point into an opportunity",
    "3": "Exit"
}

javayez = {
    "1": "PS5",
    "2": "iphon 16",
    "3": "XBOX seris S",
    "4": "sumsung TV",
    "5": "Refrigerator",
    "6": "Washing machine"
}

winners_month = {
    "ali reza tarani": javayez["1"],
    "mohamad moeini": javayez["4"],
    "sara rahmani": javayez["3"]
}

Daily_internet = {
    "1": "(2 gig) 15,000",
    "2": "(1 gig) 12,000",
    "3": "(750 mg) 11,000"
}

Monthly_internet = {
    "1": "(6 gig) 52,000",
    "2": "(5 gig) 44,000",
    "3": "(4 gig) 40,000"
}

Three_month_internet = {
    "1": "(80 gig) 610,000",
    "2": "(60 gig) 460,000",
    "3": "(45 gig) 345,000"
}

internet_menu = {
    "1": "Daily internet",
    "2": "Monthly internet",
    "3": "Three month internet",
    "4": "Exit"
}

while True:

    print("===== HAF HASTAD =====")
    shomenu(main_menu)
    user_chois = input("please Enter your chois: ")

    if isvalid(user_chois, r"[1-5]"):
        if "1" in user_chois:
            print("payamak havi link (Download) baraye shoma ersal shod")
            break
        elif "2" in user_chois:
            while True:

                shomenu(sharzh_menu)
                user_chois = input("please Enter your chois: ")
                if "1" in user_chois:
                    kharid = information(shazh_mostaghim_menu, r"[1-5]")
                    if type(kharid) == dict:
                        shomenu(kharid)

                        if gsp():
                            print("The operation was successfully completed")
                            score += 200
                            print("your score:", score)
                            break
                        else:
                            break
                    elif kharid:
                        print(kharid)
                    else:
                        break
                elif "2" in user_chois:
                    kharid = information_operator()
                    if type(kharid) == dict:
                        shomenu(kharid)

                        if gsp():
                            print("The operation was successfully completed")
                            score += 200
                            print("your zharzh: ", random_numbers(1000000000, 9999999999), "\n",
                                  "your score:", score)
                            break
                        else:
                            break
                    elif kharid:
                        print(kharid)
                    else:
                        break
                elif "3" in user_chois:
                    break
        elif "3" in user_chois:
            while True:

                shomenu(ghore_keshi_menu)
                user_chois = input("plese Enter your chois: ")
                if "1" in user_chois:
                    shomenu(select_menu)
                    user_chois = input("plese Enter your chois: ")
                    if "1" in user_chois:
                        if score < 200:
                            print("your score is not enough")
                        else:
                            user_chans = score // 200
                            score = 0
                            print("your chans is:", user_chans)
                            break
                    elif "2" in user_chois:
                        user_chans += 1
                        print("your chans is:", user_chans)
                        break
                    else:
                        print("Error in input data")
                elif "2" in user_chois:
                    print("""ghore keshi haf hashtad ba 6 jayeze mokhtalef dar entezar shomast
"har shans ezafe yek ghadam nazdik tar be bord list javayes: """)
                    shomenu(javayez)
                    break
                elif "3" in user_chois:
                    print("month's winners:")
                    shomenu(winners_month)
                elif "4" in user_chois:
                    break
        elif "4" in user_chois:
            while True:

                shomenu(internet_menu)
                user_chois = input("please Enter your chois: ")
                if "1" in user_chois:

                    kharid = information(Daily_internet, r"[1-3]")
                    if type(kharid) == dict:
                        shomenu(kharid)

                        if gsp():
                            print("The operation was successfully completed")
                            score += 200
                            print("your score:", score)
                            break
                        else:
                            break
                elif "2" in user_chois:

                    kharid = information(Monthly_internet, r"[1-3]")
                    if type(kharid) == dict:
                        shomenu(kharid)

                        if gsp():
                            print("The operation was successfully completed")
                            score += 200
                            print("your score:", score)
                            break
                        else:
                            break
                elif "3" in user_chois:

                    kharid = information(Three_month_internet, r"[1-3]")
                    if type(kharid) == dict:
                        shomenu(kharid)

                        if gsp():
                            print("The operation was successfully completed")
                            score += 200
                            print("your score:", score)
                            break
                        else:
                            break
                elif "4" in user_chois:
                    break
        elif "5" in user_chois:
            print("tanks for your visit")
            break
    else:
        print("Error in input data", "\n")
