import base_types
import Quantity52Choice
import FinancialInstrumentQuantity33Choice

class SecuritiesOption79(base_types._BaseFieldType):

	__slots__ = ["_InstdQty", "_AddtlRndUpQty", "_CondlQty"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdQty', type=Quantity52Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRndUpQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
	))

