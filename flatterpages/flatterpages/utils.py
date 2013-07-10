from os import path, mkdir


def write_to_file(instance, filetype):
	if filetype == 'html':
		extension = instance.main_content
		filedir = 'templates/pagetemplates/'
	elif filetype == 'css':
		extension = instance.css
		filedir = 'templates/css/'

	if not path.isdir(filedir):
		mkdir(filedir)
	f = open(filedir + str(instance.title).lower() + '.' + filetype, 'w')
	f.write(extension)
	f.close()

	return