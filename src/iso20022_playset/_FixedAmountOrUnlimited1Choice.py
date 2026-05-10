from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Unlimited9Text import Unlimited9Text

class FixedAmountOrUnlimited1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_NotLtd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def NotLtd(self):
		return self._NotLtd

	@NotLtd.setter
	def NotLtd(self, value):
		self._NotLtd = value if type(value) != base_types.auto else self.make_default("NotLtd")

	@NotLtd.deleter
	def NotLtd(self):
		del self._NotLtd
		self._NotLtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotLtd', type=Unlimited9Text, min=0, max=1, mutex_group=1, array=False),
	))

