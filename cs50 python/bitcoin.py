import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
else:
    print("Missing command-line argument")
    sys.exit()

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    request = r.json()
    bit = request["bpi"]["USD"]["rate_float"]
    price = bit * value
    print(f"${price:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit()
