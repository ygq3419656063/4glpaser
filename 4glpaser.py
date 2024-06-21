import copy

class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]

    def add_child(self,child):
        self.children.append(child)




def build_function_tree(code,outfile):
    root=Node("main") #假设根节点从main函数开始
    current_node =root
    indentation_stack=[root]  #用于跟踪当前缩进级别的函数节点

    line_ct=1
    new_line=[]
    new_text=[]

    for line in code:
        line=list(line)

        for index,char in enumerate(line):
            if char == "#":
                new_line=line[0:index]
                new_line.append('\n')
                break
            else:
                new_line=line


        new_text.append(new_line)



    for line in new_text:
        if len(line):
            if not (len(line) == 1 and line[0] == '\n'):
                for char in line:
                    outfile.write(char)



def process_file(input_file,out_file):
    try:
        # 打开输入文件和输出文件
        with open(input_file, 'r', encoding='utf-8') as infile,open(out_file,'w',encoding='utf-8') as outfile:
            lines=infile.readlines()
            build_function_tree(lines,outfile)


    except FileNotFoundError:
        print("指定的输入文件不存在，请检查文件路径。")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__=='__main__':
    process_file("aimi193.4gl","test.txt")







