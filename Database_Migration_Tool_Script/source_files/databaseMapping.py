import os

def getDatabaseMapping(srcDatabaseType):
#{
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	databaseMappingPath = os.path.join(currentDirectory, "..")
	databaseMappingPath = os.path.join(databaseMappingPath, "database_specific_properties")
	databaseMappingPath = os.path.join(databaseMappingPath,srcDatabaseType.lower())
	databaseMappingPath = os.path.join(databaseMappingPath,"oracle-mssql.properties")
	
	filePtr=open(databaseMappingPath, "r")
	srcDatatypeList = []
	tgtDatatypeList = []
	
	for line in filePtr:
	#{
		tmpPosition = line.find("|")
		tmpFilepropertyPrefix = line[0:tmpPosition]
		tmpFilepropertyPrefix = tmpFilepropertyPrefix.lower()
		srcDatatype = tmpFilepropertyPrefix.lower()
		srcDatatypeList.append(srcDatatype)
		tgtDatatype = line[tmpPosition+1:len(line)].lower().strip().strip("\n")
		tgtDatatypeList.append(tgtDatatype)
	#}
	return srcDatatypeList, tgtDatatypeList
#}