import mysql.connector


def insert_data(company_list):
    connection = mysql.connector.connect(
        host="localhost",
        user='root',
        password='root',
        database='crawled_data',
        port=3306
    )

    cursor = connection.cursor()

    for json_data in company_list:
        company_name = json_data['company_name']
        company_id = json_data['company_id']
        company_owner = json_data['company_owner']
        company_address = json_data['company_address']

        # NHAP DATA VAO MYSQL
        insert_query = "INSERT INTO companies (company_name, company_id, company_owner, company_address) VALUES (%s, %s, %s, %s)"
        values = (company_name, company_id, company_owner, company_address)
        cursor.execute(insert_query, values)

    connection.commit()

    cursor.close()
    connection.close()
