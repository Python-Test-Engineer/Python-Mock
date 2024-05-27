""" Based on https://medium.com/@cini01/how-to-patch-the-monkey-right-243898b6715a

I have extracted code and imported it into my own module. for demonstration purposes
"""

import sys
from itertools import dropwhile
import mymodule
from pyboxen import boxen
from rich.console import Console

console = Console()
globals()["mymodule"]
print("\n")

print("===== locals() =====")
console.print(locals())
print("\n")

print('===== globals()["mymodule"] =====')
console.print(globals()["mymodule"])
print("\n")

print("===== globals() =====")
console.print(globals())
print("\n")

# print("===== sys.modules =====")
# console.print(sys.modules)
# print("\n")

print(
    boxen(
        str(mymodule.__dict__["I"]),
        title='mymodule.__dict__["I"]',
        subtitle="mymodule.__dict__['I']",
        subtitle_alignment="left",
        color="red",
        padding=1,
    )
)
print(
    boxen(
        str(mymodule.__dict__["reduce"]),
        title='mymodule.__dict__["reduce"]',
        subtitle="=== reduce ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)

output = mymodule.I.__dict__["dropwhile"]
print(
    boxen(
        str(output),
        title="=== mymodule.I.__dict__['dropwhile'] ===",
        subtitle="=== mymodule.I.__dict__['dropwhile'] ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)
print(
    boxen(
        str(mymodule.__dict__["Path"]),
        title="=== Path ===",
        subtitle="=== Path ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)
my_list = (1, 2, 3, 4, 5)
# ===================== dropwhile ===============================

console.print(list(mymodule.I.dropwhile(lambda x: x < 3, my_list)))
# this
setattr(
    getattr(mymodule, "I"),
    "dropwhile",
    lambda my_filter, my_list: "dropwhile replaced with patched",
)  # dropwhile needs two arguments hence f,c

# or this:
print("Patching dropwhile")
mymodule.I.__dict__["dropwhile"] = (
    lambda my_filter, my_list: "dropwhile replaced with patched"
)
output = list(mymodule.I.dropwhile(lambda x: x < 3, my_list))
print(
    boxen(
        str(output),
        title="=== patched dropwhile ===",
        subtitle="=== patched dropwhile ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)
console.print(mymodule.I.dropwhile(lambda x: x < 3, my_list))

# was dropwhile replaced with patched?
# was dropwhile called with 2 arguments?


# what is blast radius?

from itertools import dropwhile

print("Reimporting dropwhile and run...")
output = list(mymodule.I.dropwhile(lambda x: x < 3, my_list))
print(
    boxen(
        str(output),
        title="=== reimported but cache patched  used for dropwhile ===",
        subtitle="=== reimported but cache patched used for dropwhile ===",
        subtitle_alignment="left",
        color="green",
        padding=1,
    )
)


# console.print("type sys.modules:")
# for n, m in sys.modules.items():
#     console.print((n, "==>", m))


console.print('mymodule.__dict__["reduce"]', mymodule.__dict__["reduce"])


output = mymodule.reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5])
print("\n")
print(
    boxen(
        str(output),
        title="=== reduce ===",
        subtitle="=== reduce ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)
print("Patching reduce...")
setattr(mymodule, "reduce", lambda a, c: "reduce replace with patched")

print("\n")
output = mymodule.reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5])
print(
    boxen(
        str(output),
        title="=== patched reduce ===",
        subtitle="=== patched reduce ===",
        subtitle_alignment="left",
        color="red",
        padding=1,
    )
)

from functools import reduce


print("\n")
output = reduce(lambda acc, cur: acc + cur, [1, 2, 3, 4, 5])
print(
    boxen(
        str(output),
        title="=== reverse reduce monkeypatch ===",
        subtitle="=== reverse reducemonkeypatch ===",
        subtitle_alignment="left",
        color="yellow",
        padding=1,
    )
)
# This time the import from the module cache brought back the original functionality. Why is that? It’s because the imported objects (variables, classes, functions) are not stored as references to the original module. Instead, they are directly added to the current namespace. In our example we have only modified mymodule.reduce(), but this change was not reflected back to the module cache, hence we were able to (re-)import the original reduce() function from functools in the module cache.


# So far we have patched objects that we have imported into our own module. “Is it even possible to patch the cache directly?”, you might be tempted to ask. Absolutely! Remember, it’s just a plain dictionary!


import pathlib as pl

print("Patching Path.home()")
setattr(getattr(sys.modules["pathlib"], "Path"), "home", lambda: "Home now: <new_dir>")
# console.print(pl.Path.home())
print("\n")
output = pl.Path.home()
print(
    boxen(
        str(output),
        title="=== pl.Path.home() ===",
        subtitle="=== pl.Path.home() ===",
        subtitle_alignment="left",
        color="blue",
        padding=1,
    )
)

# Summary
# sys.module is Python’s runtime module cache stored in memory
# modules are cached in sys.module, which is a mutable, plain dictionary mapping names to module objects
# importing entire modules creates references to the module cache in the local namespace
# objects of modules (variables, functions, classes) are directly added to the current namespace when imported
# local and global namespaces as well as the module cache are also just mutable plain dictionaries
