from . import base_types
from .PercentageRate import PercentageRate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .WaivingInstruction2Choice import WaivingInstruction2Choice

class ChargeOrCommissionDiscount2(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Amt", "_Bsis"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

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
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if type(value) != base_types.auto else self.make_default("Bsis")

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=WaivingInstruction2Choice, min=0, max=1, mutex_group=None, array=False),
	))

