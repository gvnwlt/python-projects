# saving to json
try:
    import simplejson as json
except:
    import json

book = {}
book['title'] = 'Light Science and Magic: An Introduction to Photographic Lighting, Kindle Edition'
book['tags'] = ('Photography', 'Kindle', 'Light')
book['published'] = True
book['comment_link'] = None
book['id'] = 1024

with open('ebook.json',  'w') as f:
	json.dump(book, f)

# pickle example 
import cPickle as Pickle 

with open("mymodel.pkl", "wb") as mymodelfile:
  Pickle.dump(model, mymodelfile)

with open("mymodel.pkl", "rb") as mymodelfile:
  thenewmodel = Pickle.load(mymodelfile)

thenewmodel.predict(newvector)


# real-world life cycle machine learning production 
  1. evaluate 
  2. deploy
  3. manage
  4. monitor 
