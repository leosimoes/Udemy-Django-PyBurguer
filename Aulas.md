# Aulas de Django 4 e Bootstrap 5 em 120 minutos da Udemy

## Seção 1 - O que faremos durante o curso? Como o conteúdo será apresentado?

### 1. Apresentação do projeto e metodologia
O projeto é criar um site de hamburgueria usando Django 4 e Bootstrap 5.

## Seção 2 - Fundamentos de projetos e aplicações Django

### 2. Principais características do Django Framework
O Django é utilizado pela NASA, Youtube, Spotify, Mozila, Instagram, Pinterest, National Geographic, Open Stack e Globo.com.

Algumas características do Django são: Agilidade, base no princípio DRY, Reusabilidade (Fully loaded), Segurança (trata ataques como SQL injection, cross-site scripting, cross-site request forgery and clickjacking), Versatilidade.

Os principais componentes do Django estão dispostos em MVT(Model, View e Template). 
- Model engloba classes relacionados ao banco de dados e ORM.
- View é um componente que recebe uma requisição faz o processamento da lógica do código e devolve um conteúdo html 
envelopado, processando toda a lógica do negócio.
- Template é o código html propriamente dito. 

### 3. Criando o primeiro projeto Django
Criar o projeto de nome "pyburguer" no PyCharm. 
Diferentemente do que eu fiz, ele instalou o Django depois (`pip install django`), 
salvou os requisitos (`pip freeze > requirements.txt`), 
executou o comando para criar o projeto Django `django-admin startproject core .`
e então, para executar o projeto, executou `python manage.py runserver`.

Na pasta core (ou pyburguer), em settings.py há configurações da aplicações, como ativação do debug.

Na pasta core (ou pyburguer), em urls.py há as rotas da aplicação.

### 4. Primeira Aplicação Django 
Para criar aplicação, execute o comando `django-admin startapp burguer`.

Na pasta burguer, criar urls.py.

Copiar o conteúdo de core>urls.py para burguer>urls.py.

Em views.py criar uma função home.

O arquivo core>urls.py define o roteamento global da aplicação. 

Em core>urls.py, adicionar `path('', include('burguer.urls'))` 

Em burguer>urls.py remover `path('admin/', admin.site.urls)` e adicionar `path('', views.home, name='home')`.


## Seção 3 - Introdução aos templates HTML

### 5. Renderizando templates HTML. Templates reutilizáveis com o uso de Extends


## Seção 4 - Fundamentos do Djando Admin, CRUD e arquivos estáticos

### 6. Djando Admin, Migrations, Criação de superuser, CRUD Djando Admin


### 7. Trabalhando com arquivos estáticos (Imagens, CSS e JavaScript)


## Seção 5 - Layout e Bootstrap

### 8. Navbar - Part I

### 9. Navbar - Part II

### 10. Banner + carregamento de imagens (Arquivos estáticos)

### 11. Cards e Grid cards


## Seção 6 - QuerySet API e Recuperação de informações a partir do Banco de Dados

### 12. Django Shell e manipulações básicas de objetos e QuerySet API

### 13. Objetos de Contexto + Carregamento de informações a partir do Banco de Dados


## Seção 7 - Fundamentos da navegação entre páginas

### 14. Deep Link e sistemas de rotas e passagens de parâmetros

### 15. Template para detalhamento do produto

### 16. Link para a página inicial


## Seção 8 - Carregamento de imagens armazenadas no Banco de Dados

### 17. Recuperando imagens cadastrados via processo de upload (MEDIA_URL e MEDIA_ROOT)

### 18. Download do código-fonte