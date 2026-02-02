import csv
while True:
    try:
        with open("notes/reading.txt", "r") as file:
                for line in file:
                    print(f"Hello {line.strip()}")
    except:
            print("That file can't be found")
    else:
        print("code ends")
        break


    try:
        with open("notes/sample.csv", mode = "r") as csv_file:
            content = csv.reader(csv_file)
            headers = line
            rows = []
            for line in content:
                 rows.append({headers[0]: line[0], headers[1]: line[1]})    
    except:
        print("Can't find the CSV")
    else:
        for lines in rows:
            print(rows)