import requests

def fetch_random_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    fetch_data= requests.get(url)
    data = fetch_data.json()
    # print(data)
    if data["success"] and "data" in data:
        main_data= data["data"]
        selfLink = main_data.get("selfLink", "No selfLink available")
        volumeInfo = main_data["volumeInfo"]
        title = volumeInfo["title"]
        subtitle= volumeInfo["subtitle"]
        authors = volumeInfo["authors"]
        publisher= volumeInfo["publisher"]
        publishedDate= volumeInfo["publishedDate"]
        description= volumeInfo["description"]
        return title, subtitle, publisher, publishedDate, description, selfLink, authors 
    else:
        raise Exception("Unable to fetch data Try Again")

def main():
    try:
        title, subtitle, publisher, publishedDate, description, selfLink, authors = fetch_random_books()
        print(f"authors: {authors}\n title: {title}\n subtitle: {subtitle} \n publisher: {publisher} \n publishedDate: {publishedDate} \n description: {description} \n selfLink: {selfLink}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()