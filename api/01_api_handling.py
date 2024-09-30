import requests

def fetch_api():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    resp = requests.get(url)
    # print(resp) # show success value 200 
    data =resp.json()

    if data["success"] and "data" in data:
        new_data= data["data"]
        # print(data) # show whole data part form json
        last_name= new_data["name"]["last"]
        age = new_data["dob"]["age"]
        email = new_data["email"]
        return last_name, age, email
    else:
        raise Exception("failed to fetch data please check all the line and issue with it")




def main():
    try:
       last_name, age, email =fetch_api()
       print(f"Last name: {last_name},\nage : {age}\nemail: {email}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()