# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BatchBookingIndicator
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import DirectDebitTransactionInformation33
from . import ISODate
from . import InstructionForCreditorAgent3
from . import Max35Text
from . import PaymentTypeInformation28
from . import SettlementDateTimeIndication1
from . import SupplementaryData1

class CreditTransferTransaction66(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_CdtId", "_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_DrctDbtTxInf", "_InstdAgt", "_InstgAgt", "_InstrForCdtrAgt", "_IntrBkSttlmDt", "_IntrmyAgt1", "_IntrmyAgt1Acct", "_IntrmyAgt2", "_IntrmyAgt2Acct", "_IntrmyAgt3", "_IntrmyAgt3Acct", "_PmtTpInf", "_SplmtryData", "_SttlmTmIndctn", "_TtlIntrBkSttlmAmt", "_UltmtCdtr"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if value is not None else base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

	@property
	def CdtId(self):
		return self._CdtId

	@CdtId.setter
	def CdtId(self, value):
		self._CdtId = value if value is not None else base_types.UninitialisedField(self, 'CdtId', Max35Text, False)

	@CdtId.deleter
	def CdtId(self):
		del self._CdtId
		self._CdtId = base_types.UninitialisedField(self, 'CdtId', Max35Text, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount40, False)

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount40, False)

	@property
	def DrctDbtTxInf(self):
		return self._DrctDbtTxInf

	@DrctDbtTxInf.setter
	def DrctDbtTxInf(self, value):
		self._DrctDbtTxInf = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation33, True)

	@DrctDbtTxInf.deleter
	def DrctDbtTxInf(self):
		del self._DrctDbtTxInf
		self._DrctDbtTxInf = base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation33, True)

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InstrForCdtrAgt(self):
		return self._InstrForCdtrAgt

	@InstrForCdtrAgt.setter
	def InstrForCdtrAgt(self, value):
		self._InstrForCdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForCdtrAgt', InstructionForCreditorAgent3, True)

	@InstrForCdtrAgt.deleter
	def InstrForCdtrAgt(self):
		del self._InstrForCdtrAgt
		self._InstrForCdtrAgt = base_types.UninitialisedField(self, 'InstrForCdtrAgt', InstructionForCreditorAgent3, True)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt1Acct', CashAccount40, False)

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = base_types.UninitialisedField(self, 'IntrmyAgt1Acct', CashAccount40, False)

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt2Acct', CashAccount40, False)

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = base_types.UninitialisedField(self, 'IntrmyAgt2Acct', CashAccount40, False)

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt3Acct', CashAccount40, False)

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = base_types.UninitialisedField(self, 'IntrmyAgt3Acct', CashAccount40, False)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation28, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation28, False)

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

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if value is not None else base_types.UninitialisedField(self, 'SttlmTmIndctn', SettlementDateTimeIndication1, False)

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = base_types.UninitialisedField(self, 'SttlmTmIndctn', SettlementDateTimeIndication1, False)

	@property
	def TtlIntrBkSttlmAmt(self):
		return self._TtlIntrBkSttlmAmt

	@TtlIntrBkSttlmAmt.setter
	def TtlIntrBkSttlmAmt(self, value):
		self._TtlIntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlIntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

	@TtlIntrBkSttlmAmt.deleter
	def TtlIntrBkSttlmAmt(self):
		del self._TtlIntrBkSttlmAmt
		self._TtlIntrBkSttlmAmt = base_types.UninitialisedField(self, 'TtlIntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtCdtr', BranchAndFinancialInstitutionIdentification8, False)

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = base_types.UninitialisedField(self, 'UltmtCdtr', BranchAndFinancialInstitutionIdentification8, False)

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