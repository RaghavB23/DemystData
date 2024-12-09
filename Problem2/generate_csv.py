"""generate csv file using faker"""
import csv
import random
from faker import Faker

def generate_csv(file_name, num_rows):
    """
    Generate a CSV file with random data for first_name, last_name, address, and date_of_birth.
    """
    fake = Faker()
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace('\n', ', '),
                'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
            })

if __name__ == "__main__":
    # Generate a 2GB CSV file (~10 million rows)
    generate_csv("sample_data1.csv", num_rows=30_000_000)
    print("CSV file generated: sample_data1.csv")
