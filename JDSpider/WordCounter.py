import io
import re

class Counter:
    def __init__(self,path):
        self.mapping=dict()
        with io.open(path,encoding="gbk") as f:
            data =f.read()
            words=[s.lower() for s in re.findall("\w+",data)]
            for word in words:
                self.mapping[word]=self.mapping.get(word,0)+1

    def most_common(self,n):
        assert n>0,"n should be large than 0"
        return sorted(self.mapping.items(),key=lambda item:item[1],reverse=True)[:n]

if __name__=='__main__':
    most_common_5=Counter("comment_iphone8_.txt").most_common(15)
    for item in most_common_5:
        print(item)
        
