# BLOSSOM-DATA-ENG
# Task descriptions

    1. Setup the working environment on your computer, which you'll use throughout the program.
    2. Understand S3 by completing this lab
    3. Write a python script with the following features; 
        a. Download the 7+ Million Dataset from S3 [bucket: blossom-data-engs key:-project1/free-7-million-company-dataset.zip].
        b. Read the file with pandas.
        c. Filter out companies without a domain name using pandas.
        d. Write out the output(from point c.) in the following formats 
            i. Parquet
            ii. JSON (compressed using gzip)
            iii. AVRO
        e. Upload the resulting 3 file to your S3 buckets blossom-data-eng-[student-name].

# Run the project:

python s3.py
