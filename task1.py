# TODO решить с помощью list comprehension и распечатать его
import pprint

spisok = [{'bin':bin(n), 'dec':n, 'hex':hex(n), 'oct':oct(n)} for n in range(16)]
pprint.pp(spisok)