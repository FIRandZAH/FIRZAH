_B=False
_A=None
import re,struct,binascii
_b85alphabet=b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'
_b85chars=_A
_b85chars2=_A
_b85dec=_A
bytes_types=bytes,bytearray
def _bytes_from_decode_data(s):
	if isinstance(s,str):
		try:return s.encode('ascii')
		except UnicodeEncodeError:raise ValueError('string argument should contain only ASCII characters')
	if isinstance(s,bytes_types):return s
	try:return memoryview(s).tobytes()
	except TypeError:raise TypeError('argument should be a bytes-like object or ASCII string, not %r'%s.__class__.__name__)from _A
def _85encode(b,chars,chars2,pad=_B,foldnuls=_B,foldspaces=_B):
	D=chars2;C=chars
	if not isinstance(b,bytes_types):b=memoryview(b).tobytes()
	B=-len(b)%4
	if B:b=b+b'\x00'*B
	E=struct.Struct('!%dI'%(len(b)//4)).unpack(b);A=[b'z'if foldnuls and not A else b'y'if foldspaces and A==538976288 else D[A//614125]+D[A//85%7225]+C[A%85]for A in E]
	if B and not pad:
		if A[-1]==b'z':A[-1]=C[0]*5
		A[-1]=A[-1][:-B]
	return b''.join(A)
def firzah_enc(b,pad=_B):
	global _b85chars,_b85chars2
	if _b85chars2 is _A:_b85chars=[bytes((A,))for A in _b85alphabet];_b85chars2=[A+B for A in _b85chars for B in _b85chars]
	return _85encode(b,_b85chars,_b85chars2,pad)
def firzah_dec(b):
	global _b85dec
	if _b85dec is _A:
		_b85dec=[_A]*256
		for(A,B)in enumerate(_b85alphabet):_b85dec[B]=A
	b=_bytes_from_decode_data(b);C=-len(b)%5;b=b+b'~'*C;F=[];H=struct.Struct('!I').pack
	for A in range(0,len(b),5):
		G=b[A:A+5];D=0
		try:
			for B in G:D=D*85+_b85dec[B]
		except TypeError:
			for(I,B)in enumerate(G):
				if _b85dec[B]is _A:raise ValueError('bad base85 character at position %d'%(A+I))from _A
			raise
		try:F.append(H(D))
		except struct.error:raise ValueError('base85 overflow in hunk starting at byte %d'%A)from _A
	E=b''.join(F)
	if C:E=E[:-C]
	return E