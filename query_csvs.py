import duckdb

# Create a connection to an in-memory DuckDB database
con = duckdb.connect()

# Define queries to read each CSV file from the csv_files folder
queries = {
    'plant_info': "SELECT * FROM read_csv('csv_files/plant_info.csv')",
    'image_info': "SELECT * FROM read_csv('csv_files/image_info.csv')",
    'flight_info': "SELECT * FROM read_csv('csv_files/flight_info.csv')",
    'defects_info': "SELECT * FROM read_csv('csv_files/defects_info.csv')"
}

# Execute each query and fetch results as dictionaries
results = {}
for key, query in queries.items():
    results[key] = con.execute(query).fetchdf().to_dict('records')

# Print the output for each CSV file
for key, result in results.items():
    print(f"\nResults for {key}:")
    for row in result:
        print(row)


