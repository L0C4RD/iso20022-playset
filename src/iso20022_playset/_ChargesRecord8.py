# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import ChargeBearerType1Code
from . import ChargeIncludedIndicator
from . import ChargeType3Choice
from . import CreditDebitCode
from . import PercentageRate
from . import TaxCharges2

class ChargesRecord8(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_Amt", "_Br", "_CdtDbtInd", "_ChrgInclInd", "_Rate", "_Tax", "_Tp"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if value is not None else base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = base_types.UninitialisedField(self, 'Agt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Br(self):
		return self._Br

	@Br.setter
	def Br(self, value):
		self._Br = value if value is not None else base_types.UninitialisedField(self, 'Br', ChargeBearerType1Code, False)

	@Br.deleter
	def Br(self):
		del self._Br
		self._Br = base_types.UninitialisedField(self, 'Br', ChargeBearerType1Code, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def ChrgInclInd(self):
		return self._ChrgInclInd

	@ChrgInclInd.setter
	def ChrgInclInd(self, value):
		self._ChrgInclInd = value if value is not None else base_types.UninitialisedField(self, 'ChrgInclInd', ChargeIncludedIndicator, False)

	@ChrgInclInd.deleter
	def ChrgInclInd(self):
		del self._ChrgInclInd
		self._ChrgInclInd = base_types.UninitialisedField(self, 'ChrgInclInd', ChargeIncludedIndicator, False)

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
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', TaxCharges2, False)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', TaxCharges2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Br', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgInclInd', type=ChargeIncludedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxCharges2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=0, max=1, mutex_group=None, array=False),
	))