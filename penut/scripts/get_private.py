def pri(b):
    # Import the required modules
    import mysql.connector
    import base64

    try:
        # Create a connection

        mydb = mysql.connector.connect(host="database-1.cbbbmqyvzgqg.us-east-2.rds.amazonaws.com", user="admin",
                                       password="EvDRgjT3imys6i3", database="tnstorage")

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
        image = data[0][0]

        # Decode the string
        binary_data = base64.b64decode(image)
        out = b[1:-1] + ".pem"
        file_out = open(out, "wb")
        file_out.write(binary_data)

    except Exception as e:
        return "Error retriving privatekey"