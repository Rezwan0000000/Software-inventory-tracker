import wmi
import csv
from datetime import datetime

def get_installed_software():
    c = wmi.WMI()
    software_list = []

    for product in c.Win32_Product():
        name = product.Name or "N/A"
        version = product.Version or "N/A"
        vendor = product.Vendor or "N/A"
        install_date = product.InstallDate or "N/A"

        software_list.append({
            'Name': name,
            'Version': version,
            'Vendor': vendor,
            'InstallDate': install_date
        })

    return software_list

def export_to_csv(software_list, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Version', 'Vendor', 'InstallDate'])
        writer.writeheader()
        for software in software_list:
            writer.writerow(software)

if __name__ == "__main__":
    print("Scanning installed software...")
    software = get_installed_software()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"installed_software_{timestamp}.csv"
    export_to_csv(software, filename)
    print(f"Inventory exported to {filename}")
