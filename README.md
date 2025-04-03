# Projeto Django com Python

Este projeto demonstra o uso do Django, um framework web de alto nível em Python, para criar aplicações web robustas e eficientes.

# Aluno

Nome: Diego Lohan da Motta Silva <br>
RGM: 27990231 <br>
Curso: Ciência da Computação <br>
8° semestre

## Visão Geral

O Django é conhecido por sua filosofia "baterias incluídas", fornecendo todas as ferramentas necessárias para o desenvolvimento web, desde o mapeamento objeto-relacional (ORM) até um sistema de templates poderoso. Este projeto explora os principais recursos do Django, incluindo:

* **Modelos**: Definição de estruturas de dados usando classes Python.
* **Views**: Lógica de negócios para processar requisições e gerar respostas.
* **Templates**: Criação de interfaces de usuário dinâmicas com HTML e tags de template do Django.
* **Formulários**: Gerenciamento de entrada de dados do usuário com validação e segurança.
* **Sistema de Administração**: Interface automática para gerenciamento de dados do aplicativo.

## Pré-requisitos

Certifique-se de ter o seguinte instalado:

* **Python**: Versão 3.x
* **pip**: Gerenciador de pacotes Python
* **virtualenv** (opcional): Para isolar as dependências do projeto

## Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/diegolohan14/diego_django
    cd diego_django
    ```

2.  Crie um ambiente virtual (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Aplique as migrações:

    ```bash
    python manage.py migrate
    ```

5.  Crie um superusuário (opcional):

    ```bash
    python manage.py createsuperuser
    ```

6.  Execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    O aplicativo estará disponível em `http://127.0.0.1:8000/`.

```bash
python manage.py test
