# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification57
from . import InstructionProcessingStatus59Choice
from . import PartyIdentification143
from . import RelatedSettlementInstruction4
from . import SecuritiesAccountIdentification1Choice

class BuyerProtectionInstructionDetails1(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BuyrPrtcnInstrId", "_CtrPtyDpstry", "_InstrPrcgSts", "_RltdSttlmInstrId"]
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
	def BuyrPrtcnInstrId(self):
		return self._BuyrPrtcnInstrId

	@BuyrPrtcnInstrId.setter
	def BuyrPrtcnInstrId(self, value):
		self._BuyrPrtcnInstrId = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrId', DocumentIdentification57, False)

	@BuyrPrtcnInstrId.deleter
	def BuyrPrtcnInstrId(self):
		del self._BuyrPrtcnInstrId
		self._BuyrPrtcnInstrId = base_types.UninitialisedField(self, 'BuyrPrtcnInstrId', DocumentIdentification57, False)

	@property
	def CtrPtyDpstry(self):
		return self._CtrPtyDpstry

	@CtrPtyDpstry.setter
	def CtrPtyDpstry(self, value):
		self._CtrPtyDpstry = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyDpstry', PartyIdentification143, False)

	@CtrPtyDpstry.deleter
	def CtrPtyDpstry(self):
		del self._CtrPtyDpstry
		self._CtrPtyDpstry = base_types.UninitialisedField(self, 'CtrPtyDpstry', PartyIdentification143, False)

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus59Choice, False)

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus59Choice, False)

	@property
	def RltdSttlmInstrId(self):
		return self._RltdSttlmInstrId

	@RltdSttlmInstrId.setter
	def RltdSttlmInstrId(self, value):
		self._RltdSttlmInstrId = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmInstrId', RelatedSettlementInstruction4, False)

	@RltdSttlmInstrId.deleter
	def RltdSttlmInstrId(self):
		del self._RltdSttlmInstrId
		self._RltdSttlmInstrId = base_types.UninitialisedField(self, 'RltdSttlmInstrId', RelatedSettlementInstruction4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccountIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrPrtcnInstrId', type=DocumentIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyDpstry', type=PartyIdentification143, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus59Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrId', type=RelatedSettlementInstruction4, min=1, max=1, mutex_group=None, array=False),
	))