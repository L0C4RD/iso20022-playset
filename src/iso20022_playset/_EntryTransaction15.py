# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AmountAndCurrencyExchange4
from . import BankTransactionCodeStructure4
from . import CardTransaction18
from . import CashAvailability1
from . import CashDeposit1
from . import Charges15
from . import CorporateAction82
from . import CreditDebitCode
from . import LocalInstrument2Choice
from . import Max20000Text
from . import Max500Text
from . import PaymentReturnReason8
from . import PaymentTypeInformation27
from . import Purpose2Choice
from . import RemittanceInformation22
from . import RemittanceLocation8
from . import SecuritiesAccount19
from . import SecurityIdentification19
from . import SupplementaryData1
from . import TaxData1
from . import TransactionAgents6
from . import TransactionAllocation1
from . import TransactionDates3
from . import TransactionInterest4
from . import TransactionParties12
from . import TransactionPrice4Choice
from . import TransactionQuantities4Choice
from . import TransactionReferences6

class EntryTransaction15(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxInf", "_Amt", "_AmtDtls", "_Avlbty", "_BkTxCd", "_CardTx", "_CdtDbtInd", "_Chrgs", "_CshDpst", "_FinInstrmId", "_InstrCpy", "_Intrst", "_LclInstrm", "_PmtTpInf", "_Purp", "_Refs", "_RltdAgts", "_RltdCorpActn", "_RltdDts", "_RltdPric", "_RltdPties", "_RltdQties", "_RltdRmtInf", "_RmtInf", "_RtrInf", "_SfkpgAcct", "_SplmtryData", "_Tax", "_UndrlygAllcn"]
	@property
	def AddtlTxInf(self):
		return self._AddtlTxInf

	@AddtlTxInf.setter
	def AddtlTxInf(self, value):
		self._AddtlTxInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxInf', Max500Text, False)

	@AddtlTxInf.deleter
	def AddtlTxInf(self):
		del self._AddtlTxInf
		self._AddtlTxInf = base_types.UninitialisedField(self, 'AddtlTxInf', Max500Text, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', AmountAndCurrencyExchange4, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', AmountAndCurrencyExchange4, False)

	@property
	def Avlbty(self):
		return self._Avlbty

	@Avlbty.setter
	def Avlbty(self, value):
		self._Avlbty = value if value is not None else base_types.UninitialisedField(self, 'Avlbty', CashAvailability1, True)

	@Avlbty.deleter
	def Avlbty(self):
		del self._Avlbty
		self._Avlbty = base_types.UninitialisedField(self, 'Avlbty', CashAvailability1, True)

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if value is not None else base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = base_types.UninitialisedField(self, 'BkTxCd', BankTransactionCodeStructure4, False)

	@property
	def CardTx(self):
		return self._CardTx

	@CardTx.setter
	def CardTx(self, value):
		self._CardTx = value if value is not None else base_types.UninitialisedField(self, 'CardTx', CardTransaction18, False)

	@CardTx.deleter
	def CardTx(self):
		del self._CardTx
		self._CardTx = base_types.UninitialisedField(self, 'CardTx', CardTransaction18, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', Charges15, False)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', Charges15, False)

	@property
	def CshDpst(self):
		return self._CshDpst

	@CshDpst.setter
	def CshDpst(self, value):
		self._CshDpst = value if value is not None else base_types.UninitialisedField(self, 'CshDpst', CashDeposit1, True)

	@CshDpst.deleter
	def CshDpst(self):
		del self._CshDpst
		self._CshDpst = base_types.UninitialisedField(self, 'CshDpst', CashDeposit1, True)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def InstrCpy(self):
		return self._InstrCpy

	@InstrCpy.setter
	def InstrCpy(self, value):
		self._InstrCpy = value if value is not None else base_types.UninitialisedField(self, 'InstrCpy', Max20000Text, False)

	@InstrCpy.deleter
	def InstrCpy(self):
		del self._InstrCpy
		self._InstrCpy = base_types.UninitialisedField(self, 'InstrCpy', Max20000Text, False)

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if value is not None else base_types.UninitialisedField(self, 'Intrst', TransactionInterest4, False)

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = base_types.UninitialisedField(self, 'Intrst', TransactionInterest4, False)

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if value is not None else base_types.UninitialisedField(self, 'LclInstrm', LocalInstrument2Choice, False)

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = base_types.UninitialisedField(self, 'LclInstrm', LocalInstrument2Choice, False)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation27, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation27, False)

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
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', TransactionReferences6, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', TransactionReferences6, False)

	@property
	def RltdAgts(self):
		return self._RltdAgts

	@RltdAgts.setter
	def RltdAgts(self, value):
		self._RltdAgts = value if value is not None else base_types.UninitialisedField(self, 'RltdAgts', TransactionAgents6, False)

	@RltdAgts.deleter
	def RltdAgts(self):
		del self._RltdAgts
		self._RltdAgts = base_types.UninitialisedField(self, 'RltdAgts', TransactionAgents6, False)

	@property
	def RltdCorpActn(self):
		return self._RltdCorpActn

	@RltdCorpActn.setter
	def RltdCorpActn(self, value):
		self._RltdCorpActn = value if value is not None else base_types.UninitialisedField(self, 'RltdCorpActn', CorporateAction82, False)

	@RltdCorpActn.deleter
	def RltdCorpActn(self):
		del self._RltdCorpActn
		self._RltdCorpActn = base_types.UninitialisedField(self, 'RltdCorpActn', CorporateAction82, False)

	@property
	def RltdDts(self):
		return self._RltdDts

	@RltdDts.setter
	def RltdDts(self, value):
		self._RltdDts = value if value is not None else base_types.UninitialisedField(self, 'RltdDts', TransactionDates3, False)

	@RltdDts.deleter
	def RltdDts(self):
		del self._RltdDts
		self._RltdDts = base_types.UninitialisedField(self, 'RltdDts', TransactionDates3, False)

	@property
	def RltdPric(self):
		return self._RltdPric

	@RltdPric.setter
	def RltdPric(self, value):
		self._RltdPric = value if value is not None else base_types.UninitialisedField(self, 'RltdPric', TransactionPrice4Choice, False)

	@RltdPric.deleter
	def RltdPric(self):
		del self._RltdPric
		self._RltdPric = base_types.UninitialisedField(self, 'RltdPric', TransactionPrice4Choice, False)

	@property
	def RltdPties(self):
		return self._RltdPties

	@RltdPties.setter
	def RltdPties(self, value):
		self._RltdPties = value if value is not None else base_types.UninitialisedField(self, 'RltdPties', TransactionParties12, False)

	@RltdPties.deleter
	def RltdPties(self):
		del self._RltdPties
		self._RltdPties = base_types.UninitialisedField(self, 'RltdPties', TransactionParties12, False)

	@property
	def RltdQties(self):
		return self._RltdQties

	@RltdQties.setter
	def RltdQties(self, value):
		self._RltdQties = value if value is not None else base_types.UninitialisedField(self, 'RltdQties', TransactionQuantities4Choice, True)

	@RltdQties.deleter
	def RltdQties(self):
		del self._RltdQties
		self._RltdQties = base_types.UninitialisedField(self, 'RltdQties', TransactionQuantities4Choice, True)

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if value is not None else base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, True)

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, True)

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if value is not None else base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation22, False)

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation22, False)

	@property
	def RtrInf(self):
		return self._RtrInf

	@RtrInf.setter
	def RtrInf(self, value):
		self._RtrInf = value if value is not None else base_types.UninitialisedField(self, 'RtrInf', PaymentReturnReason8, False)

	@RtrInf.deleter
	def RtrInf(self):
		del self._RtrInf
		self._RtrInf = base_types.UninitialisedField(self, 'RtrInf', PaymentReturnReason8, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

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
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', TaxData1, False)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', TaxData1, False)

	@property
	def UndrlygAllcn(self):
		return self._UndrlygAllcn

	@UndrlygAllcn.setter
	def UndrlygAllcn(self, value):
		self._UndrlygAllcn = value if value is not None else base_types.UninitialisedField(self, 'UndrlygAllcn', TransactionAllocation1, True)

	@UndrlygAllcn.deleter
	def UndrlygAllcn(self):
		del self._UndrlygAllcn
		self._UndrlygAllcn = base_types.UninitialisedField(self, 'UndrlygAllcn', TransactionAllocation1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=AmountAndCurrencyExchange4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardTx', type=CardTransaction18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDpst', type=CashDeposit1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpy', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=TransactionInterest4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=LocalInstrument2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=TransactionReferences6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAgts', type=TransactionAgents6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdCorpActn', type=CorporateAction82, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDts', type=TransactionDates3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPric', type=TransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPties', type=TransactionParties12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdQties', type=TransactionQuantities4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrInf', type=PaymentReturnReason8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tax', type=TaxData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygAllcn', type=TransactionAllocation1, min=0, max=None, mutex_group=None, array=True),
	))