# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import CreditTransferTransaction72
from . import CreditTransferTransaction80
from . import CryptographicKey1Choice
from . import ISODate
from . import ISODateTime
from . import InstructionForCreditorAgent3
from . import InstructionForNextAgent1
from . import PaymentIdentification13
from . import PaymentTypeInformation28
from . import Priority3Code
from . import Purpose2Choice
from . import RegulatoryReporting10
from . import RemittanceInformation2
from . import SettlementDateTimeIndication1
from . import SettlementTimeRequest2
from . import SupplementaryData1
from . import TransactionAllocation2

class CreditTransferTransaction79(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtAcct", "_InstdAgt", "_InstgAgt", "_InstrForCdtrAgt", "_InstrForNxtAgt", "_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_IntrmyAgt1", "_IntrmyAgt1Acct", "_IntrmyAgt2", "_IntrmyAgt2Acct", "_IntrmyAgt3", "_IntrmyAgt3Acct", "_PmtId", "_PmtSgntr", "_PmtTpInf", "_PrvsInstgAgt1", "_PrvsInstgAgt1Acct", "_PrvsInstgAgt2", "_PrvsInstgAgt2Acct", "_PrvsInstgAgt3", "_PrvsInstgAgt3Acct", "_Purp", "_RgltryRptg", "_RmtInf", "_SplmtryData", "_SttlmPrty", "_SttlmTmIndctn", "_SttlmTmReq", "_UltmtCdtr", "_UltmtDbtr", "_UndrlygAllcn", "_UndrlygCstmrCdtTrf", "_UndrlygFICdtTrf", "_XpryDtTm"]
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
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount40, False)

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount40, False)

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
	def InstrForNxtAgt(self):
		return self._InstrForNxtAgt

	@InstrForNxtAgt.setter
	def InstrForNxtAgt(self, value):
		self._InstrForNxtAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForNxtAgt', InstructionForNextAgent1, True)

	@InstrForNxtAgt.deleter
	def InstrForNxtAgt(self):
		del self._InstrForNxtAgt
		self._InstrForNxtAgt = base_types.UninitialisedField(self, 'InstrForNxtAgt', InstructionForNextAgent1, True)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveCurrencyAndAmount, False)

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
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if value is not None else base_types.UninitialisedField(self, 'PmtId', PaymentIdentification13, False)

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = base_types.UninitialisedField(self, 'PmtId', PaymentIdentification13, False)

	@property
	def PmtSgntr(self):
		return self._PmtSgntr

	@PmtSgntr.setter
	def PmtSgntr(self, value):
		self._PmtSgntr = value if value is not None else base_types.UninitialisedField(self, 'PmtSgntr', CryptographicKey1Choice, False)

	@PmtSgntr.deleter
	def PmtSgntr(self):
		del self._PmtSgntr
		self._PmtSgntr = base_types.UninitialisedField(self, 'PmtSgntr', CryptographicKey1Choice, False)

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
	def PrvsInstgAgt1(self):
		return self._PrvsInstgAgt1

	@PrvsInstgAgt1.setter
	def PrvsInstgAgt1(self, value):
		self._PrvsInstgAgt1 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@PrvsInstgAgt1.deleter
	def PrvsInstgAgt1(self):
		del self._PrvsInstgAgt1
		self._PrvsInstgAgt1 = base_types.UninitialisedField(self, 'PrvsInstgAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def PrvsInstgAgt1Acct(self):
		return self._PrvsInstgAgt1Acct

	@PrvsInstgAgt1Acct.setter
	def PrvsInstgAgt1Acct(self, value):
		self._PrvsInstgAgt1Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt1Acct', CashAccount40, False)

	@PrvsInstgAgt1Acct.deleter
	def PrvsInstgAgt1Acct(self):
		del self._PrvsInstgAgt1Acct
		self._PrvsInstgAgt1Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt1Acct', CashAccount40, False)

	@property
	def PrvsInstgAgt2(self):
		return self._PrvsInstgAgt2

	@PrvsInstgAgt2.setter
	def PrvsInstgAgt2(self, value):
		self._PrvsInstgAgt2 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@PrvsInstgAgt2.deleter
	def PrvsInstgAgt2(self):
		del self._PrvsInstgAgt2
		self._PrvsInstgAgt2 = base_types.UninitialisedField(self, 'PrvsInstgAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def PrvsInstgAgt2Acct(self):
		return self._PrvsInstgAgt2Acct

	@PrvsInstgAgt2Acct.setter
	def PrvsInstgAgt2Acct(self, value):
		self._PrvsInstgAgt2Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt2Acct', CashAccount40, False)

	@PrvsInstgAgt2Acct.deleter
	def PrvsInstgAgt2Acct(self):
		del self._PrvsInstgAgt2Acct
		self._PrvsInstgAgt2Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt2Acct', CashAccount40, False)

	@property
	def PrvsInstgAgt3(self):
		return self._PrvsInstgAgt3

	@PrvsInstgAgt3.setter
	def PrvsInstgAgt3(self, value):
		self._PrvsInstgAgt3 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@PrvsInstgAgt3.deleter
	def PrvsInstgAgt3(self):
		del self._PrvsInstgAgt3
		self._PrvsInstgAgt3 = base_types.UninitialisedField(self, 'PrvsInstgAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def PrvsInstgAgt3Acct(self):
		return self._PrvsInstgAgt3Acct

	@PrvsInstgAgt3Acct.setter
	def PrvsInstgAgt3Acct(self, value):
		self._PrvsInstgAgt3Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt3Acct', CashAccount40, False)

	@PrvsInstgAgt3Acct.deleter
	def PrvsInstgAgt3Acct(self):
		del self._PrvsInstgAgt3Acct
		self._PrvsInstgAgt3Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt3Acct', CashAccount40, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if value is not None else base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting10, True)

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting10, True)

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if value is not None else base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation2, False)

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation2, False)

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
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if value is not None else base_types.UninitialisedField(self, 'SttlmPrty', Priority3Code, False)

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = base_types.UninitialisedField(self, 'SttlmPrty', Priority3Code, False)

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
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if value is not None else base_types.UninitialisedField(self, 'SttlmTmReq', SettlementTimeRequest2, False)

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = base_types.UninitialisedField(self, 'SttlmTmReq', SettlementTimeRequest2, False)

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

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtDbtr', BranchAndFinancialInstitutionIdentification8, False)

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = base_types.UninitialisedField(self, 'UltmtDbtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def UndrlygAllcn(self):
		return self._UndrlygAllcn

	@UndrlygAllcn.setter
	def UndrlygAllcn(self, value):
		self._UndrlygAllcn = value if value is not None else base_types.UninitialisedField(self, 'UndrlygAllcn', TransactionAllocation2, True)

	@UndrlygAllcn.deleter
	def UndrlygAllcn(self):
		del self._UndrlygAllcn
		self._UndrlygAllcn = base_types.UninitialisedField(self, 'UndrlygAllcn', TransactionAllocation2, True)

	@property
	def UndrlygCstmrCdtTrf(self):
		return self._UndrlygCstmrCdtTrf

	@UndrlygCstmrCdtTrf.setter
	def UndrlygCstmrCdtTrf(self, value):
		self._UndrlygCstmrCdtTrf = value if value is not None else base_types.UninitialisedField(self, 'UndrlygCstmrCdtTrf', CreditTransferTransaction72, False)

	@UndrlygCstmrCdtTrf.deleter
	def UndrlygCstmrCdtTrf(self):
		del self._UndrlygCstmrCdtTrf
		self._UndrlygCstmrCdtTrf = base_types.UninitialisedField(self, 'UndrlygCstmrCdtTrf', CreditTransferTransaction72, False)

	@property
	def UndrlygFICdtTrf(self):
		return self._UndrlygFICdtTrf

	@UndrlygFICdtTrf.setter
	def UndrlygFICdtTrf(self, value):
		self._UndrlygFICdtTrf = value if value is not None else base_types.UninitialisedField(self, 'UndrlygFICdtTrf', CreditTransferTransaction80, False)

	@UndrlygFICdtTrf.deleter
	def UndrlygFICdtTrf(self):
		del self._UndrlygFICdtTrf
		self._UndrlygFICdtTrf = base_types.UninitialisedField(self, 'UndrlygFICdtTrf', CreditTransferTransaction80, False)

	@property
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if value is not None else base_types.UninitialisedField(self, 'XpryDtTm', ISODateTime, False)

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = base_types.UninitialisedField(self, 'XpryDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForCdtrAgt', type=InstructionForCreditorAgent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrForNxtAgt', type=InstructionForNextAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSgntr', type=CryptographicKey1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting10, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAllcn', type=TransactionAllocation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygCstmrCdtTrf', type=CreditTransferTransaction72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygFICdtTrf', type=CreditTransferTransaction80, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))