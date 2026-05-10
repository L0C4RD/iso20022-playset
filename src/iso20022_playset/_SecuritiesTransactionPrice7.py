from . import base_types
from ._DigitalTokenAmount2 import DigitalTokenAmount2
from ._AmountAndDirection61 import AmountAndDirection61

class SecuritiesTransactionPrice7(base_types._BaseFieldType):

	__slots__ = ["_MntryVal", "_DgtlTknQty"]
	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if type(value) != base_types.auto else self.make_default("MntryVal")

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = None

	@property
	def DgtlTknQty(self):
		return self._DgtlTknQty

	@DgtlTknQty.setter
	def DgtlTknQty(self, value):
		self._DgtlTknQty = value if type(value) != base_types.auto else self.make_default("DgtlTknQty")

	@DgtlTknQty.deleter
	def DgtlTknQty(self):
		del self._DgtlTknQty
		self._DgtlTknQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection61, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlTknQty', type=DigitalTokenAmount2, min=1, max=1, mutex_group=None, array=False),
	))

