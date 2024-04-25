from supportedDatabases import supportedDatabases
from getDatabaseConnectionDetail import *

def databaseConnector(srcDatabase,databaseIdentifier):
#{
	(databaseConnectionList) = getDatabaseConnectionDetail(srcDatabase,databaseIdentifier)
	
	if srcDatabase.lower() == "oracle":
	#{	
		import cx_Oracle
		
		hostName = databaseConnectionList[0]
		portNo = databaseConnectionList[1]
		serviceNameStr = databaseConnectionList[2]
		username = databaseConnectionList[3]
		passwordStr = databaseConnectionList[4]
		
		dsn_tns = cx_Oracle.makedsn(hostName,portNo,service_name=serviceNameStr)
		conn = cx_Oracle.connect(user=username, password=passwordStr, dsn=dsn_tns)
		return conn
	#}
	elif srcDatabase.lower() == "mssql":
	#{
		import pymssql
		
		hostName = databaseConnectionList[0]
		databaseName = databaseConnectionList[1]
		username = databaseConnectionList[2]
		passwordStr = databaseConnectionList[3]
		
		conn = pymssql.connect(hostName,username,passwordStr,databaseName)

		cursor = conn.cursor()
		return conn
	#}
#}'