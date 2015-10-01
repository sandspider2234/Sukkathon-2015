from parse_rest.user import User
from parse_rest.connection import register, SessionToken
from parse_rest.core import ResourceRequestBadRequest
from consts.keys import keys
from flask import Flask


def get_data():
    username = input("Username: ")
    password = input("Password: ")
    email = input("E-Mail: ")
    name = input("Full name: ")
    profession = input("Title/Profession: ")
    exp = int(input("Years of experience: "))
    return {"username": username, "password": password, "email": email, "name": name, "profession": profession,
            "exp": exp}


def sign_up():
    while True:
        try:
            sign_up_dict = get_data()
            current_user = User.signup(sign_up_dict["username"], sign_up_dict["password"], email=sign_up_dict["email"],
                                       Experience=sign_up_dict["exp"], Name=sign_up_dict["name"],
                                       Profession=sign_up_dict["profession"])
            break
        except ResourceRequestBadRequest:
            print("E-mail or username already exist")
        except ValueError:
            print("Invalid exp value")
    current_user = User.login(sign_up_dict["username"], sign_up_dict["password"])
    return current_user


def main():
    register(keys["application_key"], keys["rest_api_key"], master_key=keys["master_key"])
    new_user = sign_up()

if __name__ == "__main__":
    main()
