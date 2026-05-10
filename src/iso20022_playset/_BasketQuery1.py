from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._Max52Text import Max52Text
from ._ISINOct2015Identifier import ISINOct2015Identifier

class BasketQuery1(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_Strr", "_Idr"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Strr(self):
		return self._Strr

	@Strr.setter
	def Strr(self, value):
		self._Strr = value if type(value) != base_types.auto else self.make_default("Strr")

	@Strr.deleter
	def Strr(self):
		del self._Strr
		self._Strr = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != base_types.auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
	))

