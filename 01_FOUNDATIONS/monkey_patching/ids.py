from pyboxen import boxen

from rich.console import Console

console = Console()


def real_full_name(first, last):
    return f"[green]real_full_name()[/] being used => {first} {last}"


def FAKE_FULL_NAME(first, last):
    return f"[red]FAKE_FULL_NAME()[/] being used => {first} {last}"


console.print(globals())
hex_id_real = hex(id(real_full_name))[-3:]
hex_id_fake = hex(id(FAKE_FULL_NAME))[-3:]
console.print("\n")
console.print(f"id of real_full_name: [green]{hex_id_real}[/]")
# console.pring outputs differently
console.print(real_full_name("John", "Doe"))
console.print(f"id of fake_full_name: [red]{hex_id_fake}[/]")
console.print(FAKE_FULL_NAME("FakeFirst", "FakeLast "))
console.print("\n--------------------\n")

# monkey patch
real_full_name = FAKE_FULL_NAME
console.print("[blue bold]Monkeypatching...[/]\n")
console.print(f"real_full_name now points to: [red]{hex(id(real_full_name))[-3:]}[/]")


console.print(
    "\nCalling (patched) [green]real_full_name('Jane', 'Allen')[/] =>  \n\n\t uses FAKE_FULL_NAME():",
    real_full_name("Jane", "Allen"),
)
console.print("\n")
