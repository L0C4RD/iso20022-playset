from . import base_types
from ._AmountAndDirection34 import AmountAndDirection34
from ._BillingCompensationType1Choice import BillingCompensationType1Choice
from ._BillingCurrencyType2Code import BillingCurrencyType2Code

class BillingCompensation1(base_types._BaseFieldType):

	__slots__ = ["_CcyTp", "_Tp", "_Val"]
	@property
	def CcyTp(self):
		return self._CcyTp

	@CcyTp.setter
	def CcyTp(self, value):
		self._CcyTp = value if type(value) != base_types.auto else self.make_default("CcyTp")

	@CcyTp.deleter
	def CcyTp(self):
		del self._CcyTp
		self._CcyTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyTp', type=BillingCurrencyType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BillingCompensationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

