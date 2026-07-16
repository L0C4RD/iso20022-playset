# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ISODateTime
from . import Max35Text
from . import SettlementInstruction19
from . import TotalCharges7

class GroupHeader130(base_types._BaseFieldType):

	__slots__ = ["_ChrgsAcctAgt", "_ChrgsAcctAgtAcct", "_ChrgsRqstr", "_CreDtTm", "_MsgId", "_SttlmInstr", "_TtlChrgs"]
	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcctAgt', BranchAndFinancialInstitutionIdentification8, False)

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = base_types.UninitialisedField(self, 'ChrgsAcctAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def ChrgsAcctAgtAcct(self):
		return self._ChrgsAcctAgtAcct

	@ChrgsAcctAgtAcct.setter
	def ChrgsAcctAgtAcct(self, value):
		self._ChrgsAcctAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcctAgtAcct', CashAccount40, False)

	@ChrgsAcctAgtAcct.deleter
	def ChrgsAcctAgtAcct(self):
		del self._ChrgsAcctAgtAcct
		self._ChrgsAcctAgtAcct = base_types.UninitialisedField(self, 'ChrgsAcctAgtAcct', CashAccount40, False)

	@property
	def ChrgsRqstr(self):
		return self._ChrgsRqstr

	@ChrgsRqstr.setter
	def ChrgsRqstr(self, value):
		self._ChrgsRqstr = value if value is not None else base_types.UninitialisedField(self, 'ChrgsRqstr', BranchAndFinancialInstitutionIdentification8, False)

	@ChrgsRqstr.deleter
	def ChrgsRqstr(self):
		del self._ChrgsRqstr
		self._ChrgsRqstr = base_types.UninitialisedField(self, 'ChrgsRqstr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def SttlmInstr(self):
		return self._SttlmInstr

	@SttlmInstr.setter
	def SttlmInstr(self, value):
		self._SttlmInstr = value if value is not None else base_types.UninitialisedField(self, 'SttlmInstr', SettlementInstruction19, False)

	@SttlmInstr.deleter
	def SttlmInstr(self):
		del self._SttlmInstr
		self._SttlmInstr = base_types.UninitialisedField(self, 'SttlmInstr', SettlementInstruction19, False)

	@property
	def TtlChrgs(self):
		return self._TtlChrgs

	@TtlChrgs.setter
	def TtlChrgs(self, value):
		self._TtlChrgs = value if value is not None else base_types.UninitialisedField(self, 'TtlChrgs', TotalCharges7, False)

	@TtlChrgs.deleter
	def TtlChrgs(self):
		del self._TtlChrgs
		self._TtlChrgs = base_types.UninitialisedField(self, 'TtlChrgs', TotalCharges7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsRqstr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstr', type=SettlementInstruction19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgs', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
	))