with (open("file1.txt", mode='r') as file1):
    date1 = file1
    with open("file2.txt", mode='r') as file2:
        date2 = file2.read()

        print(date2)
