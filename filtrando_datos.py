DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"]>18, DATA)) # Filtrar datos
    adults = list(map(lambda worker: worker["name"], DATA)) # Buscar datos
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] > 70}, DATA)) # Agregar datos
    
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2))
    
    all_platzi_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers2 = list(map(lambda worker: worker["name"], all_platzi_workers2))
    
    adults2 = [worker["name"] for worker in DATA if worker["age"]>18]
    
    for worker in adults:
        print(worker)
        
    print("-------------")
        
    for worker in adults2:
        print(worker)
        
    print(str(adults == adults2))

if __name__ == '__main__':
    run()