import sys
import numpy as np






"""
alpha = os alpha/100 * size(C) candidatos de C irão formar a RCL. Um membro randômico deles irá entrar para a
lista de soluções
"""


def Grasp(seed, alpha, clientes):
	solucao_atual = S0

	while must_stop == False:
		solucao_aux = SolucaoRandomicaGulosa(alpha)
		solucao_aux = BuscaLocal(solucao_aux)
		if Avalia(solucao_nova) > Avalia(solucao_atual):
			solucao_atual = solucao_nova


	return solucao_atual



def TrataPorcento(alpha):
	if alpha < 1 or alpha > 100:
		return 10
	else:
		return alpha



def SolucaoRandomicaGulosa(alpha):
	i = 2



def BuscaLocal():
	i = 2


def Avalia():
	i = 2

def main(seed, alpha, archivename):

	seed = TrataPorcento(int(seed))
	alpha = TrataPorcento(int(alpha))
	print ("\n\n\nEssa é a seed:",seed,"Esse é o alpha:", alpha,"Esse é o nome do arquivo:",archivename,"\n\n\n")


	#abre o arquivo e preenche as estruturas correpondentes
	file = open(archivename,'r')
	content = file.read()
	file.close()
	content = content.split('\n')
	quantidade_itens = int(content[0])
	capacidade_segundo = int(content[1])
	clientes = content[2:quantidade_itens+2]
	for i in range(len(clientes)):
		clientes[i] = clientes[i].split()
	for i in range(len(clientes)):
		for j in range(4):
			clientes[i][j]=int(clientes[i][j]) 

	
	print(clientes)


main(sys.argv[1],sys.argv[2],sys.argv[3])