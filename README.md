## Tutorial WebScraping - Grupy Jundiaí - 2019 ##
![](https://img.shields.io/badge/Python-3.5%2C%203.6-blue.svg)

Tutorial de Webscraping apresentado no Grupy Jundiaí em 30/11/2019, na Fatec

Esse tutorial apresenta 3 ferramentas para WebScraping: BeautifulSoap e Scrapy

O script para o BeautifulSoap está na pasta beautifulSoap

O script para o Scrapy está na pasta quotes
___

#### Por onde começar ####

Crie seu virtualenv

* Ambiente Linux

    Recomendamos o uso do [VirtualEnv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

    ```
    mkvirtualenv --python=/usr/bin/python3.6 tutorial-scrap
    ```

    Ou usando o nativo do Python

    ```
    pip install virtualenv

    virtualenv tutorial-scrap
    ```

* Ambiente Windows

    ```
    c:\Python36\Scripts\pip.exe install virtualenv      
    ```
    Depois crie um diretório onde estarão seus ambientes virtuais
    
    ```
    c:\<alguma_pasta_sua> > mkdir virtualenv
    ```
  
    Crie o virtualenv
    ```
    c:\<alguma_pasta_sua> >c:\Python36\Scripts\virtualenv.exe virtualenv\tutorial-scrap
    ```

Ativa seu virtualenv

* Linux

    VirtualEnv Wrapper
    ```
    workon tutorial-scrap
    ```
    ou

    ```
    source tutorial-scrap/bin/activate
    ```
  
  
* Windows

    ```
    c:\<alguma_pasta_sua>\virtualenv\Scripts\activate
    ```


Instale as dependências ou libs

```
(tutorial-scrap) pip install -r requirements.txt
```

___

#### Como Executar ####

* BeautifulSoap

    Entre na pasta /beautifulsoap e execute o comando python scrap_by_soap.py

    ```
    cd beautifulsoap
    (tutorial-scrap) python scrap_by_soap.py
    ```

* Scrapy

    Entre na pasta /quotes e execute o comando scrapy crawl quotes 
    ```
    cd quotes
    (tutorial-scrap) scrapy crawl quotes
    ```


#### Requirements ####

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [scrapy](https://docs.scrapy.org/en/latest/)


___


#### Autor ####

Ana


#### Referências ####

* [VirtualEnv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [Crianda Virtual Envs no Windows](https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/)