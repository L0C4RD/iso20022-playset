from . import base_types
from .FXAmountType1Choice import FXAmountType1Choice
from .PlusOrMinusIndicator import PlusOrMinusIndicator
from .AmountOrRate4Choice import AmountOrRate4Choice

class FXCommissionOrFee1(base_types._BaseFieldType):

	__slots__ = ["_Sgn", "_AmtOrRate", "_Tp"]
	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != base_types.auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	@property
	def AmtOrRate(self):
		return self._AmtOrRate

	@AmtOrRate.setter
	def AmtOrRate(self, value):
		self._AmtOrRate = value if type(value) != base_types.auto else self.make_default("AmtOrRate")

	@AmtOrRate.deleter
	def AmtOrRate(self):
		del self._AmtOrRate
		self._AmtOrRate = None

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
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtOrRate', type=AmountOrRate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FXAmountType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

