import emoji
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print(emoji.emojize(':tada: FELIZ ANO NOVO!!! :tada:', use_aliases=True))
