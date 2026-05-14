# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._TaxReportingStatus2Code import TaxReportingStatus2Code

class InvoiceTaxReportTransactionStatus1(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Sts", "_TaxRptId", "_VldtnRule"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def TaxRptId(self):
		return self._TaxRptId

	@TaxRptId.setter
	def TaxRptId(self, value):
		self._TaxRptId = value if type(value) != base_types.auto else self.make_default("TaxRptId")

	@TaxRptId.deleter
	def TaxRptId(self):
		del self._TaxRptId
		self._TaxRptId = None

	@property
	def VldtnRule(self):
		return self._VldtnRule

	@VldtnRule.setter
	def VldtnRule(self, value):
		self._VldtnRule = value if type(value) != base_types.auto else self.make_default("VldtnRule")

	@VldtnRule.deleter
	def VldtnRule(self):
		del self._VldtnRule
		self._VldtnRule = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=TaxReportingStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))