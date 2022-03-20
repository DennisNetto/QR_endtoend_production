import mysql.connector


def conff(a):
    try:

        mydb = mysql.connector.connect(host="database-1.cbbbmqyvzgqg.us-east-2.rds.amazonaws.com", user="admin",
                                       password="EvDRgjT3imys6i3", database="tnstorage")

        mycurser = mydb.cursor()
        w = "select id_number, First_name, Last_name, DOB from penut_humanstorage where id_number = "
        p = w + a
        mycurser.execute(p)
        myresult = mycurser.fetchall()
        myresult = str(myresult)
        myresult = myresult.replace("[", "")
        myresult = myresult.replace("]", "")
        myresult = myresult.replace("'", "")
        myresult = myresult.replace(")", "")
        myresult = myresult.replace("(", "")
        myresult = myresult.replace("datetime.date", "")
        myresult = tuple(map(str, myresult.split(', ')))
        fname = str(myresult[1])
        lname = str(myresult[2])
        one = str(myresult[3])
        two = str(myresult[4])
        three = str(myresult[5])
        date = one + "-" + two + "-" + three
        if myresult[0] == a:
            return fname, lname, date

        else:
            return "id not found"

    except IndexError:
        return "unknown error-id_number probably not the right "
