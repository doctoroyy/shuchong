from datetime import datetime

if __name__ == '__main__':
   d = datetime.now() - datetime.strptime('2019-10-05 12:56:22', '%Y-%m-%d %H:%M:%S')
   print(d.seconds / 3600 > 5)
