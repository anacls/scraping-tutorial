from bs4 import BeautifulSoup

with open("tres_porquinhos.html") as fp:
    soup = BeautifulSoup(fp)

    paragrafos = soup.findAll('p')
    for paragrafo in paragrafos:
        print(paragrafo)

    paragrafo_dois = paragrafos[1]
    print(paragrafo_dois)

    paragrafo_dois.findAll('a')
    links = paragrafo_dois.findAll('a')
    for link in links:
        print(link)
