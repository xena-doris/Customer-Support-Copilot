import json


def safe_parse(text):
    try:
        return json.loads(text)
    except:
        # 🔥 fallback: extract clean query manually
        return {
            "action": "SearchKB",
            "arguments": {
                "query": extract_query(text)
            }
        }


def extract_query(text):
    # Try to find actual user query inside messy output
    if "User Query:" in text:
        return text.split("User Query:")[-1].strip()

    # fallback: return last line
    return text.strip().split("\n")[-1]