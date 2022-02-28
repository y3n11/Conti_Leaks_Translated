import re
import json
from deep_translator import GoogleTranslator
import os


def translate_file(fname):


	with open(fname, 'r') as fpr :

		file_content = fpr.read()
		splited = re.compile("(?:^.*$\n?){1,6}",re.M).findall(file_content)


		for _entry in splited :

			try:

				_json = json.loads(_entry)

				translated_entry = '----\nTs: {}\nFrom: {}\nTo: {}\nBody: {}\n'.format(_json['ts'], _json['from'], _json['to'], GoogleTranslator(source='auto', target='en').translate(_json['body']))
				
				with open('translated.txt', 'a') as out:

					out.write(translated_entry)


			except Exception as e :

				print(str(e))




directory = 'original'


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        translate_file(f)