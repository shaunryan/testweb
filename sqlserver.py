import pyodbc
server = 'dataplatform-sql.database.windows.net'
database = 'DataEngineeringControl'
username = 'shaun.ryan@shaunchiburihotmail.onmicrosoft.com'
password = 'Fr44Ride01'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute(" select top 1 data_object_properties from metadata.generic_data_object")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()