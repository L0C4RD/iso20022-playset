# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeSearch5Choice
from . import InstructionQueryType1Code
from . import Max35Text
from . import ModificationProcessingStatus9Choice
from . import SecuritiesAccount19
from . import SystemPartyIdentification8

class SecuritiesModificationQueryCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_CreDtTm", "_InstrQryTp", "_ModReqId", "_MsgOrgtr", "_PrcgSts", "_SfkpgAcct"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, True)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, True)

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
	def InstrQryTp(self):
		return self._InstrQryTp

	@InstrQryTp.setter
	def InstrQryTp(self, value):
		self._InstrQryTp = value if value is not None else base_types.UninitialisedField(self, 'InstrQryTp', InstructionQueryType1Code, False)

	@InstrQryTp.deleter
	def InstrQryTp(self):
		del self._InstrQryTp
		self._InstrQryTp = base_types.UninitialisedField(self, 'InstrQryTp', InstructionQueryType1Code, False)

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

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, True)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrQryTp', type=InstructionQueryType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModReqId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgSts', type=ModificationProcessingStatus9Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=None, mutex_group=None, array=True),
	))