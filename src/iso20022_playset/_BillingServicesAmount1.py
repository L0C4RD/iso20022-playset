from . import base_types
from .AmountAndDirection34 import AmountAndDirection34

class BillingServicesAmount1(base_types._BaseFieldType):

	__slots__ = ["_HstAmt", "_PricgAmt"]
	@property
	def HstAmt(self):
		return self._HstAmt

	@HstAmt.setter
	def HstAmt(self, value):
		self._HstAmt = value if type(value) != base_types.auto else self.make_default("HstAmt")

	@HstAmt.deleter
	def HstAmt(self):
		del self._HstAmt
		self._HstAmt = None

	@property
	def PricgAmt(self):
		return self._PricgAmt

	@PricgAmt.setter
	def PricgAmt(self, value):
		self._PricgAmt = value if type(value) != base_types.auto else self.make_default("PricgAmt")

	@PricgAmt.deleter
	def PricgAmt(self):
		del self._PricgAmt
		self._PricgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))

