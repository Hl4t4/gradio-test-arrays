from datetime import datetime

def is_valid_date(date_string: str) -> bool:
    try:
        # Attempt to parse the string to a date with the format 'YYYY-MM-DD'
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def createSQLCalendarioCierre(data_in_rows: list, template: str) -> list:
    sql_query = []
    for row in data_in_rows:
        if is_valid_date(row[1]) and is_valid_date(row[2]) and is_valid_date(row[3]) and is_valid_date(row[4]) and row[5].isnumeric():
            values = {
                "FECHA_PAGO": row[1],
                "FECHA_CIERRE": row[2],
                "FECHA_APERTURA": row[3],
                "FECHA_INFORME": row[4],
                "MANDANTE_ID": row[5]
            }
            sql_query.append(template.format(**values))
    return sql_query

def queryToFile(sql_query: list, name: str) -> None:
    file_name = f"sql_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    with open(file_name, 'w') as file:
        for line in sql_query:
            file.write(line + "\n")

def makeQueryMandanteCalendario(data_in_rows: list) -> bool:
    insert_mandante_calendario_template = """INSERT INTO mandante_calendario SET
    fecha_pago = '{FECHA_PAGO}', 
    fecha_cierre= '{FECHA_CIERRE}',
    fecha_apertura = '{FECHA_APERTURA}',
    fecha_informe = '{FECHA_INFORME}',
    mandante_id = {MANDANTE_ID};"""
    name = "Mandante_Calendario"
    sql_query = createSQLCalendarioCierre(data_in_rows, insert_mandante_calendario_template)
    queryToFile(sql_query=sql_query, name=name)
    return True
