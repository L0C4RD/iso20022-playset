import base_types
import AmountOrRate4Choice
import PlusOrMinusIndicator
import FXAmountType1Choice

class FXCommissionOrFee1(base_types._BaseFieldType):

	__slots__ = ["_AmtOrRate", "_Tp", "_Sgn"]
	@property
	def AmtOrRate(self):
		return self._AmtOrRate

	@AmtOrRate.setter
	def AmtOrRate(self, value):
		self._AmtOrRate = value if type(value) != auto else self.make_default("AmtOrRate")

	@AmtOrRate.deleter
	def AmtOrRate(self):
		del self._AmtOrRate
		self._AmtOrRate = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOrRate', type=AmountOrRate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FXAmountType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))

