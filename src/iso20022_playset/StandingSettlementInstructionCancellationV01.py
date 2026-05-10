from . import base_types
from .Max35Text import Max35Text
from .PartyOrCurrency1Choice import PartyOrCurrency1Choice
from .AccountIdentification26 import AccountIdentification26
from .EffectiveDate1 import EffectiveDate1
from .SupplementaryData1 import SupplementaryData1
from .MarketIdentificationOrCashPurpose1Choice import MarketIdentificationOrCashPurpose1Choice

class StandingSettlementInstructionCancellationV01(base_types._BaseFieldType):

	__slots__ = ["_SttlmDtls", "_AcctId", "_SplmtryData", "_PrvsMsgRef", "_MsgRefId", "_FctvDtDtls", "_MktId"]
	@property
	def SttlmDtls(self):
		return self._SttlmDtls

	@SttlmDtls.setter
	def SttlmDtls(self, value):
		self._SttlmDtls = value if type(value) != auto else self.make_default("SttlmDtls")

	@SttlmDtls.deleter
	def SttlmDtls(self):
		del self._SttlmDtls
		self._SttlmDtls = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def PrvsMsgRef(self):
		return self._PrvsMsgRef

	@PrvsMsgRef.setter
	def PrvsMsgRef(self, value):
		self._PrvsMsgRef = value if type(value) != auto else self.make_default("PrvsMsgRef")

	@PrvsMsgRef.deleter
	def PrvsMsgRef(self):
		del self._PrvsMsgRef
		self._PrvsMsgRef = None

	@property
	def MsgRefId(self):
		return self._MsgRefId

	@MsgRefId.setter
	def MsgRefId(self, value):
		self._MsgRefId = value if type(value) != auto else self.make_default("MsgRefId")

	@MsgRefId.deleter
	def MsgRefId(self):
		del self._MsgRefId
		self._MsgRefId = None

	@property
	def FctvDtDtls(self):
		return self._FctvDtDtls

	@FctvDtDtls.setter
	def FctvDtDtls(self, value):
		self._FctvDtDtls = value if type(value) != auto else self.make_default("FctvDtDtls")

	@FctvDtDtls.deleter
	def FctvDtDtls(self):
		del self._FctvDtDtls
		self._FctvDtDtls = None

	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if type(value) != auto else self.make_default("MktId")

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmDtls', type=PartyOrCurrency1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification26, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsMsgRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRefId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDtDtls', type=EffectiveDate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MarketIdentificationOrCashPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
	))

