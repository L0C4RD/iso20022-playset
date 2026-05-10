from . import base_types
from ._ChargeIncludedIndicator import ChargeIncludedIndicator
from ._CreditDebitCode import CreditDebitCode
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._PercentageRate import PercentageRate
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ChargeType3Choice import ChargeType3Choice
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._TaxCharges2 import TaxCharges2

class ChargesRecord8(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Agt", "_Amt", "_Tax", "_Br", "_CdtDbtInd", "_Rate", "_ChrgInclInd"]
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
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != base_types.auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

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
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def Br(self):
		return self._Br

	@Br.setter
	def Br(self, value):
		self._Br = value if type(value) != base_types.auto else self.make_default("Br")

	@Br.deleter
	def Br(self):
		del self._Br
		self._Br = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

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
	def ChrgInclInd(self):
		return self._ChrgInclInd

	@ChrgInclInd.setter
	def ChrgInclInd(self, value):
		self._ChrgInclInd = value if type(value) != base_types.auto else self.make_default("ChrgInclInd")

	@ChrgInclInd.deleter
	def ChrgInclInd(self):
		del self._ChrgInclInd
		self._ChrgInclInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxCharges2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Br', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgInclInd', type=ChargeIncludedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

