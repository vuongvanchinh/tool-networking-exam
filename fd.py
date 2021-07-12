from models import Attribute, DF
from utils import bao_dong, check_keys, create_list_attr, create_list_dfs, is_wrap, is_equivalent_dfs

# Tìm bao đóng neu bao dong = tat ca thuoc tinh ->> key
attrs = create_list_attr('EB')
s = 'AB-> C,D-> EG,C-> A,BE-> C, BC-> D, CG-> BD,ACD-> B, CE -> AG'
dfs = create_list_dfs(s)
print("Attrs: ", attrs)
print("Bao dong: ", bao_dong(attrs ,dfs))

# tim key trong cac key cho truoc
consider_keys = ['CA', 'BC', 'AB', 'CD', 'CG', 'EB']
keys = check_keys(consider_keys, dfs, 'ABCDEG')
print("Keys: ", keys)


# tuong duong
g = 'A->C, AC->D, E->AD, E->B'
h = 'A -> D, C -> D, E -> A'
i = 'A -> EB, C -> D, E -> A'
k = 'A->CD, E->AB'

dfs1 = create_list_dfs(k)
dfs2 = create_list_dfs(g)
print("Equivalent: ", is_equivalent_dfs( dfs1, dfs2))
