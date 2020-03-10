# LMS Simples

Um simples exemplo de LMS para as aulas gravadas de EaD de TecWeb.

## Como seguir o conteúdo

O conteúdo desse repositório está separado em várias *branches* de desenvolvimento, cada qual com a sua função. 

Para cada aula temos uma *branch* com o material utilizado para a video aula correspondente. Para acompanhar a aula, você deve estar na mesma *branch* da aula, para vero resultado da aula, basta pegar a *branch* seguinte.

As *branches* de aula referentes ao conteúdo de **frontend** são:

 * Aula02-HTML5: Conteúdo textual para a construção da primeira página em HTML5
 * Aula03-FormsHTML5: Construção do primeiro formulários em HTML5.
 * Aula04-IntroCSS3: Formatação das primeiras páginas com CSS3.
 * Aula05-LayoutsCSS3: Construção do primeiro laout com CSS3.
 * Aula06-IntroJS: Utilização do JavaScript para páginas dinâmicas.

As *branches* sobre o conteúdo de **backend** são:

 * Aula07-DjangoIntro: Preparação para a criação do projeto Django.
 * Aula08-DjangoTemplates: Construção dos templates de **Server Side Rendering**.
 * Aula09-DjangoURLs: Utilização do sistema de rotas do Django.
 * Aula10-DjangoORM: Manipulação do banco de dados com o Django ORM.
 * Aula11-DjangoAuth: Construção do sistema de autenticação e autorização do Django.
 * Aula12-AJAX: Construção de paǵians dinâmicas com Ajax e Django.

## Como visualizar o resultado

Existem duas formas de visualização do resultado do projeto, o resultado do projeto com o conteúdo só do **frontend** e o resultado do projeto com o **frontend** e **backend**.

Para ver o resultado e navegar do projeto com apenas o conteúdo **frontend** entre no link XXX. Para ver o resultado e navegar no projeto com o **frontend** e **backend** veja o link XXX.

## Como executar o projeto localmente

Caso queira testar localmente o projeto, você deve ter instalado no seu computador:

 * Python 3.x (recomenda-se algo acima da 3.6)
 * Virtualenv (instale usando o pip install virtualenv)
 * git 2.x (o mais novo)

Configure o ambiente virtual usando o comando (no Linux/Mac):

```shell
virtualenv venv --python=python3
```

Ou no Windows:

```shell
virtualenv venv
```

Ative o ambiente virtual (no Linux/Mac):

```shell
source venv/bin/activate
```

Ou no Windows:

```shell
venv\Scripts\activate
```

Dentro do ambiente virtual, devemos instalar todas as dependências do projeto:

```shell
pip install -r requirements.txt
```

Com tudo instalado, devemos preparar o projeto, primerio fazendo as migrações necessárias:

```shell
python manage.py migrate
```

E depois criando o super usuário do Django

```shell
python manage.py createsuperuser
```

Depois disso, basta rodar o servidor local para começar a usar o projeto:

```shell
python manage.py runserver
```