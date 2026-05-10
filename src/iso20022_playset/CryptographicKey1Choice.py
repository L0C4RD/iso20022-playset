from . import base_types
from .HexBinaryText import HexBinaryText
from .SHA256SignatureText import SHA256SignatureText

class CryptographicKey1Choice(base_types._BaseFieldType):

	__slots__ = ["_ILPV4", "_Sgntr"]
	@property
	def ILPV4(self):
		return self._ILPV4

	@ILPV4.setter
	def ILPV4(self, value):
		self._ILPV4 = value if type(value) != base_types.auto else self.make_default("ILPV4")

	@ILPV4.deleter
	def ILPV4(self):
		del self._ILPV4
		self._ILPV4 = None

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != base_types.auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ILPV4', type=HexBinaryText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sgntr', type=SHA256SignatureText, min=0, max=1, mutex_group=1, array=False),
	))

