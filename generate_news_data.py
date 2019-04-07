import tutor
import json

urls = [
	['https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2019/03/20/foragido-por-assassinato-de-jovem-de-guarulhos-e-preso-em-atibaia.ghtml',""],
	['https://g1.globo.com/politica/noticia/2019/03/20/alexandre-de-moraes-indica-dois-delegados-para-atuar-no-inquerito-que-investiga-ofensas-ao-stf.ghtml',""],
	['https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/justica-de-minas-bloqueia-r-7784-milhoes-do-filho-de-thor-batista.ghtml',""],
	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
	]

# urls = [
# 	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
# 	]


def generateNews():
    global urls

    for i in urls:
	    if not i[1]:
		    i[1] = tutor.applicationDev(i[0])

def saveNews():
    global urls

    with open("preProssedNews/news.txt", "w") as file:
        json_str = json.dumps(urls, ensure_ascii=False).encode('utf8')
        file.write(json_str)

if __name__ == '__main__':
    generateNews()
    saveNews()


