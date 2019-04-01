#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import polyglot
from polyglot.text import Text, Word
import info_extract
import scrap


def lprint(s):
	for i in s:
		print i



def applicationDev(url):
	
	#blob = " A economia brasileira já não está em recessão, mas isso não significa que a crise foi superada. O valor do PIB em 2016 foi 6,9% menor do que em 2014, mas cresceu 1% em 2017 e a estimativa da consultoria Tendências é que cresça outros 1,7% em 2018 e 2,9% em 2019. Mas a recuperação é desigual e será suficiente para que apenas 8 estados brasileiros atinjam finalmente em 2019 o nível de atividade registrado em 2014. Veja quais são eles:  Todos os estados que vão se recuperar mais rápido estão na região Norte e Centro-Oeste, “impulsionados principalmente pelo agronegócio e mineração, além da forte exposição ao mercado externo”, segundo a consultoria. A agropecuária, por exemplo, respondeu por 70% de todo o crescimento do país no ano de 2017. Sem ela, a expansão do PIB naquele ano teria sido de 0,2% e não 1%. O maior destaque do ranking é o Pará, um dos estados menos afetados pela crise, com queda acumulada de apenas 1,2% no biênio 2015/2016. Segundo Camila Saito, economista da Tendências, a explicação está nos grandes investimentos de mineração da Vale no estado. De forma geral, foram bastante os estados com forte participação dos setores mais afetados pela crise, como o industrial. É o caso de São Paulo e Rio de Janeiro, por exemplo. “2019 devemos ter uma retomada mais forte da indústria, que vem se recuperando mais lentamente do que o esperado, com piora ainda maior das estimativas devido a essa greve dos caminhoneiros”, diz Camila. Na outra ponta do ranking estão os estados que terminarão 2019 ainda muito distantes da recuperação plena, como Alagoas (nível -8,4% menor), Sergipe (-7,8%) e Pernambuco (-7,5%). O Nordeste, de forma geral, depende muito de investimento público e transferências do governo, dois fatores cujo cenário de recuperação ainda é muito incerto. O quarto estado mais distante do nível pré-crise será o Espírito Santo, recorde de perdas no biênio 2015/2016, em grande parte devido aos efeitos da tragédia de Mariana (MG). Veja no mapa o valor previsto pela Tendências para o PIB em 2019 em todos os estados em relação ao valor registrado em 2014: "


	#url = 'https://g1.globo.com/economia/noticia/2018/10/10/pobreza-extrema-cresce-em-25-estados-brasileiros-aponta-estudo.ghtml'
	#url = 'https://g1.globo.com/mg/minas-gerais/desastre-ambiental-em-mariana/noticia/2018/11/27/em-painel-que-discute-tragedia-de-mariana-atingidos-dizem-que-anseiam-em-recuperar-o-controle-das-proprias-vidas.ghtml'
	#url = 'https://g1.globo.com/df/distrito-federal/noticia/2019/03/12/acidente-frontal-entre-carro-e-onibus-escolar-no-df-deixa-dois-mortos-e-criancas-feridas.ghtml'
	#url = 'https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml' 

	blob = scrap.get_paragraph(url)

	# todos os toponimos presentes no texto
	topon = info_extract.parse_text_toponimo(blob)

	# remove toponimos repetidos
	newlist_t=[ii for n,ii in enumerate(topon) if ii not in topon[:n]]

	# toponimos na ordem em que aparecem no texto
	toponimos = info_extract.sortToponymOccurence(info_extract.get_sentence(blob), newlist_t)


	# para cada toponimo -> pegar json associado e criar lista
	json_data = scrap.getToponymAndAttachJson(toponimos)
	
	#insere a tag select em cada toponimo
	select_options = info_extract.insertDataIntoSelectTag(json_data)

	# pega todas as frases da noticia
	sentence = info_extract.get_sentence(blob)

	# cria um botao com o nome do toponimo 
	toponym_button_text = info_extract.create_text_button(newlist_t)

	# texto gerado
	inicial_text = info_extract.replaceMultiple(sentence,newlist_t,toponym_button_text)
	
	# texto gerado
	text_with_button = info_extract.putButtonIndex(inicial_text)
	

	final_text = info_extract.generateText(text_with_button, select_options)	

	return (final_text, toponimos)