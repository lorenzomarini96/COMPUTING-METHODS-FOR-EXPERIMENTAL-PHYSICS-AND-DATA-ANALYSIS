#!/usr/bin/env python3
"""Programma che grafica un istogramma di valori distribuiti secondo una 
   distribuzione gaussiana. Inoltre calcola il valor medio e la deviazione
   standard dei valori generati.
"""

import numpy as np
import random 
import matplotlib.pyplot as plt
import argparse
import logging

logging.basicConfig(level=logging.INFO)


def gauss_distribution(mu, sigma, N):
	"""Funzione che genera dati distribuiti secondo Gauss.
	"""
	# Imposta il seme.
	seed = np.random.seed(1)
	# Generazione di dati distribuiti gaussianamente con media mu, std sigma, e dimensione N.
	data = np.random.normal(mu, sigma, N)
	logging.info(f"Generated Data: {data}")
	
	# Calcolo la media (per vederne il confronto con quella usata per la generazione).	
	mean = np.mean(data)
	# Calcolo la stardard deviation (per vederne il confronto con quella usata per la generazione).	
	std = np.std(data)

	logging.info(f"MEAN = {mean:.2f}")
	logging.info(f"STD = {std:.2f}")

def histogram_gauss(mu, sigma, N):
	"""Funzione che genera dati distribuiti secondo Gauss.
	"""
	# Imposta il seme.
	seed = np.random.seed(1)
	# Generazione di dati distribuiti gaussianamente con media mu, std sigma, e dimensione N.
	data = np.random.normal(mu, sigma, N)

	# Calcolo la media (per vederne il confronto con quella usata per la generazione).	
	mean = np.mean(data)
	# Calcolo la stardard deviation (per vederne il confronto con quella usata per la generazione).	
	std = np.std(data)

	logging.info(f"MEAN = {mean:.2f}")
	logging.info(f"STD = {std:.2f}")

	bin_heights, bin_bordes, _ = plt.hist(data,
									     50, 
										 #range=(min_value, max_value), 
										 density=False, 
										 #facecolor='green',
										 #label='data',
										 #edgecolor='black')
										 )

	sigma_bin_heights = np.sqrt(bin_heights)  # Poisson error.
	bin_centers = 0.5 * (bin_bordes[1:] + bin_bordes[:-1])

	# FIGURE:
	plt.figure(1, figsize=(8,4))
	plt.errorbar(bin_centers, bin_heights, sigma_bin_heights, fmt='.', color="black", label="Data simulated")

	# Bellurie
	plt.xlabel('data')
	plt.ylabel('Counts')
	plt.title(f'Histogram: $\mu$ = {mu}, $\sigma$ = {sigma}, $N$ = {N}')
	plt.legend()


	plt.show()



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Programma che grafica un istogramma di 'N' valori distribuiti secondo una distribuzione gaussiana.")
	# ARGOMENTI POSIZIONALI:
	parser.add_argument("mu", type=int, help="Valore medio della distribuzione simulata.")
	parser.add_argument("sigma", type=int, help="Deviazione standard della distribuzione simulata.")
	parser.add_argument("N", type=int, help="Numero di valori che si vuole generare.")
	# ARGOMENTO OPZIONALE:
	parser.add_argument("-p", "--plot", help="Mostra il grafico della distribuzione gaussiana creata.", action="store_true")
	args = parser.parse_args()


	if args.plot:
		histogram_gauss(args.mu, args.sigma, args.N)
	else:
		gauss_distribution(args.mu, args.sigma, args.N)	




