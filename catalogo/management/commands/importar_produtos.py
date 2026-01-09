import csv
import requests
from decimal import Decimal

from django.core.management.base import BaseCommand
from catalogo.models import Produto, Categoria, SubCategoria


SHEETS_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1wZ2STzjkfYogCSFy4bIth9m4LQBTjPhkKWu13TFNo3k"
    "/export?format=csv"
)


def str_to_bool(value):
    return str(value).strip().upper() == "TRUE"


class Command(BaseCommand):
    help = "Sincroniza produtos com Google Sheets (categorias e subcategorias)"

    def handle(self, *args, **options):
        self.stdout.write("🔄 Iniciando sincronização com Google Sheets...")

        response = requests.get(SHEETS_CSV_URL, timeout=30)
        response.raise_for_status()

        lines = response.content.decode("utf-8").splitlines()
        reader = csv.DictReader(lines)

        nomes_planilha = set()

        for row in reader:
            nome = row["nome"].strip()
            nomes_planilha.add(nome)

            # --- Preço ---
            try:
                preco = Decimal(row["preco"])
            except Exception:
                self.stderr.write(f"❌ Preço inválido: {nome}")
                continue

            # --- Categoria (obrigatória) ---
            nome_categoria = row["categoria"].strip()
            if not nome_categoria:
                self.stderr.write(f"❌ Produto sem categoria: {nome}")
                continue

            categoria, _ = Categoria.objects.get_or_create(
                nome=nome_categoria.upper()
            )

            # --- Subcategoria (opcional, dependente da categoria) ---
            subcategoria = None
            nome_subcategoria = row.get("subcategoria", "").strip()

            if nome_subcategoria:
                subcategoria, _ = SubCategoria.objects.get_or_create(
                    nome=nome_subcategoria.upper(),
                    categoria=categoria
                )

            # --- Produto ---
            produto, created = Produto.objects.update_or_create(
                nome=nome,
                defaults={
                    "descricao": row.get("descricao", "").strip(),
                    "preco": preco,
                    "categoria": categoria,
                    "subcategoria": subcategoria,
                    "imagem": row.get("imagem", "").strip() or None,
                    "promocao": str_to_bool(row.get("promocao")),
                    "destaque": str_to_bool(row.get("destaque")),
                    "ativo": str_to_bool(row.get("status")),
                }
            )

            if created:
                self.stdout.write(f"🆕 Criado: {nome}")
            else:
                self.stdout.write(f"♻ Atualizado: {nome}")

        # --- Remoção de produtos fora da planilha ---
        removidos = Produto.objects.exclude(nome__in=nomes_planilha)
        total = removidos.count()
        removidos.delete()

        self.stdout.write(f"🗑 Removidos: {total}")
        self.stdout.write("✅ Sincronização concluída")
