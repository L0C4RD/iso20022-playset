from . import base_types
import GenericValidationRuleIdentification1
import Max140Text
import ReportingMessageStatus2Code

class RejectionReason70(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_DtldVldtnRule", "_MsgRptId"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def DtldVldtnRule(self):
		return self._DtldVldtnRule

	@DtldVldtnRule.setter
	def DtldVldtnRule(self, value):
		self._DtldVldtnRule = value if type(value) != auto else self.make_default("DtldVldtnRule")

	@DtldVldtnRule.deleter
	def DtldVldtnRule(self):
		del self._DtldVldtnRule
		self._DtldVldtnRule = None

	@property
	def MsgRptId(self):
		return self._MsgRptId

	@MsgRptId.setter
	def MsgRptId(self, value):
		self._MsgRptId = value if type(value) != auto else self.make_default("MsgRptId")

	@MsgRptId.deleter
	def MsgRptId(self):
		del self._MsgRptId
		self._MsgRptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldVldtnRule', type=GenericValidationRuleIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

