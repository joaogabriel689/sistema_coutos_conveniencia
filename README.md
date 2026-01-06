# 🏪 Sistema Coutos Conveniência

Sistema web para **catálogo digital de uma conveniência física**, focado na exibição de produtos, preços, promoções e combos, **sem e-commerce, sem pagamento online e sem delivery**.

O acesso ao catálogo é feito via **QR Code**, permitindo que o cliente visualize produtos e ofertas diretamente no celular, dentro da loja.

---

## 🎯 Contexto do projeto

A **Coutos Conveniência** é um comércio físico que não possuía presença digital.

Os principais problemas identificados foram:
- clientes perguntando preços repetidamente no balcão
- promoções com pouca visibilidade
- dificuldade em divulgar combos
- dependência total do atendimento para decisão de compra

Este sistema surge como uma **solução simples e objetiva**, focada em melhorar a experiência do cliente **no ambiente físico da loja**.

---

## 📌 Escopo do sistema

### ✅ O sistema É:
- Catálogo digital de produtos
- Lista de preços atualizada
- Promoções e combos
- Produtos em destaque
- Acesso via QR Code
- Painel administrativo (uso interno)

### ❌ O sistema NÃO é:
- E-commerce
- Carrinho de compras
- Pagamento online
- Delivery
- Login de clientes

---

## ⚙️ Funcionalidades

- Cadastro, edição e remoção de produtos
- Cadastro de categorias
- Marcação de produtos como:
  - promoção
  - destaque
  - parte de combo
- Alteração rápida de preços
- Sugestão de combos
- Painel administrativo do Django

---

## 🧰 Tecnologias utilizadas

### Backend
- Python
- Django
- Django ORM
- SQLite (ambiente de desenvolvimento)

### Frontend
- HTML
- CSS
- Templates Django

---

## 🧱 Estrutura geral do sistema

### Área pública
- Home
- Promoções
- Combos
- Produtos em destaque
- Lista de produtos
- Detalhe do produto
- Onde estamos (mapa, horário e contato)

### Área administrativa
- Gerenciamento de produtos
- Gerenciamento de categorias
- Controle de promoções e destaques
- Acesso restrito via admin do Django

---

## ▶️ Como rodar o projeto localmente

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências
4. Execute as migrações
5. Inicie o servidor Django

> ⚠️ Comandos detalhados serão adicionados conforme o projeto evolui.

---

## 🚧 Status do projeto

🟡 **Em desenvolvimento**

- Documentação inicial concluída
- Estrutura base do Django criada
- Modelos em evolução
- Frontend em construção

---

## 📈 Objetivo do projeto

- Criar um **case real de aplicação web**
- Melhorar a experiência do cliente na loja física
- Facilitar a divulgação de produtos e promoções
- Desenvolver um sistema reutilizável para outros comércios locais

---

## 🔜 Próximos passos

- Finalizar modelagem dos produtos e categorias
- Criar views públicas do catálogo
- Estilizar páginas com CSS
- Implementar combos e promoções
- Gerar QR Code de acesso ao sistema
