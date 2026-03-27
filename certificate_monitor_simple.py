import json
from datetime import datetime, date

# Store certificates
certificates = []

# Check status
def get_status(expiry_date):
    today = date.today()
    days = (expiry_date - today).days

    if days < 0:
        return "EXPIRED"
    elif days <= 30:
        return "EXPIRING SOON"
    else:
        return "SAFE"

# Add certificate manually
def add_certificate():
    domain = input("Enter domain: ")
    issue = input("Enter issue date (YYYY-MM-DD): ")
    expiry = input("Enter expiry date (YYYY-MM-DD): ")

    try:
        datetime.strptime(issue, "%Y-%m-%d")
        datetime.strptime(expiry, "%Y-%m-%d")
    except:
        print("Invalid date format!")
        return

    certificates.append({
        "domain": domain,
        "issue_date": issue,
        "expiry_date": expiry
    })

    print("Certificate added successfully!")

# Load from JSON
def load_json():
    file = input("Enter JSON file name: ")

    try:
        with open(file, "r") as f:
            data = json.load(f)

        certificates.clear()
        for cert in data:
            certificates.append(cert)

        print("Certificates loaded successfully!")

    except:
        print("Error loading file!")

# View certificates
def view_certificates():
    if not certificates:
        print("No certificates found!")
        return

    for cert in certificates:
        print("\nDomain:", cert["domain"])
        print("Issue Date:", cert["issue_date"])
        print("Expiry Date:", cert["expiry_date"])

# Check status
def check_certificates():
    if not certificates:
        print("No certificates found!")
        return

    for cert in certificates:
        expiry_date = datetime.strptime(cert["expiry_date"], "%Y-%m-%d").date()
        status = get_status(expiry_date)

        print("\nDomain:", cert["domain"])
        print("Expiry Date:", cert["expiry_date"])
        print("Status:", status)

# Menu
def main():
    while True:
        print("\n--- Certificate Monitor ---")
        print("1. Add Certificate")
        print("2. Load from JSON")
        print("3. View Certificates")
        print("4. Check Status")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_certificate()
        elif choice == "2":
            load_json()
        elif choice == "3":
            view_certificates()
        elif choice == "4":
            check_certificates()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

# Run program
if __name__ == "__main__":
    main()