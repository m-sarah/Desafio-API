import csv

# EXTRAÇÃO
usuarios = []
with open("usuarios.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        usuarios.append(row)

# TRANSFORMAÇÃO
mensagens = []
for usuario in usuarios:
    mensagem = (
        f"Olá, {usuario['nome']}! "
        f"Sua conta {usuario['conta']} possui ofertas exclusivas disponíveis."
    )
    mensagens.append(mensagem)

# CARREGAMENTO
with open("mensagens.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["mensagem"])
    for msg in mensagens:
        writer.writerow([msg])

print("ETL concluído com sucesso.")
