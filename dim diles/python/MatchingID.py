import csv
import os
##opening the fact table to write into and putting in the headers
def main():
    with open('fact.csv', 'w', newline='') as fact:
        fact_writer = csv.writer(fact, delimiter=',')
        fact_writer.writerow(["IndividualID", "PersonalID", "FamilyID", "EmploymentID", "EducationID", "Age", "Hours Worked", "Capital Gain", "Capital Loss"])
##opening of adult-training to read the data columns and grouping them
        with open('adult-training.csv', 'r') as training:
            training_writer = csv.reader(training, delimiter=',')
            IndividualID = 0
            for row in training_writer:
                IndividualID += 1
                
    ##          This is essentially fetching all the data in adult training
    ##          Im grouping each row into its catergories as in the dimension table 
                
    ##            Family
                family_row = [row[5].strip(), row[7].strip()]
                FamilyID = Family(family_row)
                
    ##            Employment
                employment_row = [row[1].strip(), row[6].strip()]
                EmploymentID = Employment(employment_row)
                
  
    ##          Personal
                personal_row = [row[13].strip(), row[8].strip(), row[9].strip()]
                PersonalID = Personal(personal_row)
                
                
    ##            Education
                education_row = [row[3].strip()]
                EducationID = Education(education_row)
 

                
    ##            Age
                age = row[0].strip()
    ##            Capital Gain
                cap_gain = row[10].strip()
    ##            Capital Loss
                cap_loss = row[11].strip()
    ##            Hours Worked
                hrs_wrkd = row[12].strip()                
                
                
                FactData = [IndividualID, PersonalID, FamilyID, EmploymentID, EducationID, age, hrs_wrkd, cap_gain, cap_loss]
               
                fact_writer.writerow(FactData)
            

def Family(family_row):
    with open('Family.csv', 'r') as family_file:
        family_writer = csv.reader(family_file, delimiter=',')
        id = 0
        for row in family_writer:
            id += 1
            Dimension_family_row = [row[1].strip(), row[2].strip()]
            if family_row == Dimension_family_row:
                return id

def Employment(employment_row):
    with open('Employed.csv', 'r') as employment_file:
        employment_writer = csv.reader(employment_file, delimiter=',')
        id = 0
        for row in employment_writer:
            id += 1
            Dimension_employed_row = [row[1].strip(), row[2].strip()]
            if employment_row == Dimension_employed_row:
                return id
         
def Personal(personal_row):
    with open('Personalinfo.csv', 'r') as personal_file:
        personal_writer = csv.reader(personal_file, delimiter=',')
        id = 0
        for row in personal_writer:
            id += 1
            Dimension_personal_row = [row[1].strip(), row[2].strip(),row[3].strip()]
            if personal_row == Dimension_personal_row:
                return id
                       
def Education(education_row):
    with open('Education.csv', 'r') as education_file:
        education_writer = csv.reader(education_file, delimiter=',')
        id = 0
        for row in education_writer:
            id += 1
            Dimension_education_row = [row[1].strip()]
            if education_row == Dimension_education_row:
                return id
                        


if __name__ == '__main__':
    main()   
