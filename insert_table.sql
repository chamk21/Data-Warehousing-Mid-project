:setvar SqlSamplesSourceDataPath "C:\Users\kamal\Downloads\DataForInsert\"
:setvar DatabaseName "project1DW"
BULK INSERT [dbo].[DimPersonal] FROM '$(SqlSamplesSourceDataPath)Personalinfo.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);

BULK INSERT [dbo].[DimEducation] FROM '$(SqlSamplesSourceDataPath)Education.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);

BULK INSERT [dbo].[DimEmployment] FROM '$(SqlSamplesSourceDataPath)Employed.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);

BULK INSERT [dbo].[DimFamily] FROM '$(SqlSamplesSourceDataPath)Family.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);


BULK INSERT [dbo].[DimIncome] FROM '$(SqlSamplesSourceDataPath)Income.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);

BULK INSERT [dbo].[FactIndividual] FROM '$(SqlSamplesSourceDataPath)fact.csv'
WITH (
 CHECK_CONSTRAINTS,
 --CODEPAGE='ACP',
 DATAFILETYPE='char',
 FIELDTERMINATOR=',',
 ROWTERMINATOR='\n',
 --KEEPIDENTITY,
 TABLOCK
);