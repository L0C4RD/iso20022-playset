from . import base_types
from .CashSubBalanceTypeAndQuantityBreakdown3 import CashSubBalanceTypeAndQuantityBreakdown3

class IntraBalanceType3(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if type(value) != auto else self.make_default("BalTo")

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=CashSubBalanceTypeAndQuantityBreakdown3, min=0, max=1, mutex_group=None, array=False),
	))

