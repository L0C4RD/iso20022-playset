import base_types
import ISINOct2015Identifier
import Max52Text
import LEIIdentifier

class BasketQuery1(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_Idr", "_Strr"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

	@property
	def Strr(self):
		return self._Strr

	@Strr.setter
	def Strr(self, value):
		self._Strr = value if type(value) != auto else self.make_default("Strr")

	@Strr.deleter
	def Strr(self):
		del self._Strr
		self._Strr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

