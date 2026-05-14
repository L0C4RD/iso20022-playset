from . import base_types
from ._CorporateActionElection4 import CorporateActionElection4
from ._CorporateActionGeneralInformation195 import CorporateActionGeneralInformation195
from ._DocumentIdentification57 import DocumentIdentification57
from ._InstructionProcessingStatus59Choice import InstructionProcessingStatus59Choice
from ._RelatedSettlementInstruction4 import RelatedSettlementInstruction4
from ._SecuritiesAccountIdentification1Choice import SecuritiesAccountIdentification1Choice
from ._SupplementaryData1 import SupplementaryData1

class BuyerProtectionInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BuyrPrtcnInstr", "_CorpActnElctn", "_CorpActnGnlInf", "_InstrPrcgSts", "_RltdSttlmInstr", "_SplmtryData"]
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
	def BuyrPrtcnInstr(self):
		return self._BuyrPrtcnInstr

	@BuyrPrtcnInstr.setter
	def BuyrPrtcnInstr(self, value):
		self._BuyrPrtcnInstr = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstr")

	@BuyrPrtcnInstr.deleter
	def BuyrPrtcnInstr(self):
		del self._BuyrPrtcnInstr
		self._BuyrPrtcnInstr = None

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
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if type(value) != base_types.auto else self.make_default("InstrPrcgSts")

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = None

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
		base_types.FieldEntry(name='BuyrPrtcnInstr', type=DocumentIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnElctn', type=CorporateActionElection4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation195, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus59Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdSttlmInstr', type=RelatedSettlementInstruction4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

