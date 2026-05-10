from . import base_types
from .AmountAndDirection6 import AmountAndDirection6

class BalanceAmounts2(base_types._BaseFieldType):

	__slots__ = ["_UrlsdGnLoss", "_BookVal", "_HldgVal"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='UrlsdGnLoss', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=AmountAndDirection6, min=1, max=1, mutex_group=None, array=False),
	))

