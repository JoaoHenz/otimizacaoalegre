import sys
import numpy as np
from Grasp import *
from Misc import *


"""
alpha = os alpha/100 * size(C) candidatos de C irão formar a RCL. Um membro randômico deles irá entrar para a
lista de soluções
"""


def main(archivename, upperbound, seed, alpha):

	'''
	lista_eficiencia = [[0 for x in range(100)] for y in range(2)] 
	print(lista_eficiencia[1][3])
	input("eu sou deus")'''



	alpha = Misc.TrataPorcento(int(alpha))
	print ("\n\n\nEsta é a seed:",seed,"||Este é o alpha:", alpha,"||Este é o upperbound:",upperbound,"||Este é o caminho do arquivo:",archivename)

	info = Misc.AbreArquivo(archivename)
	clientes = info[0]
	quantidade_itens = info[1]
	capacidade_segundo = info[2]
	seginicio = Misc.BuscaInicio(clientes)
	segfim = Misc.BuscaFim(clientes)


	#print("Arquivo foi lido com sucesso!")
	#input("Pressione Enter para continuar...")

	solucao_inicial = Misc.GeraSolucaoInicial(seed,seginicio,segfim,capacidade_segundo,clientes)
	#print("Solução inicial criada com sucesso!")
	#input("Pressione Enter para continuar...")


	solucao_final = Grasp.main(alpha, int(upperbound),capacidade_segundo,segfim,solucao_inicial, clientes)
	#print("O Grasp foi executado com sucesso!")
	#input("Pressione Enter para continuar...")




	print("Fim do Programa\n\n\n")


if len(sys.argv)==5:
	main(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4])
elif len(sys.argv)==4:
	main(sys.argv[1],sys.argv[2],sys.argv[3], "10")
elif len(sys.argv)==3:
	main(sys.argv[1],sys.argv[2],"14141", "10")