class SafeStorage:
    __data = None

    def get(self):
        return self.__data

    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

#To execute this code, please run these on the terminal: 
# /absolute-path/nbi-hendelsakademin-python/python06/safe_storage.py

'''
Explanation:

- SafeStorage has a private variable __data.
- put() saves data.
- get() returns the stored data.

---------------
Store "Anakonda"
Get it → x = "Anakonda"
Store "Boaorm"
Get it → y = "Boaorm"

Print both ==> Anakonda Boaorm
'''