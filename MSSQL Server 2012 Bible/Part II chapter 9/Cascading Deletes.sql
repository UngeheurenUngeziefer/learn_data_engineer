USE AdventureWorks2019

GO
ALTER TABLE [HumanResources].[JobCandidate]
DROP CONSTRAINT [FK_JobCandidate_Employee_BusinessEntityID]

GO
ALTER TABLE [HumanResources].[JobCandidate]
WITH CHECK ADD CONSTRAINT [FK_JobCandidate_Employee_BusinessEntityID]
FOREIGN KEY([BusinessEntityID])
REFERENCES [HumanResources].[Employee] ([BusinessEntityID])
ON DELETE CASCADE