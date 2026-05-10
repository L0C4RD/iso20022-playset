from . import base_types
from ._Max100KBinary import Max100KBinary
from ._Max9999HexBinaryText import Max9999HexBinaryText

class EncryptedData2Choice(base_types._BaseFieldType):

	__slots__ = ["_HexBinry", "_Binry"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if type(value) != base_types.auto else self.make_default("Binry")

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = None

	@property
	def HexBinry(self):
		return self._HexBinry

	@HexBinry.setter
	def HexBinry(self, value):
		self._HexBinry = value if type(value) != base_types.auto else self.make_default("HexBinry")

	@HexBinry.deleter
	def HexBinry(self):
		del self._HexBinry
		self._HexBinry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max100KBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HexBinry', type=Max9999HexBinaryText, min=0, max=1, mutex_group=1, array=False),
	))

