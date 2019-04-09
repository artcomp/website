import tutor
import json


urls = [
	['https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml',""],
	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/03/28/carrefour-cortara-mais-de-1-mil-empregos-na-franca-diz-sindicato.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/22/homem-e-suspeito-de-matar-mulher-em-belo-horizonte.ghtml',""],
	['https://g1.globo.com/natureza/noticia/2019/03/28/como-a-alemanha-faz-para-evitar-que-animais-vivam-abandonados-nas-ruas.ghtml',""],
	['https://g1.globo.com/sc/santa-catarina/noticia/2019/04/02/carga-de-cocaina-e-apreendida-no-porto-de-navegantes.ghtml',""],
	['https://g1.globo.com/pe/pernambuco/noticia/2019/04/06/casal-e-agredido-com-facadas-durante-tentativa-de-assalto.ghtml',""],
	['https://g1.globo.com/pe/pernambuco/noticia/2019/04/05/reducao-de-atendimento-no-expresso-cidadao-de-olinda-causa-transtornos-para-a-populacao.ghtml',""],
	['https://g1.globo.com/go/goias/noticia/2019/04/07/alunos-de-goiania-desenvolvem-robo-para-torneio-internacional-nos-estados-unidos.ghtml',""],
	['https://g1.globo.com/pr/norte-noroeste/noticia/2019/04/08/londrina-recebe-doses-da-vacina-contra-gripe-campanha-comeca-nesta-quarta-feira-10.ghtml',""],
	['https://g1.globo.com/mundo/noticia/2018/10/21/principe-harry-vai-a-evento-sem-meghan-que-reduz-agenda-por-causa-da-gravidez.ghtml',""],
	['https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2019/04/05/ministro-diz-que-preservacao-ambiental-nao-pode-ser-uma-agenda-do-bom-mocismo.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/03/onu-lanca-em-sp-plataforma-online-que-auxilia-empresas-na-contratacao-de-refugiados-no-brasil.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/03/20/verao-2019-foi-o-5o-mais-quente-da-historia-outono-tera-temperaturas-pouco-acima-da-media.ghtml',""],
	['https://g1.globo.com/rj/rio-de-janeiro/noticia/2019/03/20/policia-investiga-morte-de-jovem-de-18-anos-com-oito-tiros-na-baixada-fluminense.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/ipva-2019-em-mg-prazo-para-pagar-3a-parcela-termina-quarta.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/camara-de-bh-aprova-em-1o-turno-projeto-que-autoriza-botao-de-panico-em-escolas.ghtml',""],
	['https://g1.globo.com/df/distrito-federal/noticia/2019/04/05/operacao-investiga-grupo-que-desviou-mais-de-r-800-mil-de-clientes-do-bando-de-brasilia.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/doria-diz-que-nao-vai-cortar-servicos-nem-fechar-espacos-culturais-de-sp.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/mais-de-600-raios-atingem-a-grande-sp-durante-temporal-no-domingo.ghtml',""],
	]

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


