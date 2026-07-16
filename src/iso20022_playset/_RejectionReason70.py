# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericValidationRuleIdentification1
from . import Max140Text
from . import ReportingMessageStatus2Code

class RejectionReason70(base_types._BaseFieldType):

	__slots__ = ["_DtldVldtnRule", "_MsgRptId", "_Sts"]
	@property
	def DtldVldtnRule(self):
		return self._DtldVldtnRule

	@DtldVldtnRule.setter
	def DtldVldtnRule(self, value):
		self._DtldVldtnRule = value if value is not None else base_types.UninitialisedField(self, 'DtldVldtnRule', GenericValidationRuleIdentification1, False)

	@DtldVldtnRule.deleter
	def DtldVldtnRule(self):
		del self._DtldVldtnRule
		self._DtldVldtnRule = base_types.UninitialisedField(self, 'DtldVldtnRule', GenericValidationRuleIdentification1, False)

	@property
	def MsgRptId(self):
		return self._MsgRptId

	@MsgRptId.setter
	def MsgRptId(self, value):
		self._MsgRptId = value if value is not None else base_types.UninitialisedField(self, 'MsgRptId', Max140Text, False)

	@MsgRptId.deleter
	def MsgRptId(self):
		del self._MsgRptId
		self._MsgRptId = base_types.UninitialisedField(self, 'MsgRptId', Max140Text, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ReportingMessageStatus2Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ReportingMessageStatus2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldVldtnRule', type=GenericValidationRuleIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus2Code, min=1, max=1, mutex_group=None, array=False),
	))