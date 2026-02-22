# 1a Create class
class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []

    # 1b + 1d + 1f: print_info method
    def print_info(self):
        print(f"In {self.__name} there are {self.__population} million inhabitants.")

        if self.__area is not None:
            print(f"Area: {self.__area} square km")

        if self.__languages:
            print("Official languages:")
            for lang in self.__languages:
                print(lang)

    # 1e add_language method
    def add_language(self, language):
        self.__languages.append(language)


# 1a Create objects
iceland = Country("Iceland", 0.4)
denmark = Country("Denmark", 6.0)
sweden = Country("Sweden", 10.5, 450000)

# 1e + example usage
finland = Country("Finland", 5.6, 338000)
finland.add_language("Finnish")
finland.add_language("Swedish")

finland.print_info()

'''
Output: 
In Finland there are 5.6 million inhabitants.
Area: 338000 square km
Official languages:
Finnish
Swedish
'''