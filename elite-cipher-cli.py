import argparse,time,sys
from multiprocessing import Process
parser = argparse.ArgumentParser()
parser.add_argument('-e','--encipher',metavar='',help='Input String to Encipher')
parser.add_argument('-d','--decipher',metavar='',help='Input String to Decipher')
args = parser.parse_args()
encode_dict = {'a':'ð','b':'ð','c':'ð','d':'ð','e':'ð','f':'â','g':'âïļ','h':'ð','i':'â','j':'ðŠ','k':'ð','l':'âïļ','m':'ð','n':'ð','o':'ð','p':'ð','q':'ð','r':'ðĪ','s':'ð','t':'ð§','u':'ð','v':'ðĪģ','w':'ðĪ','x':'ðĪ','y':'ðĪ','z':'ðĪ',' ':' ',':':'ð§ ','/':'ðĶū','.':'ðĪ','0':'ðĨ·','1':'ðĪš','2':'ðĐ','3':'ð','4':'ðĨ―','5':'ð','6':'ðķ','7':'ðą','8':'ð­','9':'ðđ'}
decode_dict  =  dict([item[::-1]for item in encode_dict.items()])
class EliteCipher(object):
    def __init__(self,encode,decode):
        self.encode = encode
        self.decode = decode
    def banner(self):
        print("""\033[1;31;40m

                           ââââŽ  âŽââŽââââ  ââââŽââââŽ âŽââââŽââ
                           ââĢ â  â â ââĪââââ  âââââââĪââĪ ââŽâ
                           ââââīâââī âī âââ  ââââīâī  âī âīââââīââ
\033[1;31;40m
        âââĶââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââĶââ
          â       \033[1;37;40m Github: https://github.com/FonderElite | Droid  \033[1;31;40m   â
          â           \033[1;37;40m       Join My Discord Server!                 \033[1;31;40m â
          â            \033[1;37;40m   https://discord.gg/rcpBF88vGQ              \033[1;31;40m â
          âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
 \033[1;37;40m
         """)
    def encipher(self) -> str:
        arr = []
        try:
            output = ''
            for i in str(self.encode).lower():
                arr.append(encode_dict[i])
            return ''.join(arr)
        except Exception as err:
            pass
    def decipher(self) -> str:
        arr = []
        try:
            for i in str(self.decode).lower():
                arr.append(decode_dict[i])
            return ''.join(arr)
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
