from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from ._ReportingRecordStatus1Code import ReportingRecordStatus1Code
from ._Max140Text import Max140Text

class StatusReportRecord3(base_types._BaseFieldType):

	__slots__ = ["_VldtnRule", "_Sts", "_SplmtryData", "_OrgnlRcrdId"]
	@property
	def OrgnlRcrdId(self):
		return self._OrgnlRcrdId

	@OrgnlRcrdId.setter
	def OrgnlRcrdId(self, value):
		self._OrgnlRcrdId = value if type(value) != base_types.auto else self.make_default("OrgnlRcrdId")

	@OrgnlRcrdId.deleter
	def OrgnlRcrdId(self):
		del self._OrgnlRcrdId
		self._OrgnlRcrdId = None

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
		base_types.FieldEntry(name='OrgnlRcrdId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportingRecordStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

