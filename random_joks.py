import requests

def fetch_random_joks():
    url= "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    random_joks= requests.get(url)
    joks= random_joks.json()

    if joks ["success"] and "data" in joks:
        randam_joks=joks["data"]
        categories = randam_joks["categories"]
        jok = randam_joks["content"]
        return categories, jok
    else: 
        raise Exception("unable to fetch the data Try again")
    
def main():
    try:
        categories, joks =fetch_random_joks()
        print(f"categories: {categories} \n joks: {joks}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()