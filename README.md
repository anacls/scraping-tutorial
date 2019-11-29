## Tutorial WebScraping - Grupy Jundiaí - 2019 ##
![](https://img.shields.io/badge/Python-3.5%2C%203.6-blue.svg)

Tutorial de Web Scraping apresentado no Grupy Jundiaí em 30/11/2019, na Fatec

Esse tutorial apresenta duas ferramentas para WebScraping: BeautifulSoup e Scrapy

O script para o BeautifulSoup está na pasta beautifulsoup

O script para o Scrapy está na pasta quotes
___

#### Por onde começar ####

Crie seu virtualenv

* Ambiente Linux

    Recomendamos o uso do [VirtualEnv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

    ```
    mkvirtualenv --python=/usr/bin/python3.6 tutorial-scrape
    ```

    Ou usando o nativo do Python

    ```
    pip install virtualenv

    virtualenv tutorial-scrape
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
    c:\<alguma_pasta_sua> >c:\Python36\Scripts\virtualenv.exe virtualenv\tutorial-scrape
    ```

Ativa seu virtualenv

* Linux

    VirtualEnv Wrapper
    ```
    workon tutorial-scrape
    ```
    ou

    ```
    source tutorial-scrape/bin/activate
    ```
  
  
* Windows

    ```
    c:\<alguma_pasta_sua>\virtualenv\Scripts\activate
    ```


Instale as dependências ou libs

```
(tutorial-scrape) pip install -r requirements.txt
```

___

#### Como Executar ####

* BeautifulSoup

    Entre na pasta /beautifulsoup e execute o comando python scrape_by_soup.py

    ```
    (tutorial-scrape) cd beautifulsoup
    (tutorial-scrape) python scrape_by_soup.py
    ```

* Scrapy

    Entre na pasta /quotes e execute o comando scrapy crawl quotes 
    ```
    (tutorial-scrape) cd quotes
    (tutorial-scrape) scrapy crawl quotes
    ```


#### Requirements ####

* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [scrapy](https://docs.scrapy.org/en/latest/)


___


#### Autor ####

Ana & Paulo Henrique


#### Referências ####

* [VirtualEnv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [Crianda Virtual Envs no Windows](https://fernandofreitasalves.com/tutorial-virtualenv-para-iniciantes-windows/)
