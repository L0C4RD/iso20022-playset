# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionElection4
from . import CorporateActionGeneralInformation195
from . import DocumentIdentification57
from . import InstructionProcessingStatus59Choice
from . import RelatedSettlementInstruction4
from . import SecuritiesAccountIdentification1Choice
from . import SupplementaryData1

class BuyerProtectionInstructionStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BuyrPrtcnInstr", "_CorpActnElctn", "_CorpActnGnlInf", "_InstrPrcgSts", "_RltdSttlmInstr", "_SplmtryData"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', SecuritiesAccountIdentification1Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', SecuritiesAccountIdentification1Choice, False)

	@property
	def BuyrPrtcnInstr(self):
		return self._BuyrPrtcnInstr

	@BuyrPrtcnInstr.setter
	def BuyrPrtcnInstr(self, value):
		self._BuyrPrtcnInstr = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstr', DocumentIdentification57, False)

	@BuyrPrtcnInstr.deleter
	def BuyrPrtcnInstr(self):
		del self._BuyrPrtcnInstr
		self._BuyrPrtcnInstr = base_types.UninitialisedField(self, 'BuyrPrtcnInstr', DocumentIdentification57, False)

	@property
	def CorpActnElctn(self):
		return self._CorpActnElctn

	@CorpActnElctn.setter
	def CorpActnElctn(self, value):
		self._CorpActnElctn = value if value is not None else base_types.UninitialisedField(self, 'CorpActnElctn', CorporateActionElection4, False)

	@CorpActnElctn.deleter
	def CorpActnElctn(self):
		del self._CorpActnElctn
		self._CorpActnElctn = base_types.UninitialisedField(self, 'CorpActnElctn', CorporateActionElection4, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation195, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation195, False)

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus59Choice, True)

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus59Choice, True)

	@property
	def RltdSttlmInstr(self):
		return self._RltdSttlmInstr

	@RltdSttlmInstr.setter
	def RltdSttlmInstr(self, value):
		self._RltdSttlmInstr = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmInstr', RelatedSettlementInstruction4, False)

	@RltdSttlmInstr.deleter
	def RltdSttlmInstr(self):
		del self._RltdSttlmInstr
		self._RltdSttlmInstr = base_types.UninitialisedField(self, 'RltdSttlmInstr', RelatedSettlementInstruction4, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccountIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrPrtcnInstr', type=DocumentIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnElctn', type=CorporateActionElection4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation195, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus59Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdSttlmInstr', type=RelatedSettlementInstruction4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))