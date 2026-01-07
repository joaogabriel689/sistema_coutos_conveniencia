import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from catalogo.models import Produto, Categoria

class Command(BaseCommand):
    help = "Importa produtos a partir de um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument("arquivo", type=str)

    def handle(self, *args, **kwargs):
        caminho = kwargs["arquivo"]

        with open(caminho, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                nome = row["nome"].strip()

                if Produto.objects.filter(nome=nome).exists():
                    self.stdout.write(f"⚠️ Produto já existe: {nome}")
                    continue

                categoria, _ = Categoria.objects.get_or_create(
                    nome=row["categoria"].strip()
                )

                Produto.objects.create(
                    nome=nome,
                    descricao=row.get("descricao", ""),
                    preco=Decimal(row["preco"]),
                    categoria=categoria,
                    ativo=row.get("ativo", "TRUE") == "TRUE",
                    promocao=row.get("promocao", "FALSE") == "TRUE",
                    destaque=row.get("destaque", "FALSE") == "TRUE",
                )

                self.stdout.write(f"✅ Importado: {nome}")

        self.stdout.write(self.style.SUCCESS("Importação finalizada"))