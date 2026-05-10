from . import base_types
from .GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from .OriginalReportStatistics3 import OriginalReportStatistics3
from .ReportingMessageStatus1Code import ReportingMessageStatus1Code
from .ISODate import ISODate

class StatusAdviceReport3(base_types._BaseFieldType):

	__slots__ = ["_Sttstcs", "_MsgDt", "_VldtnRule", "_Sts"]
	@property
	def Sttstcs(self):
		return self._Sttstcs

	@Sttstcs.setter
	def Sttstcs(self, value):
		self._Sttstcs = value if type(value) != auto else self.make_default("Sttstcs")

	@Sttstcs.deleter
	def Sttstcs(self):
		del self._Sttstcs
		self._Sttstcs = None

	@property
	def MsgDt(self):
		return self._MsgDt

	@MsgDt.setter
	def MsgDt(self, value):
		self._MsgDt = value if type(value) != auto else self.make_default("MsgDt")

	@MsgDt.deleter
	def MsgDt(self):
		del self._MsgDt
		self._MsgDt = None

	@property
	def VldtnRule(self):
		return self._VldtnRule

	@VldtnRule.setter
	def VldtnRule(self, value):
		self._VldtnRule = value if type(value) != auto else self.make_default("VldtnRule")

	@VldtnRule.deleter
	def VldtnRule(self):
		del self._VldtnRule
		self._VldtnRule = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sttstcs', type=OriginalReportStatistics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportingMessageStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

