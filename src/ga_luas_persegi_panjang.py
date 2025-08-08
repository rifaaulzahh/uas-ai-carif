import streamlit as st
import random

st.title("Algoritma Genetika: Cari Panjang & Lebar dari Luas Persegi Panjang")

# Input dari user
target_area = st.number_input("Masukkan luas yang diinginkan:", min_value=1, value=120)
population_size = st.slider("Ukuran Populasi", 4, 100, 10)
generations = st.slider("Jumlah Generasi", 10, 500, 50)
mutation_rate = st.slider("Tingkat Mutasi", 0.0, 1.0, 0.1)

# Fungsi dasar GA
def create_individual():
    return [random.randint(1, 100), random.randint(1, 100)]

def fitness(individual):
    p, l = individual
    return -abs((p * l) - target_area)

def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

def crossover(parent1, parent2):
    child1 = [parent1[0], parent2[1]]
    child2 = [parent2[0], parent1[1]]
    return [child1, child2]

def mutate(individual):
    if random.random() < mutation_rate:
        individual[random.randint(0,1)] = random.randint(1, 100)
    return individual

if st.button("Jalankan Algoritma"):
    population = [create_individual() for _ in range(population_size)]
    best_fitness_list = []

    for gen in range(generations):
        selected = selection(population)
        offspring = []
        while len(offspring) < population_size:
            children = crossover(selected[0], selected[1])
            offspring.extend([mutate(c) for c in children])
        population = offspring[:population_size]
        best_fitness_list.append(-fitness(selection(population)[0]))

    best = max(population, key=fitness)
    st.success(f"Hasil terbaik: Panjang = {best[0]}, Lebar = {best[1]}, Luas = {best[0]*best[1]}")

    # Tampilkan grafik
    st.line_chart(best_fitness_list)
