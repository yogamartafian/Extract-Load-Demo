from google.cloud import bigquery
import os
import json

def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, rows_to_insert)
    if errors:
        print('Encountered errors while inserting rows: {}'.format(errors))
    else:
        print('Successfully insert data')

project_id = os.getenv('datawarehouse-04')
table_id = 'datawarehouse-04.my_dataset.task1'
rows_to_insert = [
    (1, "arter", 18, "informatics engineering"),
    (2, "yoga", 19, "data science"),
    (3, "arta", 21, "data analyst"),
    (4, "fian", 24, "game programming"),
    (5, "marta", 16, "software engineer"),
    (6, "ian", 14, "data engineer")
]

file_path = 'data.json'

with open(file_path, 'w') as json_file:
    json.dump(rows_to_insert, json_file, indent=2)

write_to_bigquery(table_id, rows_to_insert)