# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from ._Max140Text import Max140Text
from ._ReportingMessageStatus1Code import ReportingMessageStatus1Code

class RejectionReason45(base_types._BaseFieldType):

	__slots__ = ["_DtldVldtnRule", "_MsgRptId", "_Sts"]
	@property
	def DtldVldtnRule(self):
		return self._DtldVldtnRule

	@DtldVldtnRule.setter
	def DtldVldtnRule(self, value):
		self._DtldVldtnRule = value if type(value) != base_types.auto else self.make_default("DtldVldtnRule")

	@DtldVldtnRule.deleter
	def DtldVldtnRule(self):
		del self._DtldVldtnRule
		self._DtldVldtnRule = None

	@property
	def MsgRptId(self):
		return self._MsgRptId

	@MsgRptId.setter
	def MsgRptId(self, value):
		self._MsgRptId = value if type(value) != base_types.auto else self.make_default("MsgRptId")

	@MsgRptId.deleter
	def MsgRptId(self):
		del self._MsgRptId
		self._MsgRptId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldVldtnRule', type=GenericValidationRuleIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))