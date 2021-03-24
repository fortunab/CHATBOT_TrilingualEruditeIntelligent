import yaml
import random

def convorbireXAI(mesaj):
    l=[]
    with open(r'xai.yml') as file:
        xai_list = yaml.load(file, Loader=yaml.FullLoader)
        for i in xai_list['conversations']:
            if i[0].lower().find(mesaj.lower()) != -1 or mesaj.lower().find(i[0].lower()) == 0:
                l.append(i[1])

    if l == []:
        return xai_list['conversations'][random.randint(0, len(xai_list['conversations']))][1]
    else:
        return random.choice(l)


