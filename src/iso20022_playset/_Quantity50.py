from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._DecimalNumber import DecimalNumber
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate

class Quantity50(base_types._BaseFieldType):

	__slots__ = ["_AmtsdVal", "_CshAmt", "_FaceAmt", "_OthrAsst", "_PctgRate", "_Unit"]
	@property
	def AmtsdVal(self):
		return self._AmtsdVal

	@AmtsdVal.setter
	def AmtsdVal(self, value):
		self._AmtsdVal = value if type(value) != base_types.auto else self.make_default("AmtsdVal")

	@AmtsdVal.deleter
	def AmtsdVal(self):
		del self._AmtsdVal
		self._AmtsdVal = None

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if type(value) != base_types.auto else self.make_default("CshAmt")

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = None

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if type(value) != base_types.auto else self.make_default("FaceAmt")

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = None

	@property
	def OthrAsst(self):
		return self._OthrAsst

	@OthrAsst.setter
	def OthrAsst(self, value):
		self._OthrAsst = value if type(value) != base_types.auto else self.make_default("OthrAsst")

	@OthrAsst.deleter
	def OthrAsst(self):
		del self._OthrAsst
		self._OthrAsst = None

	@property
	def PctgRate(self):
		return self._PctgRate

	@PctgRate.setter
	def PctgRate(self, value):
		self._PctgRate = value if type(value) != base_types.auto else self.make_default("PctgRate")

	@PctgRate.deleter
	def PctgRate(self):
		del self._PctgRate
		self._PctgRate = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtsdVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAsst', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

