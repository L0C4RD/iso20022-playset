from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class Amount2(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCcyAmt", "_RptgAmt"]
	@property
	def OrgnlCcyAmt(self):
		return self._OrgnlCcyAmt

	@OrgnlCcyAmt.setter
	def OrgnlCcyAmt(self, value):
		self._OrgnlCcyAmt = value if type(value) != base_types.auto else self.make_default("OrgnlCcyAmt")

	@OrgnlCcyAmt.deleter
	def OrgnlCcyAmt(self):
		del self._OrgnlCcyAmt
		self._OrgnlCcyAmt = None

	@property
	def RptgAmt(self):
		return self._RptgAmt

	@RptgAmt.setter
	def RptgAmt(self, value):
		self._RptgAmt = value if type(value) != base_types.auto else self.make_default("RptgAmt")

	@RptgAmt.deleter
	def RptgAmt(self):
		del self._RptgAmt
		self._RptgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCcyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

