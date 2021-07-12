class Attribute:
    def __init__(self, name:str):
        self.name = name.upper()
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    
    def __eq__(self, obj):
        return self.name == obj.name
    def __hash__(self) -> int:
        return hash(self.name)

class DF:
    def __init__(self, string=''):
        self.left = []
        self.right = []
        string = string.strip(' ').strip('}').strip('{').strip(',')
        
        if string and 0 < string.find('->') < len(string) -1:
            data = string.split('->')
            for char in data[0].strip():
                self.left.append(Attribute(char))
            for char in data[1].strip():
                self.right.append(Attribute(char))
    
    def __str__(self):
        return f'{"".join(map(str, self.left))} -> {"".join(map(str, self.right))}'

    def __repr__(self):
        return f'{"".join(map(str, self.left))} -> {"".join(map(str, self.right))}'



