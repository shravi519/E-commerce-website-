import csv
import math
def load_csv(filename):
    lines=csv.reader(open(filename,"r"))
    datasets=list(lines)
    header=datasets.pop(0)
    return datasets,header
class Node:
    def __init__(self,attribute):
        self.attribute=attribute
        self.children=[]
        self.answer=""
def subtable(data,col,delete):
    dic={}
    coldata=[row[col] for row in data]
    attr=list(set(coldata))
    for k in attr:
        dic[k]=[]
    for y in range(len(data)):
        key=data[y][col]
        if delete:
            del data[y][col]
        dic[key].append(data[y])
    return attr,dic
def entropy(S):
    attr=list(set(S))
    if len(attr)==1:
        return 0
    count=[0,0]
    for i in range(2):
        count[i]=sum([1 for x in S if attr[i]==x])/(len(S)*1.0)
    sums=0
    for cnt in count:
        sums+=-1*cnt*math.log(cnt,2)
    return sums
def computegain(data,col):
    attrval,dic=subtable(data,col,delete=False)
    total_entropy=entropy([row[-1] for row in data])
    for x in range(len(attrval)):
        ratio=len(dic[attrval[x]])/(len(data)*1.0)
        entro=entropy([row[-1] for row in dic[attrval[x]]])
        total_entropy-=ratio*entro
    return total_entropy
def build_tree(data,features):
    lastcol=[row[-1] for row in data]
    if len(set(lastcol))==1:
        node=Node("")
        node.answer=lastcol[0]
        return node
    n=len(data[0])-1
    gain=[computegain(data,col) for col in range(n)]
    split=gain.index(max(gain))
    node=Node(features[split])
    fea=features[:split]+features[split+1:]
    attr,dic=subtable(data,split,delete=True)
    for x in range(len(attr)):
        child=build_tree(dic[attr[x]],fea)
        node.children.append((attr[x],child))
    return node
def print_tree(node,level):
    if node.answer!="":
        print("   "*level,node.answer)
        return
    print("   "*level,node.attribute)
    for value,n in node.children:
        print("   "*(level+1),value)
        print_tree(n,level+2)
def classify(node,x_test,features):
    if node.answer!="":
        print(node.answer)
        return
    pos=features.index(node.attribute)
    for value,n in node.children:
        if x_test[pos]==value:
            classify(n,x_test,features)
dataset,features=load_csv("C:\\Users\\dell1\\OneDrive\\Desktop\\external aiml\\tennisdata (2).csv")
node=build_tree(dataset,features)
print("decision tree using ID3 algorithm")
print_tree(node,0)
testdata,features=load_csv("C:\\Users\\dell1\\OneDrive\\Desktop\\external aiml\\test.csv")
for x_test in testdata:
    print("test instances are:",x_test)
    print("predicted label:",end="  ")
    classify(node,x_test,features)