def qrpic(b):
    # Import the required modules
    from scripts.Sec_key import mysql

    # Create a connection
    mydb = mysql

    # Create a cursor object
    cursor = mydb.cursor()

    # Prepare the query
    query = 'SELECT QR FROM penut_tokenstorage WHERE id_number= '
    query = query + b

    # Execute the query to get the file
    cursor.execute(query)

    data = cursor.fetchall()

    # The returned data will be a list of list
    image = data[0][0]
    return image


