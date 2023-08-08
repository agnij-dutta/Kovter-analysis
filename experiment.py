from regipy.registry import RegistryHive

reg = RegistryHive("./NTUSER.dat")
print(reg.get_key("SOFTWARE").get_subkey("").get_value(""))