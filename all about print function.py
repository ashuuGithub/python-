print("hello ... I'm a print message\n")

print() # all attributes are optional
# 1  sep: str | None = " ", 
# 2  end: str | None = "\, 
# 3 file: _SupportsWriteAndFlush[str] | None = None,  -- in case of file handling
# 4 flush: bool) -> None


print("vipul","nisha","vinay") #vipul nisha vinay
print("vipul","nisha","vinay",sep="-") #vipul-nisha-vinay
print("vipul","nisha","vinay",sep="/") #vipul/nisha/vinay
print("vipul","nisha","vinay",file=open("print.txt","w")) # it will write the result = "vipul nisha vinay" in print.txt file in same directory

print("vipul","nisha","vinay",file=open("print.txt","w"),flush=True) # it will write the result = "vipul nisha vinay" in print.txt file in same directory and flush the buffer
