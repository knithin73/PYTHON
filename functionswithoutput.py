def format_name(f_name,l_name):
    f_namew=f_name.title()
    l_namew=l_name.title()
    
    return f"{f_namew} {l_namew}"
a="nitHiN"
b="niTro"
c=format_name(a,b)
print(c)