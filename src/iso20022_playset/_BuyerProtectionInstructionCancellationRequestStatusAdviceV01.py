from . import base_types
from ._CorporateActionElection4 import CorporateActionElection4
from ._CorporateActionGeneralInformation195 import CorporateActionGeneralInformation195
from ._DocumentIdentification57 import DocumentIdentification57
from ._InstructionCancellationRequestStatus20Choice import InstructionCancellationRequestStatus20Choice
from ._Max35Text import Max35Text
from ._RelatedSettlementInstruction4 import RelatedSettlementInstruction4
from ._SecuritiesAccountIdentification1Choice import SecuritiesAccountIdentification1Choice
from ._SupplementaryData1 import SupplementaryData1

class BuyerProtectionInstructionCancellationRequestStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BuyrPrtcnInstrId", "_CorpActnElctn", "_CorpActnGnlInf", "_InstrCxlReqSts", "_PrcrTxId", "_RltdSttlmInstr", "_SplmtryData"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def BuyrPrtcnInstrId(self):
		return self._BuyrPrtcnInstrId

	@BuyrPrtcnInstrId.setter
	def BuyrPrtcnInstrId(self, value):
		self._BuyrPrtcnInstrId = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrId")

	@BuyrPrtcnInstrId.deleter
	def BuyrPrtcnInstrId(self):
		del self._BuyrPrtcnInstrId
		self._BuyrPrtcnInstrId = None

	@property
	def CorpActnElctn(self):
		return self._CorpActnElctn

	@CorpActnElctn.setter
	def CorpActnElctn(self, value):
		self._CorpActnElctn = value if type(value) != base_types.auto else self.make_default("CorpActnElctn")

	@CorpActnElctn.deleter
	def CorpActnElctn(self):
		del self._CorpActnElctn
		self._CorpActnElctn = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def InstrCxlReqSts(self):
		return self._InstrCxlReqSts

	@InstrCxlReqSts.setter
	def InstrCxlReqSts(self, value):
		self._InstrCxlReqSts = value if type(value) != base_types.auto else self.make_default("InstrCxlReqSts")

	@InstrCxlReqSts.deleter
	def InstrCxlReqSts(self):
		del self._InstrCxlReqSts
		self._InstrCxlReqSts = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != base_types.auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

	@property
	def RltdSttlmInstr(self):
		return self._RltdSttlmInstr

	@RltdSttlmInstr.setter
	def RltdSttlmInstr(self, value):
		self._RltdSttlmInstr = value if type(value) != base_types.auto else self.make_default("RltdSttlmInstr")

	@RltdSttlmInstr.deleter
	def RltdSttlmInstr(self):
		del self._RltdSttlmInstr
		self._RltdSttlmInstr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccountIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrPrtcnInstrId', type=DocumentIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnElctn', type=CorporateActionElection4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation195, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqSts', type=InstructionCancellationRequestStatus20Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstr', type=RelatedSettlementInstruction4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

