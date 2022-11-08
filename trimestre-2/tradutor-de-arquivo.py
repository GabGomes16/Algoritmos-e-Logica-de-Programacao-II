from googletrans import Translator
from datetime import datetime

data = open('StolenDance.txt', 'r')
content = data.read()
data.close()
_tranlate = Translator()
translated = _tranlate.translate(content, dest= 'pt')
new_data = open('StolenDanceTraducao', 'w')
new_data.write(translated.text)
new_data.close()
modified_time = datetime.now()
translated = _tranlate.translate(modified_time.strftime('%A'),dest='pt')
modified = modified_time.strftime(f"\n\nÚltima modificação: {translated.text}, %d/%m/%Y às %H:%M")
new_data = open('StolenDanceTraducao', 'a')
new_data.write(modified)
new_data.close()