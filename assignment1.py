import json
import os


def add_profile():
    name = input("Enter your name:")
    profession = input("Enter your profession:")
    contact = input("Enter your contact details:")
    skills = input("Enter your skills:")
    about_me_ = input("Give a bio about yourself:")
    passion = input("Enter your passion:")

    if os.path.getsize('user_details.json') == 0:
        if os.path.getsize('user_credentials.json') == 0:
            user_details = dict()
            user_credentials = dict()
            email = input("Enter you email:")
            password = input("Enter your password:")
            print("Your password is ", password)
            user_details[email] = {'name': name, 'profession': profession, 'contact': contact, 'skills': skills,
                                   'about_me_': about_me_, 'passion': passion}
            user_credentials[email] = {'password': password}
            with open('user_details.json', 'w') as my_file:
                json.dump(user_details, my_file)
                my_file.write("\n")
            with open('user_credentials.json', 'w') as my_file:
                json.dump(user_credentials, my_file)
                my_file.write("\n")
    else:
        with open('user_details.json') as json_file:
            user_details = json.load(json_file)
        with open('user_credentials.json') as json_file:
            user_credentials = json.load(json_file)
        check_mail = input("Enter your email:")
        password = input("Enter your password:")
        if check_mail in user_details.keys():
            print("Email already present enter again")
        else:
            email = check_mail
            user_details[email] = {'name': name, 'profession': profession, 'contact': contact, 'skills': skills,
                                   'about_me_': about_me_, 'passion': passion}
            user_credentials[email] = {'password': password}

        with open('user_details.json', 'w') as my_file:
            json.dump(user_details, my_file)
            my_file.write("\n")
        with open('user_credentials.json', 'w') as my_file:
            json.dump(user_credentials, my_file)
            my_file.write("\n")


def edit_profile():
    with open('user_details.json') as json_file:
        user_details = json.load(json_file)
    with open('user_credentials.json') as json_file:
        user_credentials = json.load(json_file)
    verify_mail = input("Enter your email")
    if verify_mail in user_details.keys():
        verify_password = input("Enter your password")
        if user_credentials[verify_mail]['password'] == verify_password:
            details = input("Enter the user details to be edited")
            new_info = input("Enter the new data")
            user_details[verify_mail][details] = new_info
            with open('user_details.json', 'w') as my_file:
                json.dump(user_details, my_file)
        else:
            print("Enter the correct password")
    else:
        print("Enter the correct email id")


def delete_profile():
    with open('user_details.json') as json_file:
        user_details = json.load(json_file)
    with open('user_credentials.json') as json_file:
        user_credentials = json.load(json_file)
    verify_mail = input("Enter your email:")
    if verify_mail in user_details.keys():
        verify_password = input("Enter your password:")
        if user_credentials[verify_mail]['password'] == verify_password:
            choice = int(input("1. Delete profile/n 2.Delete an entry"))
            if choice == 1:
                del user_credentials[verify_mail]
                del user_details[verify_mail]
                with open('user_details.json', 'w') as my_file:
                    json.dump(user_details, my_file)
                with open('user_credentials.json.json', 'w') as my_file:
                    json.dump(user_credentials, my_file)
            elif choice == 2:
                entry = input("Enter the detail to be deleted:")
                del user_details[verify_mail][entry]
                with open('user_details.json', 'w') as my_file:
                    json.dump(user_details, my_file)
            else:
                print("Invalid choice")
        else:
            print("Enter correct password")
    else:
        print("Enter correct email id")


def find_profile():
    with open('user_details.json') as json_file:
        user_details = json.load(json_file)
    with open('user_credentials.json') as json_file:
        user_credentials = json.load(json_file)
    verify_mail = input("Enter your email:")
    if verify_mail in user_details.keys():
        verify_password = input("Enter your password:")
        if user_credentials[verify_mail]['password'] == verify_password:
            choice = int(input("1.Profile/n 2.One detail"))
            if choice == 1:
                detail = input("Enter any one detail to find your profile:")
                if detail in user_details[verify_mail].values():
                    print(user_details[verify_mail])
                else:
                    print("Invalid input")
            elif choice == 2:
                one_detail = input("Detail to find:")
                if one_detail in user_details[verify_mail].keys():
                    print(user_details[verify_mail][one_detail])
            else:
                print("Invalid choice")
        else:
            print("Enter correct password")
    else:
        print("Enter correct email id")


def show_all_profiles():
    print("Displaying all the profiles")
    with open('user_details.json') as file:
        for obj in file:
            print(obj)


def about_me():
    while True:
        print("1. Add Profile/n 2. Edit Profile/n 3. Delete Profile/n 4. Find Profile/n 5. Show all profiles/n 6.Exit:")
        selection = int(input("Please Select an option:"))
        if selection == 1:
            add_profile()
        elif selection == 2:
            edit_profile()
        elif selection == 3:
            delete_profile()
        elif selection == 4:
            find_profile()
        elif selection == 5:
            show_all_profiles()
        elif selection == 6:
            break
        else:
            print("Unknown Option Selected!")


if __name__ == '__main__':
    about_me()
