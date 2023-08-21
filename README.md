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

Obs.: pyburguer é o core.


# Referências
Udemy - Django 4 e Bootstrap 5 em 120 minutos:
https://www.udemy.com/course/django-em-120-minutos/