import random
import time

colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
prefession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

rev_colors = {v: k for k, v in colors.items()}
rev_profession = {v: k for k, v in prefession.items()}
rev_language = {v: k for k, v in languaje.items()}
rev_database = {v: k for k, v in database.items()}
rev_editor = {v: k for k, v in editor.items()}

def decode_value(diccionario, clave):
    return diccionario.get(clave, 'ERROR')

class Phenotype:
    def __init__(self):
        self.chromosome = self.encode()
        self.score = 0

    def encode(self):
        chromosome = []
        for _ in range(5):
            gene = [random.choice(list(colors.keys())),
                    random.choice(list(prefession.keys())),
                    random.choice(list(languaje.keys())),
                    random.choice(list(database.keys())),
                    random.choice(list(editor.keys()))]
            chromosome += gene
        return chromosome

    def decode(self):
        return [[colors[self.chromosome[i*5+0]], 
                 prefession[self.chromosome[i*5+1]],
                 languaje[self.chromosome[i*5+2]],
                 database[self.chromosome[i*5+3]],
                 editor[self.chromosome[i*5+4]]] for i in range(5)]

    def mutate(self):
        index = random.randint(0, len(self.chromosome) - 1)
        keys = list(colors.keys()) if index % 5 == 0 else \
               list(prefession.keys()) if index % 5 == 1 else \
               list(languaje.keys()) if index % 5 == 2 else \
               list(database.keys()) if index % 5 == 3 else \
               list(editor.keys())
        self.chromosome[index] = random.choice(keys)

    def fitness_function(self):
        self.score = 0
        chromosome = self.decode()

        for house in chromosome:
            if house[1] == 'Mathematician' and house[0] == 'red':
                self.score += 1
            if house[1] == 'Hacker' and house[2] == 'Python':
                self.score += 1
            if house[0] == 'green' and house[4] == 'Brackets':
                self.score += 1
            if house[1] == 'Analyst' and house[4] == 'Atom':
                self.score += 1
            if house[3] == 'Redis' and house[2] == 'Java':
                self.score += 1
            if house[3] == 'Cassandra' and house[0] == 'yellow':
                self.score += 1
            if house[4] == 'Notepad++' and chromosome.index(house) == 2:
                self.score += 1
            if house[1] == 'Developer' and chromosome.index(house) == 0:
                self.score += 1
            if house[1] == 'Developer' and house[0] == 'blue':
                self.score += 1
            if house[3] == 'Neo4j' and house[4] == 'Sublime Text':
                self.score += 1
            if house[1] == 'Engineer' and house[3] == 'MongoDB':
                self.score += 1

        for i in range(4):
            if chromosome[i][0] == 'white' and chromosome[i+1][0] == 'green':
                self.score += 1
            if chromosome[i][3] == 'HBase' and chromosome[i+1][2] == 'JavaScript':
                self.score += 1
            if chromosome[i][3] == 'Cassandra' and chromosome[i+1][2] == 'C#':
                self.score += 1

    def __lt__(self, other):
        return self.score > other.score  # maximizamos

class Riddle:
    def __init__(self):
        self.start_time = time.time()
        self.population = []

    def solve(self, n_population):
        self.generate(n_population)

        for individual in self.population:
            individual.fitness_function()

        fit, indi = self.iterar()
        print(f"\n\nResultado Final\nFitness: {fit}\n")
        for i, casa in enumerate(indi.decode()):
            print(f"Casa {i+1}: {casa}")

        for i, casa in enumerate(indi.decode()):
            if casa[4] == 'Vim':
                print(f"\n➡️ La persona que usa Vim vive en la casa {i+1} y es {casa[1]}")

    def iterar(self):
        counter = 0
        max_generations = 1000

        while counter < max_generations:
            self.population.sort()
            next_generation = self.population[:100]

            while len(next_generation) < len(self.population):
                parent1 = random.choice(self.population[:100])
                parent2 = random.choice(self.population[:100])
                child = self.crossOver(parent1, parent2)
                if random.random() < 0.2:
                    child.mutate()
                child.fitness_function()
                next_generation.append(child)

            self.population = next_generation
            counter += 1

            if self.population[0].score >= 15:
                break

        return self.population[0].score, self.population[0]

    def generate(self, i):
        for _ in range(i):
            newbie = Phenotype()
            self.population.append(newbie)

    def crossOver(self, parent1, parent2):
        cut = random.randint(0, len(parent1.chromosome))
        child_chrom = parent1.chromosome[:cut] + parent2.chromosome[cut:]
        child = Phenotype()
        child.chromosome = child_chrom
        return child

start = time.time()
rid = Riddle()
rid.solve(n_population = 500)
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("\nTiempo total: {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
