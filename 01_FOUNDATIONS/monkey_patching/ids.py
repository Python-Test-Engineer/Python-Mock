def real_full_name(first, last):
    return f"real_full_name(): {first} {last}"


def fake_full_name(first, last):
    return f"fake_full_name(): {first} {last}"


hex_id_real = hex(id(real_full_name))[-6:]
hex_id_fake = hex(id(fake_full_name))[-6:]

print(f"id of real_full_name: {hex_id_real}")
print(real_full_name("John", "Doe"))
print(f"id of fake_full_name: {hex_id_fake}")
print(fake_full_name("FakeFirst", "FakeLast "))
print("--------------------")

# monkey patch
real_full_name = fake_full_name
print(f"id of real_full_name is now: {hex(id(real_full_name))[-6:]}")
# now it's fake - real_full_name("Sally", "Jane"))
print(
    f"Calling real_full_name using {hex(id(real_full_name))[-6:]} but hex_fake_id is {hex_id_fake}: \n\t{real_full_name('MonkeyPatchedFirst', 'MonkeyPatchedLast')}"
)
