import tabula

tables = tabula.read_pdf("mpesa.pdf", pages="all", password="34915463")


print(tables)
