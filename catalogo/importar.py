import csv
from decimal import Decimal
from catalogo.models import Produto, Categoria

def run():
    categoria_padrao, _ = Categoria.objects.get_or_create(nome="Geral")

    with open("produtos.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            nome = row["Nome"].strip()

            if Produto.objects.filter(nome=nome).exists():
                print(f"⚠️ Já existe: {nome}")
                continue

            try:
                preco = Decimal(row["Preco"])
            except:
                print(f"❌ Preço inválido: {nome}")
                continue

            categoria, _ = Categoria.objects.get_or_create(
                nome=row["categoria"].strip()
            )

            Produto.objects.create(
                nome=nome,
                descricao=row.get("descricao", ""),
                preco=preco,
                categoria=categoria,
                promocao=row["promocao"].upper() == "TRUE",
                ativo=row["ativo"].upper() == "TRUE",
                destaque=row["destaque"].upper() == "TRUE",
            )

    print("✅ Importação concluída")
