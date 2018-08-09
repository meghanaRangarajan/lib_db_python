import libcir


name = "tv.db"
db_handle = libcir.init_library(name)
r_id = int(input("enter r_id : "))
remote = libcir.load_remote(r_id,db_handle)
libcir.print_remote(r_id,remote)
key_codes = libcir.key_codes()
protocol = libcir.protocol_ids()
key_id = key_codes.KEY_POWER
code = libcir.get_code(key_id,remote)
libcir.print_key_and_code(key_id,remote)

libcir.send_code(key_id,remote)

print(protocol.PROTOCOL_MCE)