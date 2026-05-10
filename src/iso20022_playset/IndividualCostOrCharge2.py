from . import base_types
import ChargeType8Choice
import ActiveCurrencyAnd13DecimalAmount
import PercentageRate
import IntendedOrActual2Code
import Period15
import PlusOrMinusIndicator
import AdditionalInformation15

class IndividualCostOrCharge2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CostTp", "_AddtlInf", "_Rate", "_ExAnteOrExPst", "_RefPrd", "_Sgn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CostTp(self):
		return self._CostTp

	@CostTp.setter
	def CostTp(self, value):
		self._CostTp = value if type(value) != auto else self.make_default("CostTp")

	@CostTp.deleter
	def CostTp(self):
		del self._CostTp
		self._CostTp = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def ExAnteOrExPst(self):
		return self._ExAnteOrExPst

	@ExAnteOrExPst.setter
	def ExAnteOrExPst(self, value):
		self._ExAnteOrExPst = value if type(value) != auto else self.make_default("ExAnteOrExPst")

	@ExAnteOrExPst.deleter
	def ExAnteOrExPst(self):
		del self._ExAnteOrExPst
		self._ExAnteOrExPst = None

	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if type(value) != auto else self.make_default("RefPrd")

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = None

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
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostTp', type=ChargeType8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteOrExPst', type=IntendedOrActual2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPrd', type=Period15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))

