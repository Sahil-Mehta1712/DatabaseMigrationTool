import os

def getQuery(srcDatabaseType,property):
#{
	oldCurrentDirectory = os.path.dirname(os.path.realpath(__file__))
	currentWorkingDirectory = os.getcwd()
	
	if (oldCurrentDirectory != currentWorkingDirectory):
	#{
		raise SystemExit("Python Script invoked from wrong directory. Please change directory to where \"createJARFiles.py\" script is present.")
	#}
	
	currentDirectory = os.path.dirname(os.path.realpath(__file__))
	getQueryPath = os.path.join(currentDirectory, "..")
	getQueryPath = os.path.join(getQueryPath, "database_specific_properties")
	getQueryPath = os.path.join(getQueryPath,srcDatabaseType.lower())
	getQueryPath = os.path.join(getQueryPath,"oracle-query.properties")
	
	filePtr=open(getQueryPath, "r")
	
	propertyPrefix = srcDatabaseType.lower() + "." + property.lower()
	
	for line in filePtr:
	#{
		tmpPosition = line.find("=")
		tmpFilepropertyPrefix = line[0:tmpPosition]
		tmpFilepropertyPrefix = tmpFilepropertyPrefix.lower()
		
		if tmpFilepropertyPrefix == propertyPrefix:
		#{
			query = line[tmpPosition+1:len(line)].strip().strip("\n")
		#}
	#}
	return query
#}