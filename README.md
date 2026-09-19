# Sistema de Gestão de Biblioteca (CLI)

> Projeto acadêmico desenvolvido em **Python** com foco forte em **Programação Orientada a Objetos (POO)** e arquitetura de software limpa, executado via terminal (CLI).

---

## 📌 Sobre o Projeto
Este sistema simula o gerenciamento completo de uma biblioteca, controlando o acervo de livros, cadastro de usuários, controle de empréstimos e devoluções. O principal objetivo é aplicar os pilares da POO de forma prática, criando uma base sólida de regras de negócio que posteriormente será migrada para um ecossistema corporativo em **Java (Spring Boot / APIs REST)**.

---

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Interface:** Linha de Comando (Terminal / CLI)
* **Controle de Versão:** Git & GitHub

---

## 🧱 Conceitos de POO Aplicados
* **Encapsulamento:** Proteção de dados sensíveis (como status de empréstimo e histórico de usuários) utilizando atributos privados.
* **Herança:** Hierarquia de classes para diferentes tipos de usuários ou itens do acervo.
* **Polimorfismo:** Sobrescrita de métodos para regras específicas de devolução e multas.
* **Abstração:** Modelagem de entidades do mundo real em classes coesas.

---

## ⚙️ Funcionalidades
* **Gestão de Acervo:** Cadastro, consulta e atualização de livros.
* **Gestão de Usuários:** Cadastro de leitores e funcionários.
* **Módulo de Empréstimos:** Registro de empréstimos com validação de disponibilidade e prazos.
* **Devoluções e Multas:** Controle de devolução e cálculo automatizado de atrasos.
* **Relatórios Básicos:** Listagem de livros emprestados e histórico por usuário.

---

## 📦 Como Executar o Projeto

Clone o repositório e execute o arquivo principal diretamente pelo terminal:

```bash
# Clone o repositório
git clone [https://github.com/SEU-USUARIO/nome-do-repositorio.git](https://github.com/SEU-USUARIO/nome-do-repositorio.git)

# Entre na pasta do projeto
cd nome-do-repositorio

# Execute o sistema
python main.py