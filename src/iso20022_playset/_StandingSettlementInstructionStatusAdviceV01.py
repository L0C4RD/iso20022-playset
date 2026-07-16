# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification26
from . import EffectiveDate1
from . import MarketIdentificationOrCashPurpose1Choice
from . import Max35Text
from . import PartyOrCurrency1Choice
from . import ProcessingStatus43Choice
from . import SupplementaryData1

class StandingSettlementInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_FctvDtDtls", "_MktId", "_PrcgSts", "_RltdMsgRef", "_SplmtryData", "_SttlmDtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification26, True)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification26, True)

	@property
	def FctvDtDtls(self):
		return self._FctvDtDtls

	@FctvDtDtls.setter
	def FctvDtDtls(self, value):
		self._FctvDtDtls = value if value is not None else base_types.UninitialisedField(self, 'FctvDtDtls', EffectiveDate1, False)

	@FctvDtDtls.deleter
	def FctvDtDtls(self):
		del self._FctvDtDtls
		self._FctvDtDtls = base_types.UninitialisedField(self, 'FctvDtDtls', EffectiveDate1, False)

	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if value is not None else base_types.UninitialisedField(self, 'MktId', MarketIdentificationOrCashPurpose1Choice, False)

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = base_types.UninitialisedField(self, 'MktId', MarketIdentificationOrCashPurpose1Choice, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus43Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus43Choice, False)

	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if value is not None else base_types.UninitialisedField(self, 'RltdMsgRef', Max35Text, False)

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = base_types.UninitialisedField(self, 'RltdMsgRef', Max35Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SttlmDtls(self):
		return self._SttlmDtls

	@SttlmDtls.setter
	def SttlmDtls(self, value):
		self._SttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmDtls', PartyOrCurrency1Choice, False)

	@SttlmDtls.deleter
	def SttlmDtls(self):
		del self._SttlmDtls
		self._SttlmDtls = base_types.UninitialisedField(self, 'SttlmDtls', PartyOrCurrency1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification26, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FctvDtDtls', type=EffectiveDate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MarketIdentificationOrCashPurpose1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus43Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMsgRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmDtls', type=PartyOrCurrency1Choice, min=1, max=1, mutex_group=None, array=False),
	))