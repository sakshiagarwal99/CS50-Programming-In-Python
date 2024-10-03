import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price_in_usd = get_bitcoin_price()
    total = price_in_usd * n
    print(f"${total:,.4f}")


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching bitcoin price")

    json_response =  response.json()
    price_in_usd = json_response['bpi']['USD']['rate_float']
    return price_in_usd

if __name__ == "__main__":
    main()
