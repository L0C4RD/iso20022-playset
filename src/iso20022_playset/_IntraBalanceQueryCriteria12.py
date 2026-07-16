# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationSearchCriteria2Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import DateAndDateTimeSearch5Choice
from . import Max35Text
from . import ModificationProcessingStatus9Choice
from . import SystemPartyIdentification8

class IntraBalanceQueryCriteria12(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_CshAcct", "_CshAcctOwnr", "_CshAcctSvcr", "_ModReqId", "_MsgOrgtr", "_PrcgSts"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTimeSearch5Choice, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', DateAndDateTimeSearch5Choice, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', AccountIdentificationSearchCriteria2Choice, True)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', AccountIdentificationSearchCriteria2Choice, True)

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification8, True)

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = base_types.UninitialisedField(self, 'CshAcctOwnr', SystemPartyIdentification8, True)

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = base_types.UninitialisedField(self, 'CshAcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def ModReqId(self):
		return self._ModReqId

	@ModReqId.setter
	def ModReqId(self, value):
		self._ModReqId = value if value is not None else base_types.UninitialisedField(self, 'ModReqId', Max35Text, True)

	@ModReqId.deleter
	def ModReqId(self):
		del self._ModReqId
		self._ModReqId = base_types.UninitialisedField(self, 'ModReqId', Max35Text, True)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, True)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, True)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ModificationProcessingStatus9Choice, True)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ModificationProcessingStatus9Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModReqId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgSts', type=ModificationProcessingStatus9Choice, min=0, max=None, mutex_group=None, array=True),
	))