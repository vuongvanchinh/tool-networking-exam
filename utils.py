from models import DF, Attribute
def create_list_dfs(s):
    """ TẬP PHỤ THUỘC HÀM"""
    strings = s.strip().split(',')
    rs = [DF(string) for string in strings]
    return rs

def create_list_attr(s:str):
    return [Attribute(char) for char in s.strip(' ')]

def in_(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

def bao_dong(attrs, fds):
    rs = [attr for attr in attrs]
    
    add = True
    while add:
        add = False
        for fd in fds:
            if in_(fd.left, rs):
                for attr in fd.right:
                    if attr not in rs:
                        rs.append(attr)
                        add = True
    rs.sort(key=lambda x:x.name)
    return rs
    
          

def is_wrap(a, b):
    """return true if a wrap b else false"""
    for df in b:
        wrap = bao_dong(df.left, a)
        if not in_(df.right, wrap):
            print("is not subset", df)
            print(wrap)
            return False
    return True

def is_equivalent_dfs(a, b):
    """ Kiem tra hai tập phụ thuộc hàm có tương đương nhau không"""
    return is_wrap(a, b) and is_wrap(b, a)

def check_keys(arr_attrs, dfs, all_attrs:str):
    rs = []
    for attrs in arr_attrs:
        if len(bao_dong(create_list_attr(attrs), dfs)) == len(all_attrs.strip(' ')):
            rs.append(attrs)
    return rs
