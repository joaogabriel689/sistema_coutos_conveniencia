import csv
import requests
from decimal import Decimal
from catalogo.models import Produto, Categoria

SHEETS_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1wZ2STzjkfYogCSFy4bIth9m4LQBTjPhkKWu13TFNo3k"
    "/export?format=csv"
)

def str_to_bool(value):
    return str(value).strip().upper() == "TRUE"


def run():
    print("🔄 Iniciando sincronização com Google Sheets...")

    response = requests.get(SHEETS_CSV_URL)
    response.raise_for_status()

    lines = response.content.decode("utf-8").splitlines()
    reader = csv.DictReader(lines)

    nomes_planilha = set()

    for row in reader:
        nome = row["nome"].strip()
        nomes_planilha.add(nome)

        try:
            preco = Decimal(row["preco"])
        except:
            print(f"❌ Preço inválido: {nome}")
            continue

        categoria, _ = Categoria.objects.get_or_create(
            nome=row["categoria"].strip()
        )

        produto, created = Produto.objects.update_or_create(
            nome=nome,
            defaults={
                "descricao": row.get("descricao", ""),
                "preco": preco,
                "categoria": categoria,
                "promocao": str_to_bool(row.get("promocao")),
                "destaque": str_to_bool(row.get("destaque")),
                "ativo": str_to_bool(row.get("status")),
            }
        )

        if created:
            print(f"🆕 Criado: {nome}")
        else:
            print(f"♻ Atualizado: {nome}")

    # 🔥 APAGA PRODUTOS QUE NÃO ESTÃO MAIS NA PLANILHA
    produtos_remover = Produto.objects.exclude(nome__in=nomes_planilha)

    removidos = produtos_remover.count()
    produtos_remover.delete()

    print(f"🗑 Removidos do banco: {removidos}")
    print("✅ Sincronização concluída com sucesso")