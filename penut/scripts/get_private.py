def pri(b):
    # Import the required modules
    import mysql.connector
    import base64
    from .Sec_key import mysqlauth



    try:
        # Create a connection

        mydb = mysqlauth()

        # Create a cursor object
        cursor = mydb.cursor()

        # Prepare the query
        b = '"' + b + '"'
        query = 'SELECT privatekey FROM penut_tokenstorage WHERE hash= '
        query = query + b

        # Execute the query to get the file
        cursor.execute(query)

        data = cursor.fetchall()

        # The returned data will be a list of list
        key_data = data[0][0]

        # Decode the string
        binary_data = base64.b64decode(key_data)
        return binary_data

    except Exception as e:
        return "Error retriving privatekey"

