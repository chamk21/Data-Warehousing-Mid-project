PRINT '';
PRINT '*** Dropping Database';
GO

IF EXISTS (SELECT [name] FROM [master].[sys].[databases] WHERE [name] = N'project1DW')
DROP DATABASE project1DW;
GO

CREATE database project1DW
GO

USE project1DW
GO

CREATE TABLE DimPersonal
(
PersonalID int primary key identity,
Race varchar(50),
Native_Country varchar(50),
Gender varchar(50)
)
GO

CREATE TABLE DimEducation
(
EducationID int primary key identity,
Education varchar(50)
)

CREATE TABLE DimEmployment
(
EmploymentID int primary key identity,
Workclass varchar(50),
Occupation varchar(50)
)

CREATE TABLE DimFamily
(
FamilyID int primary key identity,
Relationships varchar(50),
Marital_Status varchar(50)
)


CREATE TABLE DimIncome
(
IncomeID int primary key identity,
Income_Bracket varchar(50)
)
GO

CREATE TABLE FactIndividual
(
IndividualId bigint primary key identity,
IncomeID int not null,
PersonalID int not null,
FamilyID int not null,
EmploymentID int not null,
EducationID int not null,
Age int not null,
Hours_Worked int,
Capital_Gain money,
Capital_Loss money
)

ALTER TABLE FactIndividual ADD CONSTRAINT
FK_IncomeID FOREIGN KEY (IncomeID) REFERENCES DimIncome(IncomeID);


ALTER TABLE FactIndividual ADD CONSTRAINT
FK_PersonalID FOREIGN KEY (PersonalID) REFERENCES DimPersonal(PersonalID);

ALTER TABLE FactIndividual ADD CONSTRAINT
FK_FamilyID FOREIGN KEY (FamilyID) REFERENCES DimFamily(FamilyID);

ALTER TABLE FactIndividual ADD CONSTRAINT
FK_EmploymentID FOREIGN KEY (EmploymentID) REFERENCES DimEmployment(EmploymentID);

ALTER TABLE FactIndividual ADD CONSTRAINT
FK_EducationID FOREIGN KEY (EducationID) REFERENCES DimEducation(EducationID);
GO
