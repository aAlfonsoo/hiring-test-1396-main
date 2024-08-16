import requests

API_KEY = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"
CLIENT_ID = 100
BASE_URL = "https://api.recruitment.shq.nz"


def get_domains(client_id, api_key):
    url = f"{BASE_URL}/domains/{client_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch domains: {response.status_code}")
        return None


def get_dns_records(zone_id, api_key):
    url = f"{BASE_URL}/zones/{zone_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch DNS records: {response.status_code}")
        return None


def main():
    domains = get_domains(CLIENT_ID, API_KEY)
    if not domains:
        return

    for domain in domains:
        print(f"\nDomain Name: {domain['name']}")
        print("=" * (8 + len(domain['name'])))

        for zone in domain['zones']:
            print(f"  Zone: {zone}")
            if 'id' in zone:
                dns_records = get_dns_records(zone['id'], API_KEY)
                if dns_records:
                    print("    DNS Records:")
                    for record in dns_records:
                        print(f"      - {record['type']} {record['name']} {record['content']}")


if __name__ == "__main__":
    main()
