import csv

def get_dim_family(row):
    marital=row[0]
    relationship=row[1]
    if relationship=="Not-in-family" and marital=="Never-married":
        return 1
    elif relationship=="Not-in-family" and marital=="Divorced":
        return 3
    elif relationship=="Not-in-family" and marital=="Married-spouse-absent":
        return 5
    elif relationship=="Not-in-family" and marital=="Widowed":
        return 18
    elif relationship=="Not-in-family" and marital=="Seperated":
        return 20
    elif relationship=="Not-in-family" and marital=="Married-civ-spouse":
        return 24
    elif relationship=="Husband" and marital=="Married-civ-spouse":
        return 2
    elif relationship=="Husband" and marital=="Married-AF-spouse":
        return 27
    elif relationship=="Other-relative" and marital=="Married-civ-spouse":
        return 14
    elif relationship=="Other-relative" and marital=="Never-married":
        return 15
    elif relationship=="Other-relative" and marital=="Seperated":
        return 17
    elif relationship=="Other-relative" and marital=="Divorced":
        return 21
    elif relationship=="Other-relative" and marital=="Married-spouse-absent":
        return 23
    elif relationship=="Other-relative" and marital=="Widowed":
        return 26
    elif relationship=="Other-relative" and marital=="Married-AF-spouse":
        return 29
    elif relationship=="Own-child" and marital=="Never-married":
        return 6
    elif relationship=="Own-child" and marital=="Divorced":
        return 10
    elif relationship=="Own-child" and marital=="Married-civ-spouse":
        return 11
    elif relationship=="Own-child" and marital=="Seperated":
        return 13
    elif relationship=="Own-child" and marital=="Married-spouse-absent":
        return 22
    elif relationship=="Own-child" and marital=="Widowed":
        return 25
    elif relationship=="Own-child" and marital=="Married-AF-spouse":
        return 28
    elif relationship=="Unmarried" and marital=="Never-married":
        return 7
    elif relationship=="Unmarried" and marital=="Divorced":
        return 8
    elif relationship=="Unmarried" and marital=="Seperated":
        return 9
    elif relationship=="Unmarried" and marital=="Widowed":
        return 16
    elif relationship=="Unmarried" and marital=="Married-spouse-absent":
        return 19
    elif relationship=="Wife" and marital=="Married-civ-spouse":
        return 4
    return 29

def main():
    train = open("train.csv", "r")
    output = open("associations2.csv", "w")

    read_train = csv.reader(train)
    write_output = csv.writer(output)
    write_output.writerow(["FamilyID"])
    print("Extracting data from train.csv")
    next(read_train) # Skip the header
    for row in read_train:
        familyID= get_dim_family(row)
        write_output.writerow([familyID])

    
if __name__ == '__main__':
    main()   
    
    
