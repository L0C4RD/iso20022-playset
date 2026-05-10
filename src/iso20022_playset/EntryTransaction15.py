import base_types
import CreditDebitCode
import Max500Text
import TransactionInterest4
import TransactionDates3
import TransactionPrice4Choice
import TaxData1
import RemittanceLocation8
import LocalInstrument2Choice
import TransactionAgents6
import Purpose2Choice
import BankTransactionCodeStructure4
import SupplementaryData1
import CardTransaction18
import TransactionParties12
import CashAvailability1
import PaymentTypeInformation27
import AmountAndCurrencyExchange4
import Charges15
import PaymentReturnReason8
import ActiveOrHistoricCurrencyAndAmount
import Max20000Text
import TransactionAllocation1
import SecuritiesAccount19
import TransactionQuantities4Choice
import RemittanceInformation22
import CorporateAction82
import SecurityIdentification19
import TransactionReferences6
import CashDeposit1

class EntryTransaction15(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Avlbty", "_RltdPric", "_RtrInf", "_Refs", "_UndrlygAllcn", "_RltdRmtInf", "_Amt", "_PmtTpInf", "_BkTxCd", "_InstrCpy", "_CardTx", "_Intrst", "_LclInstrm", "_AddtlTxInf", "_CshDpst", "_FinInstrmId", "_RltdAgts", "_CdtDbtInd", "_RltdQties", "_Purp", "_RmtInf", "_AmtDtls", "_Tax", "_RltdDts", "_RltdCorpActn", "_SfkpgAcct", "_Chrgs", "_RltdPties"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Avlbty(self):
		return self._Avlbty

	@Avlbty.setter
	def Avlbty(self, value):
		self._Avlbty = value if type(value) != auto else self.make_default("Avlbty")

	@Avlbty.deleter
	def Avlbty(self):
		del self._Avlbty
		self._Avlbty = None

	@property
	def RltdPric(self):
		return self._RltdPric

	@RltdPric.setter
	def RltdPric(self, value):
		self._RltdPric = value if type(value) != auto else self.make_default("RltdPric")

	@RltdPric.deleter
	def RltdPric(self):
		del self._RltdPric
		self._RltdPric = None

	@property
	def RtrInf(self):
		return self._RtrInf

	@RtrInf.setter
	def RtrInf(self, value):
		self._RtrInf = value if type(value) != auto else self.make_default("RtrInf")

	@RtrInf.deleter
	def RtrInf(self):
		del self._RtrInf
		self._RtrInf = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def UndrlygAllcn(self):
		return self._UndrlygAllcn

	@UndrlygAllcn.setter
	def UndrlygAllcn(self, value):
		self._UndrlygAllcn = value if type(value) != auto else self.make_default("UndrlygAllcn")

	@UndrlygAllcn.deleter
	def UndrlygAllcn(self):
		del self._UndrlygAllcn
		self._UndrlygAllcn = None

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if type(value) != auto else self.make_default("RltdRmtInf")

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if type(value) != auto else self.make_default("BkTxCd")

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = None

	@property
	def InstrCpy(self):
		return self._InstrCpy

	@InstrCpy.setter
	def InstrCpy(self, value):
		self._InstrCpy = value if type(value) != auto else self.make_default("InstrCpy")

	@InstrCpy.deleter
	def InstrCpy(self):
		del self._InstrCpy
		self._InstrCpy = None

	@property
	def CardTx(self):
		return self._CardTx

	@CardTx.setter
	def CardTx(self, value):
		self._CardTx = value if type(value) != auto else self.make_default("CardTx")

	@CardTx.deleter
	def CardTx(self):
		del self._CardTx
		self._CardTx = None

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if type(value) != auto else self.make_default("LclInstrm")

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = None

	@property
	def AddtlTxInf(self):
		return self._AddtlTxInf

	@AddtlTxInf.setter
	def AddtlTxInf(self, value):
		self._AddtlTxInf = value if type(value) != auto else self.make_default("AddtlTxInf")

	@AddtlTxInf.deleter
	def AddtlTxInf(self):
		del self._AddtlTxInf
		self._AddtlTxInf = None

	@property
	def CshDpst(self):
		return self._CshDpst

	@CshDpst.setter
	def CshDpst(self, value):
		self._CshDpst = value if type(value) != auto else self.make_default("CshDpst")

	@CshDpst.deleter
	def CshDpst(self):
		del self._CshDpst
		self._CshDpst = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def RltdAgts(self):
		return self._RltdAgts

	@RltdAgts.setter
	def RltdAgts(self, value):
		self._RltdAgts = value if type(value) != auto else self.make_default("RltdAgts")

	@RltdAgts.deleter
	def RltdAgts(self):
		del self._RltdAgts
		self._RltdAgts = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def RltdQties(self):
		return self._RltdQties

	@RltdQties.setter
	def RltdQties(self, value):
		self._RltdQties = value if type(value) != auto else self.make_default("RltdQties")

	@RltdQties.deleter
	def RltdQties(self):
		del self._RltdQties
		self._RltdQties = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if type(value) != auto else self.make_default("RmtInf")

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def RltdDts(self):
		return self._RltdDts

	@RltdDts.setter
	def RltdDts(self, value):
		self._RltdDts = value if type(value) != auto else self.make_default("RltdDts")

	@RltdDts.deleter
	def RltdDts(self):
		del self._RltdDts
		self._RltdDts = None

	@property
	def RltdCorpActn(self):
		return self._RltdCorpActn

	@RltdCorpActn.setter
	def RltdCorpActn(self, value):
		self._RltdCorpActn = value if type(value) != auto else self.make_default("RltdCorpActn")

	@RltdCorpActn.deleter
	def RltdCorpActn(self):
		del self._RltdCorpActn
		self._RltdCorpActn = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def RltdPties(self):
		return self._RltdPties

	@RltdPties.setter
	def RltdPties(self, value):
		self._RltdPties = value if type(value) != auto else self.make_default("RltdPties")

	@RltdPties.deleter
	def RltdPties(self):
		del self._RltdPties
		self._RltdPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPric', type=TransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrInf', type=PaymentReturnReason8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=TransactionReferences6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAllcn', type=TransactionAllocation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpy', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardTx', type=CardTransaction18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=TransactionInterest4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDpst', type=CashDeposit1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAgts', type=TransactionAgents6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdQties', type=TransactionQuantities4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=AmountAndCurrencyExchange4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDts', type=TransactionDates3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdCorpActn', type=CorporateAction82, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPties', type=TransactionParties12, min=0, max=1, mutex_group=None, array=False),
	))

