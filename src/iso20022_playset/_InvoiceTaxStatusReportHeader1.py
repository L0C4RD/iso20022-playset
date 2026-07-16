# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericValidationRuleIdentification1
from . import MessageIdentification1
from . import TaxOrganisationIdentification1
from . import TaxReportingStatus1Code

class InvoiceTaxStatusReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_OrgnlMsgId", "_RptSts", "_TaxAuthrty", "_VldtnRule"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', MessageIdentification1, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', MessageIdentification1, False)

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if value is not None else base_types.UninitialisedField(self, 'RptSts', TaxReportingStatus1Code, False)

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = base_types.UninitialisedField(self, 'RptSts', TaxReportingStatus1Code, False)

	@property
	def TaxAuthrty(self):
		return self._TaxAuthrty

	@TaxAuthrty.setter
	def TaxAuthrty(self, value):
		self._TaxAuthrty = value if value is not None else base_types.UninitialisedField(self, 'TaxAuthrty', TaxOrganisationIdentification1, False)

	@TaxAuthrty.deleter
	def TaxAuthrty(self):
		del self._TaxAuthrty
		self._TaxAuthrty = base_types.UninitialisedField(self, 'TaxAuthrty', TaxOrganisationIdentification1, False)

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
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=TaxReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAuthrty', type=TaxOrganisationIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))