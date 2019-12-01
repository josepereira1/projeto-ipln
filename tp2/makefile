type = 0						#	0 -> top_reg_by_elem() e 1 ->top_reg_in_file 
inputFiles = 'data/Posts.xml'	#	ficheiro/ficheiros de input
atributes = 'Body'				#	atributo da tag, neste caso do Posts.xml
regex = 'java'					# 	expressão regular
limit = 10						#	top 10
	
run: xmlstats	#	o comando run deve ser utilizado quando deseja correr o programa na pasta de download
	python3 xmlstats -t ${type} -f ${inputFiles} -a ${atributes} -r ${regex} -l ${limit}

#	IMPORTANTE: podem ser enviados mais do que um ficheiro de input, no entanto é preciso lembrar
#				que nesse caso, também devem ser enviados a mesma quantidade de atributes, porque
#				eles são respetivos a cada ficheiro, isto é se:

#				inputFiles = 'data/Posts.xml,data/Comments.xml'
#				atributes = 'Body,Text'

#				o campo Body está presente no ficheiro Posts.xml, o Text no ficheiro Comments.xml