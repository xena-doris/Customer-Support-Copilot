import json


def safe_parse(text):
    try:
        return json.loads(text)
    except:
        return {
            "action": "SearchKB",
            "arguments": {
                "query": extract_query(text)
            }
        }


def extract_query(text):
    # Try to extract clean query from model output
    if "User Query:" in text:
        return text.split("User Query:")[-1].strip()

    # fallback: last line
    lines = text.strip().split("\n")
    return lines[-1]