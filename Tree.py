from string_manipulations import clean_data, find
from anytree.exporter import DictExporter
from utilities import remove_duplicates

class Tree:
    def __init__(self):
        self.root = {}
        self.root["name"] = "root"
        self.root["dict"] = {}

    def add_sentence(self, node, sentence, source, dict={}):
        if sentence == '\n' or sentence == '':
            leaf = {}
            leaf["name"] = "leaf"
            leaf["dict"] = {}
            leaf["src"] = source
            node["dict"]["leaf"] = leaf
            return
        else:
            if str(sentence[0]) in node["dict"]:
                self.add_sentence(node["dict"][sentence[0]], sentence[1:], source, {})
                return

            new_Node = {}
            new_Node["name"] = sentence[0]
            new_Node["dict"] = {}
            new_Node["src"] = source
            node["dict"][str(sentence[0])] = new_Node
            self.add_sentence(new_Node, sentence[1:], source, {})

    def find_best_match(self, node, sentence):
        ret = []
        if node["name"] == "leaf":
            ret.append(node["src"])
            return ret
        if sentence == "":
            return self.find_max_in_point(node, [])

        if len(ret) < 5:
            if str(sentence[0]) in node["dict"]:
                result = self.find_best_match(node["dict"][str(sentence[0])], sentence[1:])
                ret += result

        if len(ret) <= 5:
            for child in node["dict"]:
                if len(ret) < 5:
                    ret += self.find_best_match(node["dict"][child], sentence[1:])

        if len(ret) < 5:
            for child in node["dict"]:
                if len(ret) < 5:
                    ret += self.find_best_match(node["dict"][child], sentence)

        if len(ret) < 5:
            ret += self.find_best_match(node, sentence[1:])

        ret = remove_duplicates(ret)

        return ret[:5]

    def find_max_in_point(self, node, lst=[]):
        for child in node["dict"]:
            if node["dict"][child]["name"] == "leaf":
                lst.append(node["dict"][child]["src"])
            else:
                lst += (self.find_max_in_point(node["dict"][child], lst=[]))
        return lst

    def add_lines_to_tree(self, path, lines):

        for line in lines:
            tpl = (path, line)
            if line != "\n" and not line.startswith(" "):
                line = clean_data(line[15:])
                self.add_sentence(self.root, line, tpl)
                lst = find(line, ' ')
                for index in lst:
                    self.add_sentence(self.root, line[index + 1:], tpl)



