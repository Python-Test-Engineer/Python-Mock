# https://medium.com/@cini01/how-to-patch-the-monkey-right-243898b6715a

- ### sys.module is Python’s runtime module cache stored in memory
-  ### modules are cached in sys.module, which is a mutable, plain dictionary mapping names to module objects
-  ### importing entire modules creates references to the module cache in the local namespace
-  ### objects of modules (variables, functions, classes) are directly added to the current namespace when imported
-  ### local and global namespaces as well as the module cache are also just mutable plain dictionaries