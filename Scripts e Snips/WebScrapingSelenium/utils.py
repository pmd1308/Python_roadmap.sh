import validators

def get_user_input():
    while True:
        url = input("Enter url: ")
        if validators.url(url):
            break
        else:
            print("Invalid url")

    tag_name = input("Enter tag name: ").strip()
    while not tag_name:
        print("Tag name cannot be empty. Please enter a valid tag name.")
        tag_name = input("Enter the tag name of the element you want to extract: ").strip()

    return url, tag_name

