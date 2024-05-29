# import foo to see where the refernce to it is stored...
from mymodule import foo as imported_foo_from_mymodule
from rich.console import Console

console = Console()


def real_full_name(first, last):
    return f"[green]real_full_name()[/] being used => {first} {last}"


def fake_full_name(first, last):
    return f"[red]FAKE_FULL_NAME()[/] being used => {first} {last}"


hex_id_real = hex(id(real_full_name))[-3:]
hex_id_fake = hex(id(fake_full_name))[-3:]
console.print("\n")
console.print(f"id of real_full_name: [green]{hex_id_real}[/]")
# console.pring outputs differently
console.print(real_full_name("John", "Doe"))
console.print(f"id of fake_full_name: [red]{hex_id_fake}[/]")
console.print(fake_full_name("FakeFirst", "FakeLast "))
console.print("--------------------")

# monkey patch
real_full_name = fake_full_name
console.print("Monkeypatching...")
console.print(f"id of real_full_name is now: [red]{hex(id(real_full_name))[-3:]}[/]")
# now it's fake - real_full_name("FakeFirst", "FakeLast"))


console.print(
    "Calling (patched) [green]real_full_name('Jane', 'Allen')[/] and we get:",
    real_full_name("Jane", "Allen"),
)
console.print("\n")

console.print(globals())
imported_foo_from_mymodule()

console.print("Monkeypatching imported_foo_from_mymodule\n")


def patched_imported_foo_from_mymodule():
    console.print("Patched: [red]imported_foo_from_mymodule foo() output...[/red]\n")


imported_foo_from_mymodule = patched_imported_foo_from_mymodule

patched_imported_foo_from_mymodule()
