from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class BalanceStatus2(base_types._BaseFieldType):

	__slots__ = ["_Bal"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

