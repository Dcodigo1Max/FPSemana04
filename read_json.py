import json

try:
    path =input()
    file = open(path,"rt", encoding="utf-8")
    json_data = file.read() 
    data = json.loads(json_data) 
    print("caminho_certo/data.json")
    print(data) 
    file.close()
except:
    print("caminho errado/data.json")
    print("Ocorreu um erro!")
finally:
    print("Processo Concluido!")
