
import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


api_key = get_secret("api_key")
chat_id = get_secret("chat_id")
