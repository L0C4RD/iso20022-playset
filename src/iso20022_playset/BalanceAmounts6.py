from . import base_types
from .AmountAndDirection14 import AmountAndDirection14

class BalanceAmounts6(base_types._BaseFieldType):

	__slots__ = ["_BookVal", "_HldgVal", "_UrlsdGnLoss"]
	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if type(value) != base_types.auto else self.make_default("BookVal")

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = None

	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if type(value) != base_types.auto else self.make_default("HldgVal")

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = None

	@property
	def UrlsdGnLoss(self):
		return self._UrlsdGnLoss

	@UrlsdGnLoss.setter
	def UrlsdGnLoss(self, value):
		self._UrlsdGnLoss = value if type(value) != base_types.auto else self.make_default("UrlsdGnLoss")

	@UrlsdGnLoss.deleter
	def UrlsdGnLoss(self):
		del self._UrlsdGnLoss
		self._UrlsdGnLoss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=AmountAndDirection14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrlsdGnLoss', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
	))

