# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericValidationRuleIdentification1
from . import ISODate
from . import OriginalReportStatistics3
from . import ReportingMessageStatus1Code

class StatusAdviceReport3(base_types._BaseFieldType):

	__slots__ = ["_MsgDt", "_Sts", "_Sttstcs", "_VldtnRule"]
	@property
	def MsgDt(self):
		return self._MsgDt

	@MsgDt.setter
	def MsgDt(self, value):
		self._MsgDt = value if value is not None else base_types.UninitialisedField(self, 'MsgDt', ISODate, False)

	@MsgDt.deleter
	def MsgDt(self):
		del self._MsgDt
		self._MsgDt = base_types.UninitialisedField(self, 'MsgDt', ISODate, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ReportingMessageStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ReportingMessageStatus1Code, False)

	@property
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if value is not None else base_types.UninitialisedField(self, 'Sttstcs', OriginalReportStatistics3, False)

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = base_types.UninitialisedField(self, 'Sttstcs', OriginalReportStatistics3, False)

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
		base_types.FieldEntry(name='MsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttstcs', type=OriginalReportStatistics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))