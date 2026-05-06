import argparse
import json
import urllib.request

def call_api():
    url = "http://localhost:3000/api/providers"

    req = urllib.request.Request(
        url,
        headers={"Content-Type": "application/json"},
        method="GET"
    )

    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

def main():
    result = call_api()
    print(result)

if __name__ == "__main__":
    main()
