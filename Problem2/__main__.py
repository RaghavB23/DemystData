"""main function"""
from generate_csv import generate_csv
from anonymize_csv import anonymize_csv
from anonymize_csv_spark import anonymize_csv_spark

def main():
    input_file = "sample_data1.csv"
    anonymized_file = "anonymized_data.csv"
    spark_output_dir = "anonymized_data_spark"

    print("Step 1: Generating CSV...")
    generate_csv(input_file, num_rows=30_000_000)
    print(f"CSV file generated: {input_file}")

    print("Step 2: Anonymizing with Python...")
    anonymize_csv(input_file, anonymized_file)
    print(f"Anonymized CSV created: {anonymized_file}")

    print("Step 3: Anonymizing with Spark...")
    anonymize_csv_spark(input_file, spark_output_dir)
    print(f"Anonymized CSV created with Spark: {spark_output_dir}")

if __name__ == "__main__":
    main()

