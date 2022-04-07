import argparse,time,sys
from multiprocessing import Process
parser = argparse.ArgumentParser()
parser.add_argument('-e','--encipher',metavar='',help='Input String to Encipher')
parser.add_argument('-d','--decipher',metavar='',help='Input String to Decipher')
args = parser.parse_args()
encode_dict = {'a':'0','b':')','c':'@','d':'*','e':'#','f':'o','g':'r','h':'$','i':'v','j':':','k':';','l':'`','m':'~','n':'?','o':'z','p':'s','q':'[','r':']','s':'&','t':'!','u':'<','v':'>','w':'_','x':'=','y':'+','z':'^',' ':' ',}
decode_dict  =  dict([item[::-1]for item in encode_dict.items()])
class EliteCipher(object):
    def __init__(self,encode,decode):
        self.encode = encode
        self.decode = decode
    def banner(self):
        print("""\033[1;31;40m

                            ╔═╗┬  ┬┌┬┐┌─┐  ╔═╗┬┌─┐┬ ┬┌─┐┬─┐
                            ║╣ │  │ │ ├┤───║  │├─┘├─┤├┤ ├┬┘
                            ╚═╝┴─┘┴ ┴ └─┘  ╚═╝┴┴  ┴ ┴└─┘┴└─
\033[1;31;40m
        ══╦═══════════════════════════════════════════════════════════╦══
          ║       \033[1;37;40m Github: https://github.com/FonderElite | Droid  \033[1;31;40m   ║
          ║           \033[1;37;40m       Join My Discord Server!                 \033[1;31;40m ║
          ║            \033[1;37;40m   https://discord.gg/rcpBF88vGQ              \033[1;31;40m ║
          ╚═══════════════════════════════════════════════════════════╝
 \033[1;37;40m
         """)
    def encipher(self) -> str:
            output = ''
            for i in str(self.encode):
                get_items = encode_dict.get(i)
                output+=str(get_items)
            print(f"[\033[1;32;40m+\033[1;37;40m]Enciphered Text: {output}")
    def decipher(self) -> str:
        arr = []
        try:
            for i in str(self.decode):
                arr.append(decode_dict[i])
            print("[\033[1;32;40m+\033[1;37;40m]Deciphered Text: "+ ''.join(arr))
        except Exception as err:
            pass
if __name__ == "__main__":
    call_class = EliteCipher(args.encipher,args.decipher)
    banner = Process(target=call_class.banner)
    encode_f = Process(target=call_class.encipher)
    decode_f = Process(target=call_class.decipher)
    banner.start()
    banner.join()
    encode_f.start()
    encode_f.join()
    decode_f.start()
    decode_f.join()
