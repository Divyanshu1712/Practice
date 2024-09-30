import requests

# api fetch function to use
def fetch_api():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    resp = requests.get(url)
    data = resp.json()
    print(resp) # show success value of 200

    if data["success"] and "data" in data:
        new_data = data["data"]
        print(new_data) # this will show upthe whole data of josn file 
        last_name = new_data["name"]["last"]
        Age = new_data["dob"]["age"]
        email = new_data["email"]
        return last_name, Age, email
    else:
        raise Exception("Failed to fetch data wwith api")

# main driver code

def main():
    try:
        last_name, Age, email = fetch_api()
        print(f"Last name: {last_name},\n age: {Age},\n email: {email}")
    except Exception as e:
        print(str(e))

# Script Execution

if __name__ == "__main__":
    main()