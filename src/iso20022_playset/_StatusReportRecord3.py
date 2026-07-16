# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericValidationRuleIdentification1
from . import Max140Text
from . import ReportingRecordStatus1Code
from . import SupplementaryData1

class StatusReportRecord3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlRcrdId", "_SplmtryData", "_Sts", "_VldtnRule"]
	@property
	def OrgnlRcrdId(self):
		return self._OrgnlRcrdId

	@OrgnlRcrdId.setter
	def OrgnlRcrdId(self, value):
		self._OrgnlRcrdId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRcrdId', Max140Text, False)

	@OrgnlRcrdId.deleter
	def OrgnlRcrdId(self):
		del self._OrgnlRcrdId
		self._OrgnlRcrdId = base_types.UninitialisedField(self, 'OrgnlRcrdId', Max140Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ReportingRecordStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ReportingRecordStatus1Code, False)

	@property
	def VldtnRule(self):
		return self._VldtnRule

	@VldtnRule.setter
	def VldtnRule(self, value):
		self._VldtnRule = value if value is not None else base_types.UninitialisedField(self, 'VldtnRule', GenericValidationRuleIdentification1, True)

	@VldtnRule.deleter
	def VldtnRule(self):
		del self._VldtnRule
		self._VldtnRule = base_types.UninitialisedField(self, 'VldtnRule', GenericValidationRuleIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlRcrdId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportingRecordStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))