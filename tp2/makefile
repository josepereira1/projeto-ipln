FUNCTIONALLY_TYPE = 0			#	0 -> top_reg_by_elem(), 1 ->top_reg_in_file e 2 ->top_reg_sort_by_atribute 
INPUT_FILES = 'data/Posts.xml'	#	ficheiro ou ficheiros de input
ATRIBUTES = 'Body'				#	atributo da tag do ficheiro a analisar
REGEX = 'java'					# 	expressão regular
LIMIT = 10						#	top 10

#	EXECUÇÃO PERSONALIZADA PARA CADA TIPO DE FUNCIONALIDADE (PODE SE MUDAR OS ARGUMENTOS ACIMA):

run_f1: xmlstats.py
	python3 xmlstats.py -t 0 -f ${INPUT_FILES} -a ${ATRIBUTES} -r ${REGEX} -l ${LIMIT}

run_f2: xmlstats.py
	python3 xmlstats.py -t 1 -f ${INPUT_FILES} -a ${ATRIBUTES} -r ${REGEX} -l ${LIMIT}


SPECIAL_REGEX = "[0-9]+"		#	se o atributo for inteiro, a REGEX deverá ser [0-9]+, e [A-Za-z\ ]+ no caso de texto
CAST_INT = 1					#	esta variável só é usada na funcionalidade <<-t 2>> e deve estar a 1 quando o <<ATRIBUTES>> usado é inteiro e 0 caso contrário
SPECIAL_ATRIBUTES = "Score"		#	atributo é a métrica de ordenação nesta funcionalidade, recomendamos a utilização dos atributos "Score" (Posts.xml) , "Reputation" (Users.xml), ...

run_f3: xmlstats.py
	python3 xmlstats.py -t 2 -f ${INPUT_FILES} -a ${SPECIAL_ATRIBUTES} -r ${SPECIAL_REGEX} -c ${CAST_INT} -l ${LIMIT}


#	IMPORTANTE: 
#	podem ser enviados mais do que um ficheiro de input, no entanto é preciso lembrar
#	que nesse caso, também devem ser enviados a mesma quantidade de <<ATRIBUTES>>, porque
#	eles são respetivos a cada ficheiro, isto é se:

#	INPUT_FILES = 'data/Posts.xml,data/Comments.xml'
#	ATRIBUTES = 'Body,Text'

#	o campo Body está presente no ficheiro Posts.xml, o Text no ficheiro Comments.xml





#	MACROS DE EXEMPLOS DE EXECUÇÃO:

f1: xmlstats.py data/Posts.xml 
	python3 xmlstats.py -t 0 -f 'data/Posts.xml' -a 'Body' -r 'java' -c 1 -l 15

f2: xmlstats.py data/Posts.xml 
	python3 xmlstats.py -t 1 -f 'data/Posts.xml' -a 'Body' -r 'java' -l 10

f3: xmlstats.py data/Posts.xml 
	python3 xmlstats.py -t 2 -f 'data/Posts.xml' -a 'Score' -r '[0-9]+' -c 1 -l 15

#	EXEMPLO DE EXECUÇÃO COM VÁRIOS FICHEIROS E RESPETIVOS ATRIBUTOS:

f4: xmlstats.py data/Posts.xml data/Comments.xml
	python3 xmlstats.py -t 0 -f 'data/Posts.xml,data/Comments.xml' -a 'Body,Text' -r 'java' -l 15