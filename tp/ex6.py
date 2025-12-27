etudients = [
    {
        "nome": "student1",
        "age": 17,
        "matieres": ["analyse", "algebre", "python" , "c"],
    },
    {
        "nome": "student2",
        "age": 18,
        "matieres": ["analyse", "algebre", "python" , "c"],
      },
    {
        "nome": "student3",
        "age": 20,
        "matieres": ["analyse", "algebre", "python" , "c"],
    }
]
matieres = ["mtu", "arab"]

etudients.pop(0)
etudients[1]["matieres"] = matieres




for etudient in etudients:
    print(etudient)

