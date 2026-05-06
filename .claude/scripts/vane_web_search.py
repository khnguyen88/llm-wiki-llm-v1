import argparse
import json
import urllib.request

def call_api(chat_model_provider_id, chat_model_key, embedding_model_provider_id, embedding_model_key, web_search_query):
    url = "http://localhost:3000/api/search"
    payload = {
        "chatModel": {
            "providerId": chat_model_provider_id,
            "key": chat_model_key
        },
        "embeddingModel": {
            "providerId": embedding_model_provider_id,
            "key": embedding_model_key
        },
        "optimizationMode": "quality",
        "sources": ["web"],
        "query": web_search_query,
        "history": [],
        "systemInstructions": "",
        "stream": False
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

def main():
    parser = argparse.ArgumentParser(description="Dependency-free HTTP caller")
    parser.add_argument("chat_model_provider_id", help="UUID of chat model provider"), 
    parser.add_argument("chat_model_key", help="Chat model key (e.g., gpt-4o-mini)")
    parser.add_argument("embedding_model_provider_id", help="UUID of embedding model provider")
    parser.add_argument("embedding_model_key", help="Embedding model key")
    parser.add_argument("web_search_query", help="Web search query to send to Vane")

    args = parser.parse_args()

    result = call_api(args.chat_model_provider_id, args.chat_model_key, args.embedding_model_provider_id, args.embedding_model_key, args.web_search_query)
    print(result)

if __name__ == "__main__":
    main()