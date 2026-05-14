# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BatchBookingIndicator import BatchBookingIndicator
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._DirectDebitTransactionInformation33 import DirectDebitTransactionInformation33
from ._ISODate import ISODate
from ._InstructionForCreditorAgent3 import InstructionForCreditorAgent3
from ._Max35Text import Max35Text
from ._PaymentTypeInformation28 import PaymentTypeInformation28
from ._SettlementDateTimeIndication1 import SettlementDateTimeIndication1
from ._SupplementaryData1 import SupplementaryData1

class CreditTransferTransaction66(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_CdtId", "_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_DrctDbtTxInf", "_InstdAgt", "_InstgAgt", "_InstrForCdtrAgt", "_IntrBkSttlmDt", "_IntrmyAgt1", "_IntrmyAgt1Acct", "_IntrmyAgt2", "_IntrmyAgt2Acct", "_IntrmyAgt3", "_IntrmyAgt3Acct", "_PmtTpInf", "_SplmtryData", "_SttlmTmIndctn", "_TtlIntrBkSttlmAmt", "_UltmtCdtr"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if type(value) != base_types.auto else self.make_default("BtchBookg")

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = None

	@property
	def CdtId(self):
		return self._CdtId

	@CdtId.setter
	def CdtId(self, value):
		self._CdtId = value if type(value) != base_types.auto else self.make_default("CdtId")

	@CdtId.deleter
	def CdtId(self):
		del self._CdtId
		self._CdtId = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != base_types.auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if type(value) != base_types.auto else self.make_default("CdtrAgtAcct")

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = None

	@property
	def DrctDbtTxInf(self):
		return self._DrctDbtTxInf

	@DrctDbtTxInf.setter
	def DrctDbtTxInf(self, value):
		self._DrctDbtTxInf = value if type(value) != base_types.auto else self.make_default("DrctDbtTxInf")

	@DrctDbtTxInf.deleter
	def DrctDbtTxInf(self):
		del self._DrctDbtTxInf
		self._DrctDbtTxInf = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != base_types.auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != base_types.auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def InstrForCdtrAgt(self):
		return self._InstrForCdtrAgt

	@InstrForCdtrAgt.setter
	def InstrForCdtrAgt(self, value):
		self._InstrForCdtrAgt = value if type(value) != base_types.auto else self.make_default("InstrForCdtrAgt")

	@InstrForCdtrAgt.deleter
	def InstrForCdtrAgt(self):
		del self._InstrForCdtrAgt
		self._InstrForCdtrAgt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt1Acct")

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = None

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt2Acct")

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = None

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt3")

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = None

	@property
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if type(value) != base_types.auto else self.make_default("IntrmyAgt3Acct")

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

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

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if type(value) != base_types.auto else self.make_default("SttlmTmIndctn")

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = None

	@property
	def TtlIntrBkSttlmAmt(self):
		return self._TtlIntrBkSttlmAmt

	@TtlIntrBkSttlmAmt.setter
	def TtlIntrBkSttlmAmt(self, value):
		self._TtlIntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("TtlIntrBkSttlmAmt")

	@TtlIntrBkSttlmAmt.deleter
	def TtlIntrBkSttlmAmt(self):
		del self._TtlIntrBkSttlmAmt
		self._TtlIntrBkSttlmAmt = None

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != base_types.auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchBookg', type=BatchBookingIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtTxInf', type=DirectDebitTransactionInformation33, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForCdtrAgt', type=InstructionForCreditorAgent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))