from . import base_types
from .Quantity55Choice import Quantity55Choice
from .FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice

class SecuritiesOption88(base_types._BaseFieldType):

	__slots__ = ["_CondlQty", "_InstdQty", "_AddtlRndUpQty"]
	@property
	def CondlQty(self):
		return self._CondlQty

	@CondlQty.setter
	def CondlQty(self, value):
		self._CondlQty = value if type(value) != auto else self.make_default("CondlQty")

	@CondlQty.deleter
	def CondlQty(self):
		del self._CondlQty
		self._CondlQty = None

	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if type(value) != auto else self.make_default("InstdQty")

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = None

	@property
	def AddtlRndUpQty(self):
		return self._AddtlRndUpQty

	@AddtlRndUpQty.setter
	def AddtlRndUpQty(self, value):
		self._AddtlRndUpQty = value if type(value) != auto else self.make_default("AddtlRndUpQty")

	@AddtlRndUpQty.deleter
	def AddtlRndUpQty(self):
		del self._AddtlRndUpQty
		self._AddtlRndUpQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdQty', type=Quantity55Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRndUpQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=None, array=False),
	))

