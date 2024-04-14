http_status = int(input("200 or 400 or 404 or 500 or 501 or 201: "))

# if http_status == 200 or http_status == 201:
#     print("Success")
# elif http_status == 400:
#     print("Bad request")
# elif http_status == 404:
#     print("Not Found")
# elif http_status == 500 or http_status == 501:
#     print("Server Error")
# else:
#     print("Unknown")

# WITH MATCH STATEMENT
match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")