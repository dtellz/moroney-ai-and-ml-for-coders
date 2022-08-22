import urllib.request
import zipfile

url = 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/hores-or-human.zip'

fileName = 'hores-or-human.zip'
trainingDirectory = 'horse-or-human/training/'
urllib.request.urlretrieve(url, fileName)

zipRef = zipfile.ZipFile(fileName, 'r')
zipRef.extractall(trainingDirectory)
zipRef.close()
