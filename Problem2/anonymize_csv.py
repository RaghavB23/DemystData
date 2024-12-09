"""anonymize using python"""
import csv
import hashlib

def anonymize_csv(input_file, output_file, chunk_size=10000):
    """
    Anonymize a CSV file by hashing first_name, last_name, and address.
    Processes the file in chunks to handle large datasets.
    """
    def hash_value(value):
        """Hash a string value using SHA-256."""
        return hashlib.sha256(value.encode()).hexdigest()

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        chunk = []
        
        for row in reader:
            # Anonymize sensitive columns
            row['first_name'] = hash_value(row['first_name'])
            row['last_name'] = hash_value(row['last_name'])
            row['address'] = hash_value(row['address'])
            chunk.append(row)

            # Write in chunks
            if len(chunk) >= chunk_size:
                writer.writerows(chunk)
                chunk = []

        # Write remaining rows
        if chunk:
            writer.writerows(chunk)
