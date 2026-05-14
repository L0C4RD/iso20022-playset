from . import base_types
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max6NumericText import Max6NumericText
from ._TemporaryServicesCharge2Code import TemporaryServicesCharge2Code

class TemporaryServiceChargeRate1(base_types._BaseFieldType):

	__slots__ = ["_Hrs", "_Rate", "_Tp"]
	@property
	def Hrs(self):
		return self._Hrs

	@Hrs.setter
	def Hrs(self, value):
		self._Hrs = value if type(value) != base_types.auto else self.make_default("Hrs")

	@Hrs.deleter
	def Hrs(self):
		del self._Hrs
		self._Hrs = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrs', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TemporaryServicesCharge2Code, min=0, max=1, mutex_group=None, array=False),
	))

