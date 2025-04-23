import requests
from urllib.parse import urljoin

def test_http_verb(base_url, path, verb, data=None):
    url = urljoin(base_url, path)
    try:
        print(f"\n=== TEST {verb} ===")
        kwargs = {
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded", "Cookie": "" }}
        if verb in ["POST", "PUT", "PATCH"] and data:
            kwargs["data"] = data

        response = requests.request(verb, url, **kwargs)

        print(f"Status Code: {response.status_code}")
        print("Headers:")
        
        for key, value in response.headers.items():
            if key.lower() != "set-cookie":
                print(f"- {key}: {value}")
        if "Set-Cookie" in response.headers:
            del response.headers["Set-Cookie"]

        if verb not in ["HEAD", "OPTIONS"] and response.text:
            print(f"Body (parziale): {response.text[:200]}...")
        return response.status_code, response.headers
    except requests.exceptions.RequestException as e:
        print(f"Errore durante {verb}: {e}")
        return None, None

if __name__ == "__main__":
    base_url = input("Inserisci l'URL base di phpMyAdmin (es. http://192.168.20.10/): ").strip()
    target_path = input("Inserisci il percorso da testare (es. /phpmyadmin/ o /phpmyadmin/index.php): ").strip()

    common_verbs = ["GET", "HEAD", "POST", "PUT", "DELETE", "PATCH"]
    test_data = {"pma_username": "test", "pma_password": "test"}  

    for verb in common_verbs:
        test_http_verb(
            base_url,
            target_path,
            verb,
            data=test_data if verb == "POST" else None
        )
