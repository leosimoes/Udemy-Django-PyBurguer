# Aulas de Django 4 e Bootstrap 5 em 120 minutos da Udemy

## Seção 1 - O que faremos durante o curso? Como o conteúdo será apresentado?

### 1. Apresentação do projeto e metodologia
O projeto é criar um site de hamburgueria usando Django 4 e Bootstrap 5.


## Seção 2 - Fundamentos de projetos e aplicações Django

### 2. Principais características do Django Framework
O Django é utilizado pela NASA, Youtube, Spotify, Mozila, Instagram, Pinterest, National Geographic, Open Stack e Globo.com.

Algumas características do Django são: Agilidade, base no princípio DRY, Reusabilidade (Fully loaded), 
Segurança (trata ataques como SQL injection, cross-site scripting, cross-site request forgery and clickjacking), 
Versatilidade.

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
Na pasta "templates", criar uma subpasta "burguer".

Usar um arquivo html como base para os outros templates. 
A base conterá a maior parte do código html e alguns blocos, como título e conteúdo, que serão modificados pelos outros
templates que o extenderem.

Para usar os htmls criados deve-se indicá-los em funções de views.py.


## Seção 4 - Fundamentos do Djando Admin, CRUD e arquivos estáticos

### 6. Djando Admin, Migrations, Criação de superuser, CRUD Djando Admin
Criar os primeiros models, que contém campos e comportamentos essenciais. 
O arquivo referente a models é models.py que está burguer.

Em models.py, criar a classe Produto. 

Depois de criar algum model, deve-se executar os comandos `python manage.py makemigrations` ("é semelhante com git add"),
`python manage.py migrate`, `python manage.py createsuperuser`.

Em burguer>admin.py registramos os models.

### 7. Trabalhando com arquivos estáticos (Imagens, CSS e JavaScript)

Para adicionar imagens, altere a classe produto, execute os comandos `python manage.py makemigrations` 
e `python manage.py migrate`, e faça configurações adicionais. 

Em templates>burguer, criar produto.html. 

Em pyburguer>settings.py, defina STATIC_ROOT, MEDIA_URL e MEDIA_ROOT.

Em burguer>urls.py, adicionar o path de produto e dos arquivos estáticos.


## Seção 5 - Layout e Bootstrap

### 8. Navbar - Part I
A navbar vai ser escrita em um novo arquivo e será reutilizada por outros arquivos html.
O código de navbar do Bootstrap é copiado do exemplo e depois alterado.

Criar pasta fragments dentro da templates>burguer.

Em templates>burguer>fragments, criar navbar.html e colar um dos exemplos de
https://getbootstrap.com/docs/5.1/components/navbar/

Editar base.html para adicionar div com bootstrap, navbar entre tags headers, e conteúdo entre tags main.

Editar home.html 

Editar navbar.html, alterando o nome de titulo, remover dropdown menu e elemento disable, 
adicionar a classe "ms-auto" para `<ul>` para alinhar elementos ao centro. 

### 9. Navbar - Part II

Adicionar 2 novos botões no navbar.

Usar font awesome:
https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css

Em base.html, mudar a tag de header para nav, e colocar o nome do bloco de navbar também em home.html.

Em burguer>fragments, criar o arquivo banner.html.

Incluir bloco banner em base.html e home.html.

Em burguer, criar diretorio static/burguer.

Em burguer>static>burguer, adicionar o arquivo de imagem `burguer_slide.png`.

Em burguer>urls.py, substituir MEDIA_URL por STATIC_URL e MEDIA_ROOT por STATIC_ROOT.

### 10. Banner + carregamento de imagens (Arquivos estáticos)
Crie um arquivo banner.html.

A página home deve utilizar mais de um arquivo html que devem ser linkados e organizados corretamente.

Os arquivos html devem ser ajustados para suportar as funcionalidades desejadas.

### 11. Cards e Grid cards
Alterar as funções das views, rotas e htmls para que os produtos possam ser utilizados dinamicamente.

Verificar usos de MEDIA_URL, STATIC_URL, MEDIA_ROOT e STATIC_ROOT de settings.py.


## Seção 6 - QuerySet API e Recuperação de informações a partir do Banco de Dados

### 12. Django Shell e manipulações básicas de objetos e QuerySet API
Para adicionar novos produtos, usaremos o Django Shell ao invés do Django Admin.

No terminal, execute `pip install iPython`, `python manage.py shell`, e depois `python manage.py shell` para abir o shell.
No shell, adicione algum hamburguer:
`

    from burguer.models import Produto
    
    produto = Produto()
    
    produto.descricao = 'Artesanal'
    
    produto.preco = 19.99
    
    produto.imagem = ''
    
    produto.save()
    
    produtos = Produto.objects.all()

    produtos
`

### 13. Objetos de Contexto + Carregamento de informações a partir do Banco de Dados
Na classe Produto, adicione o campo `nome` e adicione um valor para nome de cada produto e altere os valores de descrição. 
Nos arquivos de templates, corrija as referências destes campos.

Para referenciar preço corretamente use `R${{ produto.preco | floatformat:2 }}` e altere o idioma para "pt-br" em
settings.py e base.html.


## Seção 7 - Fundamentos da navegação entre páginas

### 14. Deep Link e sistemas de rotas e passagens de parâmetros

### 15. Template para detalhamento do produto
Criar (se não tiver feito) produto.html sem banner, 
em burguer>urls.py criar uma função para tratar da rota, em burguer>views.py criar função `detalhe_produto()`, 
em conteudo.html colocar link `<a href="{% url 'produto' produto.id %}">`.

### 16. Link para a página inicial
Em navbar.html, adicionar link para home com `<a href="{% url 'home' %}">PyBurguer</a>`.


## Seção 8 - Carregamento de imagens armazenadas no Banco de Dados

### 17. Recuperando imagens cadastrados via processo de upload (MEDIA_URL e MEDIA_ROOT)
Usar MEDIAR_URL e MEDIA_ROOT, ao invés de STATIC_URL e STATIC_ROOT, para acessar imagens da base dados provenientes de upload.
STATIC_URL e STATIC_ROOT devem ser usadas quando carregar alguma imagem que não seja por upload dinâmico.

Em conteúdo.html e produto.html use `<img src="{{ produto.imagem.url }}" alt="hamburguer"/>` para carregar as imagens 
do banco de dados.

### 18. Download do código-fonte
https://github.com/academiapython/pyburguer