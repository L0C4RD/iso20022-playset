from . import base_types
import PartyOrCurrency1Choice
import EffectiveDate1
import ProcessingStatus43Choice
import AccountIdentification26
import SupplementaryData1
import MarketIdentificationOrCashPurpose1Choice
import Max35Text

class StandingSettlementInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_RltdMsgRef", "_SplmtryData", "_FctvDtDtls", "_MktId", "_AcctId", "_SttlmDtls", "_PrcgSts"]
	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if type(value) != auto else self.make_default("RltdMsgRef")

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = None

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
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdMsgRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FctvDtDtls', type=EffectiveDate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MarketIdentificationOrCashPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification26, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmDtls', type=PartyOrCurrency1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus43Choice, min=1, max=1, mutex_group=None, array=False),
	))

