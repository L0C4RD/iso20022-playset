from . import base_types
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._Quantity52Choice import Quantity52Choice

class SecuritiesOption79(base_types._BaseFieldType):

	__slots__ = ["_AddtlRndUpQty", "_CondlQty", "_InstdQty"]
	@property
	def AddtlRndUpQty(self):
		return self._AddtlRndUpQty

	@AddtlRndUpQty.setter
	def AddtlRndUpQty(self, value):
		self._AddtlRndUpQty = value if type(value) != base_types.auto else self.make_default("AddtlRndUpQty")

	@AddtlRndUpQty.deleter
	def AddtlRndUpQty(self):
		del self._AddtlRndUpQty
		self._AddtlRndUpQty = None

	@property
	def CondlQty(self):
		return self._CondlQty

	@CondlQty.setter
	def CondlQty(self, value):
		self._CondlQty = value if type(value) != base_types.auto else self.make_default("CondlQty")

	@CondlQty.deleter
	def CondlQty(self):
		del self._CondlQty
		self._CondlQty = None

	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if type(value) != base_types.auto else self.make_default("InstdQty")

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRndUpQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdQty', type=Quantity52Choice, min=1, max=1, mutex_group=None, array=False),
	))

