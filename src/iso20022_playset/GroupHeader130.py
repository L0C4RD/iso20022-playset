from . import base_types
import CashAccount40
import ISODateTime
import Max35Text
import TotalCharges7
import BranchAndFinancialInstitutionIdentification8
import SettlementInstruction19

class GroupHeader130(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_ChrgsAcctAgt", "_ChrgsAcctAgtAcct", "_TtlChrgs", "_SttlmInstr", "_CreDtTm", "_ChrgsRqstr"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if type(value) != auto else self.make_default("ChrgsAcctAgt")

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = None

	@property
	def ChrgsAcctAgtAcct(self):
		return self._ChrgsAcctAgtAcct

	@ChrgsAcctAgtAcct.setter
	def ChrgsAcctAgtAcct(self, value):
		self._ChrgsAcctAgtAcct = value if type(value) != auto else self.make_default("ChrgsAcctAgtAcct")

	@ChrgsAcctAgtAcct.deleter
	def ChrgsAcctAgtAcct(self):
		del self._ChrgsAcctAgtAcct
		self._ChrgsAcctAgtAcct = None

	@property
	def TtlChrgs(self):
		return self._TtlChrgs

	@TtlChrgs.setter
	def TtlChrgs(self, value):
		self._TtlChrgs = value if type(value) != auto else self.make_default("TtlChrgs")

	@TtlChrgs.deleter
	def TtlChrgs(self):
		del self._TtlChrgs
		self._TtlChrgs = None

	@property
	def SttlmInstr(self):
		return self._SttlmInstr

	@SttlmInstr.setter
	def SttlmInstr(self, value):
		self._SttlmInstr = value if type(value) != auto else self.make_default("SttlmInstr")

	@SttlmInstr.deleter
	def SttlmInstr(self):
		del self._SttlmInstr
		self._SttlmInstr = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def ChrgsRqstr(self):
		return self._ChrgsRqstr

	@ChrgsRqstr.setter
	def ChrgsRqstr(self, value):
		self._ChrgsRqstr = value if type(value) != auto else self.make_default("ChrgsRqstr")

	@ChrgsRqstr.deleter
	def ChrgsRqstr(self):
		del self._ChrgsRqstr
		self._ChrgsRqstr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgs', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstr', type=SettlementInstruction19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsRqstr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

