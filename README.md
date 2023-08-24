# Django - PyBurguer

## Passos

### Seção 1:
1. Criar projeto Django no PyCharm com nome "burguer":

![PyCharm-Django-Starter](/printscreens/PyCharm-Django-Starter-PyBurguer.png)

### Seção 2:
2. Na pasta burguer, criar urls.py. 
3. Copiar o conteúdo de core>urls.py para burguer>urls.py.
4. Em views.py criar uma função home.
5. Em burguer>urls.py remover `path('admin/', admin.site.urls)` e adicionar `path('', views.home, name='home')`.
6. Em pyburguer>urls.py, adicionar `path('', include('burguer.urls'))` e burguer>urls.py.
7. Em pyburguer>settings.py verificar se a aplicação 'burguer' está em INSTALLED_APPS.

### Seção 3:
8. Na pasta "templates", criar uma subpasta "burguer".
9. Em templates>burguer, criar base.html que serivrá extendido pelos demais templates.
10. Em templates>burguer, criar home.html que extende base.html.
11. Em views.py, alterar função home para usar o home.html.

### Seção 4:
12. Em burguer>settings.py verifique as configurações do banco de dados no dicionário DATABASES.
13. Em models.py, criar a classe Produto.
14. Executar o comando `python manage.py makemigrations`.
15. Executar o comando `python manage.py migrate`.
16. Executar o comando `python manage.py createsuperuser` e configurar login e password.

![Terminal-SuperUser](/printscreens/Terminal-Create-super-user.png)
17. (Opcional) Configurar o runserver
18. python manage.py createsuperuser
19. Em burguer>admin.py, registre a model Produto com `admin.site.register(Produto)`.
20. Acesse '/admin/' do localhost com as credeciais criadas para o superuser para verificar a implementação.

![Django-admin](/printscreens/Django-admin-V1.png)
21. Adicione o campo de imagem na classe Produto.
22. Em pyburguer>settings.py, defina STATIC_ROOT, MEDIA_URL e MEDIA_ROOT.
23. Em templates>burguer, criar produto.html.
24. Em burguer>urls.py, adicionar o path de produto e dos arquivos estáticos.
25. Executar os comandos `python manage.py makemigrations` e `python manage.py migrate`.

![Terminal-Migration-0002](/printscreens/Terminal-Migration-0002.png)

### Seção 5:
26. Criar pasta fragments dentro da templates>burguer.
27. Em templates>burguer>fragments, criar navbar.html e colar um dos exemplos de
https://getbootstrap.com/docs/5.1/components/navbar/
28. Editar base.html para adicionar div com bootstrap, navbar entre tags headers, e conteúdo entre tags main.
29. Editar home.html. 
30. Editar navbar.html, alterando o nome de titulo, remover dropdown menu e elemento disable.
31. Editar navbar.html, adicionar a classe "ms-auto" para `<ul>` para alinhar elementos ao centro.
32. Editar navbar.html, adicionar botão de login, botão de cadastre-se.
33. Em base.html, linkar font awesome para adicionar imagens.
34. Em base.html, mudar a tag de header para nav, e colocar o nome do bloco de navbar também em home.html.
35. Em burguer>fragments, criar o arquivo banner.html.
36. Incluir bloco banner em base.html e home.html.
37. Em burguer, criar diretorio static/burguer.
38. Em burguer>static>burguer, adicionar o arquivo de imagem `burguer_slide.png`.
39. Em burguer>urls.py, substituir MEDIA_URL por STATIC_URL e MEDIA_ROOT por STATIC_ROOT.
40. Em burguer>fragments, criar o arquivo conteudo.html.
41. Incluir bloco conteudo em base.html e home.html.
42. Em views, alterar função home.
43. Fazer outras modificações para fazer tudo funcionar (foram mostradas nas seções seguintes).

![Site-Home-V1](/printscreens/Site-Home-V1.png)

### Seção 6:
44. (Opcional) No terminal, execute `pip install iPython` e `python manage.py shell`.
45. (Opcional) No terminal, execute `python manage.py shell` para abir o shell.
46. (Opcional) No shell, adicione algum hamburguer:

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

47. Em models.py, adicione o campo nome para a classe Produto, e use-o em `__str__()`.
48. Executar os comandos `python manage.py makemigrations` e `python manage.py migrate` para atualizar o banco de dados.

![Terminal-Migration-0003](/printscreens/Terminal-Migration-0003.png)

49. Use o Django Admin (ou Shell) para atualizar os valores de nome e descrição dos produtos.
50. Modifique produto.html e conteudo.html para que referenciam campos de Produtos corretamente.
51. Em settings.py e base.html, mude o idioma para "pt-br"

![Site-Home-V2](/printscreens/Site-Home-V2.png)


Obs.: pyburguer é o core.


# Referências
Udemy - Django 4 e Bootstrap 5 em 120 minutos:
https://www.udemy.com/course/django-em-120-minutos/