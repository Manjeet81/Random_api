import requests

def random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    responce = requests.get(url)
    extracted_data = responce.json()

    if extracted_data ["success"] and "data" in extracted_data:
        user_data = extracted_data["data"]
        username = user_data["login"]["username"]
        password = user_data["login"]["password"]
        return username, password
    else:
        raise Exception("data is unable to fetch Try angin")

def main():
    try:
        userdata,password = random_user()
        print(f"username: {userdata}\npassword: {password}")
        #print(f"password: {password}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()