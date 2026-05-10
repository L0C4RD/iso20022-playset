from . import base_types
from ._GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from ._MessageIdentification1 import MessageIdentification1
from ._TaxOrganisationIdentification1 import TaxOrganisationIdentification1
from ._TaxReportingStatus1Code import TaxReportingStatus1Code

class InvoiceTaxStatusReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_OrgnlMsgId", "_RptSts", "_TaxAuthrty", "_VldtnRule"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != base_types.auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	@property
	def TaxAuthrty(self):
		return self._TaxAuthrty

	@TaxAuthrty.setter
	def TaxAuthrty(self, value):
		self._TaxAuthrty = value if type(value) != base_types.auto else self.make_default("TaxAuthrty")

	@TaxAuthrty.deleter
	def TaxAuthrty(self):
		del self._TaxAuthrty
		self._TaxAuthrty = None

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
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=TaxReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAuthrty', type=TaxOrganisationIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

