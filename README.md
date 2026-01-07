# 🏪 Sistema Couto’s Conveniência

Sistema web para **catálogo digital de uma conveniência física**, desenvolvido com **Django + HTML/CSS**, focado na exibição de produtos, preços, promoções e categorias, **sem e-commerce, sem pagamento online e sem delivery**.

O sistema é acessado via **QR Code**, facilitando a decisão de compra do cliente dentro da loja e aumentando o ticket médio.

---

## 🎯 Contexto do projeto

A Couto’s Conveniência é um comércio físico que não possuía presença digital estruturada.

Problemas identificados:
- clientes perguntando preços repetidamente
- promoções pouco visíveis
- dificuldade em divulgar produtos e categorias
- dependência total do balcão para decisão de compra

Este projeto resolve isso com um **catálogo digital simples, rápido e acessível**, pensado para uso **no ambiente físico da loja**.

---

## 📌 Escopo do sistema

### ✅ O sistema É:
- Catálogo digital de produtos
- Exibição de preços
- Filtro por categorias
- Página de detalhe do produto
- Contador de cliques (interesse do cliente)
- Acesso via QR Code
- Importação automatizada de produtos
- Deploy em produção

### ❌ O sistema NÃO é:
- E-commerce
- Carrinho de compras
- Pagamento online
- Delivery
- Login de clientes

---

## 🧰 Tecnologias utilizadas

### Backend
- Python
- Django
- Django ORM
- Gunicorn

### Frontend
- HTML
- CSS
- Templates Django

### Infraestrutura
- Git (versionamento)
- Render (deploy)
- Banco de dados em produção
- Arquivos estáticos configurados corretamente

---

## ⚙️ Funcionalidades implementadas

### Frontend
- Layout completo das páginas:
  - Home
  - Produtos
  - Detalhe do produto
  - Promoções
  - Contato
- Identidade visual definida (preto + amarelo)
- Design responsivo (mobile, tablet e desktop)
- Grid de produtos organizado
- Botões de CTA funcionando (WhatsApp / detalhes)

### Backend
- Models organizados:
  - Produto
  - Categoria
- Campo de imagem com `ImageField(upload_to="produtos/")`
- Views limpas e organizadas
- Filtro de produtos por categoria
- Página de detalhe funcional
- Contador de cliques com `F('cliques') + 1`
- Rotas padrão do Django funcionando corretamente

---

## 🧪 Qualidade e confiabilidade

- Testes automatizados implementados
- Testes corrigidos e 100% passando
- Lógica validada em ambiente de testes
- Código sem gambiarras ou dependências frágeis

---

## 📦 Importação automatizada de dados

- Comando customizado para importação via CSV
- Cadastro de produtos sem uso do admin manual
- Pipeline preparado para escalar o catálogo

---

## 🧱 Decisão técnica importante — gestão de imagens

### Problema identificado
Upload manual de imagens não escala.

### Solução adotada
Importação automática de imagens via URL.

### Estratégia definida
- CSV contendo coluna `image_url`
- Comando de importação:
  - baixa a imagem automaticamente
  - salva no `ImageField`
  - associa corretamente ao produto
- Compatível com ambiente de produção (Render)
- Zero trabalho manual

### Fontes de imagens
- Unsplash
- Pexels
- Pixabay

---

## ▶️ Como rodar o projeto localmente

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências
4. Execute as migrações
5. Inicie o servidor Django

> ⚠️ Detalhamento dos comandos será expandido conforme necessário.

---

## 🚧 Status do projeto

🟢 **Funcional e em produção**

Infraestrutura, deploy, frontend base, backend e testes **já resolvidos**.

---

## 🔜 Próximo passo (ponto exato de retomada)

### 🥇 Automação definitiva de imagens

Objetivo:
- eliminar qualquer upload manual
- importar produtos com imagens automaticamente

Próximas ações:
- criar CSV com coluna `image_url`
- ajustar comando de importação para:
  - baixar a imagem
  - salvar no `ImageField`
  - associar corretamente ao produto

📍 **Para retomar o projeto no futuro, basta dizer:**

> “Vamos continuar pela automação de imagens via URL no comando de importação.”

A partir disso, o desenvolvimento segue **sem retrabalho**.

