# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionElection4
from . import CorporateActionGeneralInformation195
from . import RelatedSettlementInstruction3
from . import SecuritiesAccountIdentification1Choice
from . import SupplementaryData1

class BuyerProtectionInstructionV01(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_CorpActnElctn", "_CorpActnGnlInf", "_RltdSttlmInstr", "_SplmtryData"]
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
	def RltdSttlmInstr(self):
		return self._RltdSttlmInstr

	@RltdSttlmInstr.setter
	def RltdSttlmInstr(self, value):
		self._RltdSttlmInstr = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmInstr', RelatedSettlementInstruction3, False)

	@RltdSttlmInstr.deleter
	def RltdSttlmInstr(self):
		del self._RltdSttlmInstr
		self._RltdSttlmInstr = base_types.UninitialisedField(self, 'RltdSttlmInstr', RelatedSettlementInstruction3, False)

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
		base_types.FieldEntry(name='CorpActnElctn', type=CorporateActionElection4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation195, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstr', type=RelatedSettlementInstruction3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))