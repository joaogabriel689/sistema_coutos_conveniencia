import csv
import requests
from io import StringIO

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from catalogo.models import Produto, Categoria


SHEET_URL = "https://docs.google.com/spreadsheets/d/1wZ2STzjkfYogCSFy4bIth9m4LQBTjPhkKWu13TFNo3k/export?format=csv"


class Command(BaseCommand):
    help = "Sincroniza totalmente o banco de produtos a partir da planilha"

    def handle(self, *args, **options):
        self.stdout.write("🔄 Iniciando sincronização de produtos...")

        response = requests.get(SHEET_URL)
        response.raise_for_status()

        csv_file = StringIO(response.text)
        reader = csv.DictReader(csv_file)

        nomes_planilha = set()

        for row in reader:
            nome = row["nome"].strip()
            preco = row["preco"]
            categoria_nome = row["categoria"].strip()

            nomes_planilha.add(nome)

            # 🔹 Categoria
            categoria, _ = Categoria.objects.get_or_create(
                nome=categoria_nome
            )

            # 🔹 Produto (cria ou atualiza)
            produto, created = Produto.objects.update_or_create(
                nome=nome,
                defaults={
                    "preco": preco,
                    "categoria": categoria,
                }
            )

            # =============================
            # 📸 LÓGICA DE IMAGEM
            # =============================
            image_id = row.get("image_id")
            image_url = row.get("image_url")

            # 1️⃣ Google Drive (prioridade máxima)
            if image_id:
                image_url = (
                    "https://drive.google.com/uc"
                    f"?export=download&id={image_id}"
                )

            # 2️⃣ Unsplash automático (fallback)
            if not image_url:
                query = f"{produto.nome},{produto.categoria.nome}"
                image_url = (
                    f"https://source.unsplash.com/600x600/?{query}"
                )

            # 3️⃣ Download apenas se o produto não tiver imagem
            if image_url and not produto.imagem:
                img_response = requests.get(image_url)
                img_response.raise_for_status()

                file_name = (
                    produto.nome
                    .lower()
                    .replace(" ", "_")
                    .replace("/", "_")
                ) + ".jpg"

                produto.imagem.save(
                    file_name,
                    ContentFile(img_response.content),
                    save=True
                )

            self.stdout.write(
                self.style.SUCCESS(f"✔ Sincronizado: {produto.nome}")
            )

        # =============================
        # 🗑️ REMOÇÃO AUTOMÁTICA
        # =============================
        produtos_removidos = Produto.objects.exclude(
            nome__in=nomes_planilha
        )

        removidos = produtos_removidos.count()
        produtos_removidos.delete()

        self.stdout.write(
            self.style.WARNING(f"🗑️ Produtos removidos: {removidos}")
        )

        self.stdout.write(
            self.style.SUCCESS("✅ Sincronização completa finalizada")
        )