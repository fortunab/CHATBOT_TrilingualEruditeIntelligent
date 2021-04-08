import yaml
import random

def findvrc(vrc):
    f = vrc.find("http")
    if f == -1:
        return vrc
    else:
        vrc = vrc.replace("(", "<a href=\'")
        vrc = vrc.replace(")", "\'>here")
        print(vrc)
        return vrc

def convorbireXAI(mesaj):
    l=[]
    with open(r'xai.yml') as file:
        xai_list = yaml.load(file, Loader=yaml.FullLoader)
        for i in xai_list['conversations']:
            #print(i[1])
            #if mesaj.lower().find("what is") == -1:
            #mesaj = mesaj.lower().replace("what is ", "")
            if i[0].lower().find(mesaj.lower()) != -1 or mesaj.lower().find(i[0].lower()) == 0:
                l.append(i[1])
    if l == []:
        solu = xai_list['conversations'][random.randint(0, len(xai_list['conversations']))][1]
        return findvrc(solu)
    else:
        vrc = random.choice(l)
        sol = findvrc(vrc)
        return sol



