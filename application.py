# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tutor
import scrap
import random
import files

from flask import request, Flask, render_template, url_for

app = Flask(__name__)

# urls = [
# 	['https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2019/03/20/foragido-por-assassinato-de-jovem-de-guarulhos-e-preso-em-atibaia.ghtml',""],
# 	['https://g1.globo.com/politica/noticia/2019/03/20/alexandre-de-moraes-indica-dois-delegados-para-atuar-no-inquerito-que-investiga-ofensas-ao-stf.ghtml',""],
# 	['https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml',""],
# 	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/justica-de-minas-bloqueia-r-7784-milhoes-do-filho-de-thor-batista.ghtml',""],
# 	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
# 	]

urls = [
	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
	]

for i in urls:
	if not i[1]:
		i[1] = tutor.applicationDev(i[0])

# urls[17][1] = tutor.applicationDev(urls[17][0])


len_urls_available = len(urls)
toponyms = []
user_data = []
data_to_store = []
random_news = 0
title = ""
gen_data = []
noticia = ""
#=====

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/avaliar', methods=['POST','GET'])
def avaliar():
	global toponyms
	global user_data
	global random_news
	global data_to_store
	global title
	global gen_data
	global noticia

	if request.method == 'POST':
		i=0
		qt_of_tops = len(toponyms)
		# del toponyms[:]

			
		while qt_of_tops > 0:
			top = request.form.get('top_data_'+str(i))
			conf = request.form.get('confi_data_'+str(i))
			i = i+1
			qt_of_tops = qt_of_tops - 1
			if top is not None:
				if conf is not None:
					user_data.append((top,conf))


		data_to_store.append((urls[random_news][0], user_data))
		files.dataFromUser(title, data_to_store)
		data_to_create_json = files.processData(title, urls[random_news][0])
		


		# if news is closed then write into a file
		if data_to_create_json != False:
			files.generateNewsJsonFiles(data_to_create_json, toponyms, urls[random_news][0],title)

		del data_to_store[:]


		# limpa os dados, para nao acc 
		del user_data[:]
		

		if request.form['submit_button'] == 'Do Something':
	            

			random_news = random.randint(0,(len_urls_available-1)) 
			url = urls[random_news][0]
			#print "The random news is : ", random_news

			gen_data = urls[random_news][1]
			noticia = gen_data[0]
			toponyms = gen_data[1]
			title = scrap.getTitle(url)

			return render_template("avaliar.html", title=title, noticia=noticia)

		elif request.form['submit_button'] == 'Do Something Else':
			return render_template("validar.html")
	            

	if request.method == 'GET':
		random_news = random.randint(0,(len_urls_available-1)) 
		url = urls[random_news][0]
		#print "The random news is : ", random_news

		gen_data = urls[random_news][1]
		noticia = gen_data[0]
		toponyms = gen_data[1]
		title = scrap.getTitle(url)

		return render_template("avaliar.html", title=title, noticia=noticia)

	



@app.route('/validar', methods=['post','get'])
def validar():

	return render_template("validar.html")
	

def lprint(lista):
	for each in lista:
		print each[0], each[1]




if __name__ == '__main__':
	app.run(debug=True)
