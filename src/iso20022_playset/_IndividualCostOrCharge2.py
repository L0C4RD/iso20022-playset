# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import ChargeType8Choice
from . import IntendedOrActual2Code
from . import PercentageRate
from . import Period15
from . import PlusOrMinusIndicator

class IndividualCostOrCharge2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_CostTp", "_ExAnteOrExPst", "_Rate", "_RefPrd", "_Sgn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def CostTp(self):
		return self._CostTp

	@CostTp.setter
	def CostTp(self, value):
		self._CostTp = value if value is not None else base_types.UninitialisedField(self, 'CostTp', ChargeType8Choice, False)

	@CostTp.deleter
	def CostTp(self):
		del self._CostTp
		self._CostTp = base_types.UninitialisedField(self, 'CostTp', ChargeType8Choice, False)

	@property
	def ExAnteOrExPst(self):
		return self._ExAnteOrExPst

	@ExAnteOrExPst.setter
	def ExAnteOrExPst(self, value):
		self._ExAnteOrExPst = value if value is not None else base_types.UninitialisedField(self, 'ExAnteOrExPst', IntendedOrActual2Code, False)

	@ExAnteOrExPst.deleter
	def ExAnteOrExPst(self):
		del self._ExAnteOrExPst
		self._ExAnteOrExPst = base_types.UninitialisedField(self, 'ExAnteOrExPst', IntendedOrActual2Code, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if value is not None else base_types.UninitialisedField(self, 'RefPrd', Period15, False)

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = base_types.UninitialisedField(self, 'RefPrd', Period15, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostTp', type=ChargeType8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteOrExPst', type=IntendedOrActual2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPrd', type=Period15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
	))