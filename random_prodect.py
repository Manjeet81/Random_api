import requests

def fetch_the_random_prodect():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    fetched_data= requests.get(url)
    responce= fetched_data.json()

    if responce ["success"] and "data" in responce:
        prodect_data = responce["data"]
        prodect = prodect_data["brand"]
        category = prodect_data["category"]
        return prodect, category
    else:
        raise Exception("data is unbale to fetch Try again and check internet connection")

def main():
    try:
        prodect, catagory= fetch_the_random_prodect()
        print(f"prodect: {prodect} \n catagory: {catagory}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
else:
    print("faild")