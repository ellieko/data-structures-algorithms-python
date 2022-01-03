class TreeNode:
    def __init__(self, name, designation=''):
        self.data = {'name': name, 'designation': designation}
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data['name'])
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_ex1(self, option):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if option == "both":
            print(prefix + self.data['name'] +
                  " (" + self.data['designation'] + ")")
        elif option in ("name", "designation"):
            print(prefix + self.data[option])
        else:
            raise Exception("Invalid option")
        if self.children:
            for child in self.children:
                child.print_tree_ex1(option)

    def print_tree_ex2(self, level):
        lv = self.get_level()
        spaces = ' ' * lv * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data['name'])
        if level == lv:
            return
        else:
            if self.children:
                for child in self.children:
                    child.print_tree_ex2(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

# exercise prob 1) company hierarchy tree


def build_management_tree():
    ceo = TreeNode("Nilupul", "CEO")
    cto = TreeNode("Chinmay", "CTO")
    hr = TreeNode("Gels", "HR Head")
    ceo.add_child(cto)
    ceo.add_child(hr)

    infra = TreeNode("Vishwa", "Infrastructure Head")
    cto.add_child(infra)
    cto.add_child(TreeNode("Aamir", "Application Head"))
    infra.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra.add_child(TreeNode("Abhijit", "App Manager"))

    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))

    return ceo

# exercise prob 2) location tree


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))
    ca = TreeNode("California")
    ca.add_child(TreeNode("San Francisco"))
    ca.add_child(TreeNode("Mountain View"))
    ca.add_child(TreeNode("Palo Alto"))
    usa.add_child(nj)
    usa.add_child(ca)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    build_product_tree()

    print("\n- - - - - - - - - - - - - - - - -\n")

    # exercise prob 1)
    # extend data and print tree with options, name, designation, both
    root_node_1 = build_management_tree()
    root_node_1.print_tree_ex1("name")  # prints only name hierarchy
    # prints only designation hierarchy
    root_node_1.print_tree_ex1("designation")
    # prints both (name and designation) hierarchy
    root_node_1.print_tree_ex1("both")

    print("\n- - - - - - - - - - - - - - - - -\n")

    # exercise prob 2)
    # build location tree and print tree with tree level
    root_node_2 = build_location_tree()
    root_node_2.print_tree_ex2(2)
