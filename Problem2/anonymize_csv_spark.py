"""anonymize using spack"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2

def anonymize_csv_spark(input_file, output_file):
    """
    Anonymize a CSV file using Apache Spark.
    """
    spark = SparkSession.builder \
        .appName("Anonymize CSV") \
        .getOrCreate()

    # Read the CSV file
    df = spark.read.csv(input_file, header=True)

    # Anonymize the data using SHA-256
    anonymized_df = df.withColumn("first_name", sha2("first_name", 256)) \
                      .withColumn("last_name", sha2("last_name", 256)) \
                      .withColumn("address", sha2("address", 256))

    # Write the anonymized data back to a CSV file
    anonymized_df.write.csv(output_file, header=True)
