from . import base_types
from ._Max15NumericText import Max15NumericText

class BinRange1(base_types._BaseFieldType):

	__slots__ = ["_HghrBin", "_LwrBin"]
	@property
	def HghrBin(self):
		return self._HghrBin

	@HghrBin.setter
	def HghrBin(self, value):
		self._HghrBin = value if type(value) != base_types.auto else self.make_default("HghrBin")

	@HghrBin.deleter
	def HghrBin(self):
		del self._HghrBin
		self._HghrBin = None

	@property
	def LwrBin(self):
		return self._LwrBin

	@LwrBin.setter
	def LwrBin(self, value):
		self._LwrBin = value if type(value) != base_types.auto else self.make_default("LwrBin")

	@LwrBin.deleter
	def LwrBin(self):
		del self._LwrBin
		self._LwrBin = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghrBin', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwrBin', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

