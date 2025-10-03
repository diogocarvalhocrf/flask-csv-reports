# 📊 Sistema de Relatórios Escolares

Este sistema foi desenvolvido para facilitar a coleta e organização dos **relatórios diários das unidades escolares** do município de Mesquita.  
A aplicação disponibiliza um **formulário online** para entrada de dados e permite a **exportação em CSV**, de forma que os resultados possam ser analisados em ferramentas externas (planilhas, dashboards, etc.).

---

## 🚀 Funcionalidades

- Formulário digital para preenchimento de dados das escolas
- Exportação automática de informações em **CSV**
- Possibilidade de uso dos arquivos gerados em planilhas e ferramentas de BI para construção de gráficos e análises
- Sistema de login para controle de acesso
- Interface simples e responsiva

---

## 🛠 Tecnologias utilizadas

- **Python (Flask)** para o backend
- **HTML + CSS + JavaScript** no frontend
- **Jinja2** para templates dinâmicos
- **CSV** como formato de exportação de dados

---

## 📂 Estrutura do Projeto

```plaintext
cco_web/
 ├─ app.py                  # Backend principal (Flask)
 ├─ static/
 │   ├─ form.js             # Scripts do formulário
 │   └─ style.css           # Estilos da aplicação
 └─ templates/
     ├─ form.html           # Página de formulário
     ├─ layout.html         # Template base
     └─ login.html          # Tela de login
