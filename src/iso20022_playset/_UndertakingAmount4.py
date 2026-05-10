from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class UndertakingAmount4(base_types._BaseFieldType):

	__slots__ = ["_VartnAmt", "_BalAmt"]
	@property
	def VartnAmt(self):
		return self._VartnAmt

	@VartnAmt.setter
	def VartnAmt(self, value):
		self._VartnAmt = value if type(value) != base_types.auto else self.make_default("VartnAmt")

	@VartnAmt.deleter
	def VartnAmt(self):
		del self._VartnAmt
		self._VartnAmt = None

	@property
	def BalAmt(self):
		return self._BalAmt

	@BalAmt.setter
	def BalAmt(self, value):
		self._BalAmt = value if type(value) != base_types.auto else self.make_default("BalAmt")

	@BalAmt.deleter
	def BalAmt(self):
		del self._BalAmt
		self._BalAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VartnAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

