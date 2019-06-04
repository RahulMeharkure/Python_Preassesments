import json

if __name__=='__main__':
  with open('C:/Users/Rahul Meharkure/.PyCharmEdu2019.1/config/scratches/my.json') as f:
    dat = json.load(f)
  print(dat['Records'][0]['s3']['bucket']['arn'])

