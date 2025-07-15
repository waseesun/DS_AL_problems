import random

class Genetic_Algo:
    
    def __init__(self, act_result, population, mutation_rate):
        self.act_result = act_result
        self.population = population
        self.crossover_point = len(population[1]) // 2
        self.mutation_rate = mutation_rate
        self.generation = 0
        
    def fitness(self, individual):
        fit = 0
        for i in range(len(individual)):
            if individual[i] == self.act_result[i]:
                fit += 1
        return fit
    
    def selection(self, fit_arr, n):
        parent_arr = []
        
        for i in range(n):
            random_key = random.choice(list(fit_arr.keys()))
            parent_arr.append(random_key)
                
        return parent_arr
        
    
    def crossover(self, parent_arr):
        offspring_arr = []
        
        # Crossover
        for i in range(len(parent_arr) // 2):
            parent1 = random.choice(parent_arr)
            if offspring_arr.count(parent1) > 1:
                offspring_arr.remove(parent1)
            while True:
                parent2 = random.choice(parent_arr)
                if parent2 != parent1:
                    break
                
            if offspring_arr.count(parent2) > 1:
                offspring_arr.remove(parent2)
            
            child1 = parent1[:self.crossover_point] + parent2[self.crossover_point:]
            child2 = parent2[:self.crossover_point] + parent1[self.crossover_point:]
            
            if child1 in offspring_arr:
                mutated_child1 = self.mutation(child1)
                child1 = mutated_child1
            if child2 in offspring_arr:
                mutated_child2 = self.mutation(child2)
                child2 = mutated_child2
            
            offspring_arr.append(child1)
            offspring_arr.append(child2)
            
        # Addin an extra offspring if the number of parents is odd or
        # if the number of offspring is not equal to the number of parents
        while len(offspring_arr) != len(parent_arr):
            random_index = random.randint(0, len(parent_arr) - 1)
            mutated_child = self.mutation(parent_arr[random_index])
            if mutated_child not in offspring_arr:
                offspring_arr.append(mutated_child)
                    
        
        return offspring_arr
    
    def mutation(self, child):
        for i in range(self.mutation_rate):
            random_index = random.randint(0, len(child) - 1)
            if child[random_index] == "0":
                child = child[:random_index] + "1" + child[random_index + 1:]
            else:
                child = child[:random_index] + "0" + child[random_index + 1:]
                
        return child
    
    def genetic_process(self):
        print(f"Actual result: {self.act_result}")
        while True:
            print(f"Generation {self.generation}: {self.population}")
            for individual in self.population:
                if individual == self.act_result:
                    print(f"Found the solution in generation {self.generation}")
                    return
            fit_arr = {}
            for individual in self.population:
                fitness = self.fitness(individual)
                if fitness > 0:
                    fit_arr[individual] = fitness
                
            elite = max(fit_arr)
            del fit_arr[elite]
            parent_arr = self.selection(fit_arr, len(self.population) - 1)
            offspring_arr = self.crossover(parent_arr)
            offspring_arr.append(elite) 
            self.population = offspring_arr
            self.generation += 1
        
      
def random_n_digits(n):
    return "".join([str(random.randint(0, 1)) for i in range(n)]) 
        
if __name__ == "__main__":
    n_bits = 4
    population_count = 6
    mutation_rate = 1
    gen_al = Genetic_Algo(
        random_n_digits(n_bits),
        # ["0100", "1010", "1001", "0101", "0110", "0111"],
        [random_n_digits(n_bits) for i in range(population_count)], 
        mutation_rate
    )
    gen_al.genetic_process()