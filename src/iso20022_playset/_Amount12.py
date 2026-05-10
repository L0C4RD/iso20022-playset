from . import base_types
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Max6NumericText import Max6NumericText
from ._TemporaryServicesCharge1Code import TemporaryServicesCharge1Code

class Amount12(base_types._BaseFieldType):

	__slots__ = ["_Hrs", "_OthrTp", "_Rate", "_Tp"]
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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != base_types.auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

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
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TemporaryServicesCharge1Code, min=0, max=1, mutex_group=None, array=False),
	))

