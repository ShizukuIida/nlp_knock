import json

if __name__ == "__main__":
   with open("../data/jawiki-country.json", 'r') as f:
      for line in f:
         article = json.loads(line)
         if article['title'] == 'イギリス':
            print(article['text'])
            break

   with open("../data/wiki_england.txt", "w") as f:
      f.write(article['text'])
