# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._ChargesBreakdown1 import ChargesBreakdown1
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._InstructionForInstructedAgent1 import InstructionForInstructedAgent1
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._PartyIdentification272 import PartyIdentification272
from ._SettlementInstruction19 import SettlementInstruction19
from ._TotalCharges8 import TotalCharges8
from ._TransactionReferences7 import TransactionReferences7

class ChargesPerTransactionRecord6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ChrgsAcctAgt", "_ChrgsAcctAgtAcct", "_ChrgsBrkdwn", "_ChrgsRqstr", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtAcct", "_InstrForInstdAgt", "_RcrdId", "_SttlmInstr", "_TtlChrgsPerRcrd", "_UndrlygTx", "_ValDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if type(value) != base_types.auto else self.make_default("ChrgsAcctAgt")

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = None

	@property
	def ChrgsAcctAgtAcct(self):
		return self._ChrgsAcctAgtAcct

	@ChrgsAcctAgtAcct.setter
	def ChrgsAcctAgtAcct(self, value):
		self._ChrgsAcctAgtAcct = value if type(value) != base_types.auto else self.make_default("ChrgsAcctAgtAcct")

	@ChrgsAcctAgtAcct.deleter
	def ChrgsAcctAgtAcct(self):
		del self._ChrgsAcctAgtAcct
		self._ChrgsAcctAgtAcct = None

	@property
	def ChrgsBrkdwn(self):
		return self._ChrgsBrkdwn

	@ChrgsBrkdwn.setter
	def ChrgsBrkdwn(self, value):
		self._ChrgsBrkdwn = value if type(value) != base_types.auto else self.make_default("ChrgsBrkdwn")

	@ChrgsBrkdwn.deleter
	def ChrgsBrkdwn(self):
		del self._ChrgsBrkdwn
		self._ChrgsBrkdwn = None

	@property
	def ChrgsRqstr(self):
		return self._ChrgsRqstr

	@ChrgsRqstr.setter
	def ChrgsRqstr(self, value):
		self._ChrgsRqstr = value if type(value) != base_types.auto else self.make_default("ChrgsRqstr")

	@ChrgsRqstr.deleter
	def ChrgsRqstr(self):
		del self._ChrgsRqstr
		self._ChrgsRqstr = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != base_types.auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

	@property
	def InstrForInstdAgt(self):
		return self._InstrForInstdAgt

	@InstrForInstdAgt.setter
	def InstrForInstdAgt(self, value):
		self._InstrForInstdAgt = value if type(value) != base_types.auto else self.make_default("InstrForInstdAgt")

	@InstrForInstdAgt.deleter
	def InstrForInstdAgt(self):
		del self._InstrForInstdAgt
		self._InstrForInstdAgt = None

	@property
	def RcrdId(self):
		return self._RcrdId

	@RcrdId.setter
	def RcrdId(self, value):
		self._RcrdId = value if type(value) != base_types.auto else self.make_default("RcrdId")

	@RcrdId.deleter
	def RcrdId(self):
		del self._RcrdId
		self._RcrdId = None

	@property
	def SttlmInstr(self):
		return self._SttlmInstr

	@SttlmInstr.setter
	def SttlmInstr(self, value):
		self._SttlmInstr = value if type(value) != base_types.auto else self.make_default("SttlmInstr")

	@SttlmInstr.deleter
	def SttlmInstr(self):
		del self._SttlmInstr
		self._SttlmInstr = None

	@property
	def TtlChrgsPerRcrd(self):
		return self._TtlChrgsPerRcrd

	@TtlChrgsPerRcrd.setter
	def TtlChrgsPerRcrd(self, value):
		self._TtlChrgsPerRcrd = value if type(value) != base_types.auto else self.make_default("TtlChrgsPerRcrd")

	@TtlChrgsPerRcrd.deleter
	def TtlChrgsPerRcrd(self):
		del self._TtlChrgsPerRcrd
		self._TtlChrgsPerRcrd = None

	@property
	def UndrlygTx(self):
		return self._UndrlygTx

	@UndrlygTx.setter
	def UndrlygTx(self, value):
		self._UndrlygTx = value if type(value) != base_types.auto else self.make_default("UndrlygTx")

	@UndrlygTx.deleter
	def UndrlygTx(self):
		del self._UndrlygTx
		self._UndrlygTx = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsBrkdwn', type=ChargesBreakdown1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgsRqstr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForInstdAgt', type=InstructionForInstructedAgent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstr', type=SettlementInstruction19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsPerRcrd', type=TotalCharges8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTx', type=TransactionReferences7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))