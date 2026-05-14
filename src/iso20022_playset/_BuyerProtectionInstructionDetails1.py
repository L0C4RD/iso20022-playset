# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentIdentification57 import DocumentIdentification57
from ._InstructionProcessingStatus59Choice import InstructionProcessingStatus59Choice
from ._PartyIdentification143 import PartyIdentification143
from ._RelatedSettlementInstruction4 import RelatedSettlementInstruction4
from ._SecuritiesAccountIdentification1Choice import SecuritiesAccountIdentification1Choice

class BuyerProtectionInstructionDetails1(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BuyrPrtcnInstrId", "_CtrPtyDpstry", "_InstrPrcgSts", "_RltdSttlmInstrId"]
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
	def CtrPtyDpstry(self):
		return self._CtrPtyDpstry

	@CtrPtyDpstry.setter
	def CtrPtyDpstry(self, value):
		self._CtrPtyDpstry = value if type(value) != base_types.auto else self.make_default("CtrPtyDpstry")

	@CtrPtyDpstry.deleter
	def CtrPtyDpstry(self):
		del self._CtrPtyDpstry
		self._CtrPtyDpstry = None

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
	def RltdSttlmInstrId(self):
		return self._RltdSttlmInstrId

	@RltdSttlmInstrId.setter
	def RltdSttlmInstrId(self, value):
		self._RltdSttlmInstrId = value if type(value) != base_types.auto else self.make_default("RltdSttlmInstrId")

	@RltdSttlmInstrId.deleter
	def RltdSttlmInstrId(self):
		del self._RltdSttlmInstrId
		self._RltdSttlmInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=SecuritiesAccountIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrPrtcnInstrId', type=DocumentIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyDpstry', type=PartyIdentification143, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus59Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrId', type=RelatedSettlementInstruction4, min=1, max=1, mutex_group=None, array=False),
	))