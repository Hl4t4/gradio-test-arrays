def getMonthNumber (month:str):
    print(month)
    match month:
        case "Enero":
            return "01"
        case "Febrero":
            return "02"
        case "Marzo":
            return "03"
        case "Abril":
            return "04"
        case "Mayo":
            return "05"
        case "Junio":
            return "06"
        case "Julio":
            return "07"
        case "Agosto":
            return "08"
        case "Septiembre":
            return "09"
        case "Octubre":
            return "10"
        case "Noviembre":
            return "11"
        case "Diciembre":
            return "12"
        case _:
            return ""

year2025 = "Miércoles, 01 de Enero,Viernes, 18 de Abril,Sábado, 19 de Abril,Jueves, 01 de Mayo,Miércoles, 21 de Mayo,Viernes, 20 de Junio,Domingo, 29 de Junio,Domingo, 29 de Junio,Miércoles, 16 de Julio,Viernes, 15 de Agosto,Jueves, 18 de Septiembre,Viernes, 19 de Septiembre,Domingo, 12 de Octubre,Viernes, 31 de Octubre,Sábado, 01 de Noviembre,Domingo, 16 de Noviembre,Lunes, 08 de Diciembre,Domingo, 14 de Diciembre,Jueves, 25 de Diciembre"
year2026 = "Jueves, 01 de Enero,Viernes, 3 de Abril,Sábado, 4 de Abril,Viernes, 01 de Mayo,Jueves, 21 de Mayo,Domingo, 21 de Junio,Lunes, 29 de Junio,Jueves, 16 de Julio,Sábado, 15 de Agosto,Viernes, 18 de Septiembre,Sábado, 19 de Septiembre,Lunes, 12 de Octubre,Sábado, 31 de Octubre,Domingo, 01 de Noviembre,Martes, 08 de Diciembre,Viernes, 25 de Diciembre"

splitted_year2025 = year2025.split(',')
splitted_year2025 = splitted_year2025[1::2]

splitted_year2026 = year2026.split(',')
splitted_year2026 = splitted_year2026[1::2]

formatted2025 = [{"fecha" : "2025-"+getMonthNumber(date[7:])+"-"+date[1:3]} for date in splitted_year2025]
formatted2026 = [{"fecha" : "2026-"+getMonthNumber(date[7:])+"-"+date[1:3]} for date in splitted_year2026]

print(formatted2025)
print(formatted2026)



