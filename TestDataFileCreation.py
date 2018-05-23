# Calls the Base Module methods and executes to Generate Test Data File

from Advance import Base

Base.displayWelcomeMessage()
n = Base.enterNumberOfRecords()
o = Base.selectGenerateOptions()
Base.generateData(n, o)
