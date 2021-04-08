
import yaml
import random

from pathlib import Path

my_path = Path(__file__).resolve()  # resolve to get rid of any symlinks
config_path = my_path.parent/'srpskixai.yml'

with config_path.open(encoding="utf-8") as config_file:
    config = yaml.safe_load(config_file)

def findvrc(vrc):
    f = vrc.find("http")
    if f == -1:
        return vrc
    else:
        vrc = vrc.replace("(", "<a href=\'")
        vrc = vrc.replace(")", "\' target='_blank'>ovde")
        print(vrc)
        return vrc

def convorbireXAI(mesaj):
    l=[]
    with config_path.open(encoding="utf-8") as config_file:
        xai_list = yaml.safe_load(config_file)
        for i in xai_list['conversations']:
            if i[0].lower().find(mesaj.lower()) != -1 or mesaj.lower().find(i[0].lower()) == 0:
                l.append(i[1])
    if l == []:
        solu = xai_list['conversations'][random.randint(0, len(xai_list['conversations']))][1]
        return findvrc(solu)
    else:
        vrc = random.choice(l)
        sol = findvrc(vrc)
        return sol

