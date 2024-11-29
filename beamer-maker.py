import os
import re
l=os.listdir("F:/Documents/Youtube/Art/2024-11-15_Foundations")
filenames_for_beamer=os.listdir("F:/Documents/Youtube/Art/2024-11-15_Foundations")
w = open("beamer_slides.txt", "w")
names=[]

for i in range(len(l)):
    l[i] = l[i].replace(".jpg", "")  # Remove ".jpg"
    names.append(re.sub(r'[^a-zA-Z_]', '', l[i]))
    l[i] = re.sub("[^0-9]", "", l[i])  # Remove all non-numeric characters
    l[i] = int(l[i])
    
for i in range(len(names)):
    names[i]=names[i][1:]
    names[i]=names[i].replace("_"," ")    
    
dic1=dict(zip(l,names))
dic2=dict(zip(l,filenames_for_beamer))

dic1 = dict(sorted(dic1.items(), key=lambda item: item[0]))
dic2 = dict(sorted(dic2.items(), key=lambda item: item[0]))

latex_code="""

\\begin{frame}{%x}
\\begin{columns}[T]
    \\begin{column}{0.5\\textwidth}
        \\begin{figure}
            \\centering
            \\includegraphics[width=0.8\\linewidth]{FDN Art/%y}
        \\end{figure}
    \\end{column}

    \\begin{column}{0.5\\textwidth}
        \\begin{figure}
            \\centering
            \\begin{minipage}{0.45\\textwidth}
                \\centering
                \\includegraphics[width=0.8\\linewidth]{Other Sets/}
            \\end{minipage} \\hfill
            \\begin{minipage}{0.45\\textwidth}
                \\centering
                \\includegraphics[width=0.8\\linewidth]{Other Sets/}
            \\end{minipage}

            \\begin{minipage}{0.45\\textwidth}
                \\centering
                \\includegraphics[width=0.8\\linewidth]{Other Sets/}
            \\end{minipage} \\hfill
            \\begin{minipage}{0.45\\textwidth}
                \\centering
                \\includegraphics[width=0.8\\linewidth]{Other Sets/}
            \\end{minipage}
        \\end{figure}
    \\end{column}
\\end{columns}
\\end{frame}

"""

for key,val in dic2.items():
    if key < 134:
        latex_code1=latex_code
        latex_code1=latex_code1.replace("%x",str(dic1[key]))
        latex_code1=latex_code1.replace("%y",val)
        w.write(latex_code1)
    