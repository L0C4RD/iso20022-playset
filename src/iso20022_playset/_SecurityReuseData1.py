from . import base_types
from .ReuseValue1Choice import ReuseValue1Choice
from .ISINOct2015Identifier import ISINOct2015Identifier

class SecurityReuseData1(base_types._BaseFieldType):

	__slots__ = ["_ReuseVal", "_ISIN"]
	@property
	def ReuseVal(self):
		return self._ReuseVal

	@ReuseVal.setter
	def ReuseVal(self, value):
		self._ReuseVal = value if type(value) != base_types.auto else self.make_default("ReuseVal")

	@ReuseVal.deleter
	def ReuseVal(self):
		del self._ReuseVal
		self._ReuseVal = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReuseVal', type=ReuseValue1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

