import urllib.request
import zipfile

url = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip'

fileName = 'validation-horse-or-human.zip'
validationDirectory = 'horse-or-human/validation/'
urllib.request.urlretrieve(url, fileName)

zipRef = zipfile.ZipFile(fileName, 'r')
zipRef.extractall(validationDirectory)
zipRef.close()