from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._AmountAndCurrencyExchange4 import AmountAndCurrencyExchange4
from ._BankTransactionCodeStructure4 import BankTransactionCodeStructure4
from ._CardEntry5 import CardEntry5
from ._CashAvailability1 import CashAvailability1
from ._Charges15 import Charges15
from ._CreditDebitCode import CreditDebitCode
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._EntryDetails16 import EntryDetails16
from ._EntryStatus1Choice import EntryStatus1Choice
from ._Max35Text import Max35Text
from ._Max500Text import Max500Text
from ._MessageIdentification2 import MessageIdentification2
from ._TechnicalInputChannel1Choice import TechnicalInputChannel1Choice
from ._TransactionInterest4 import TransactionInterest4
from ._TrueFalseIndicator import TrueFalseIndicator
from ._YesNoIndicator import YesNoIndicator

class ReportEntry16(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrRef", "_AddtlInfInd", "_AddtlNtryInf", "_Amt", "_AmtDtls", "_Avlbty", "_BkTxCd", "_BookgDt", "_CardTx", "_CdtDbtInd", "_Chrgs", "_ComssnWvrInd", "_Intrst", "_NtryDtls", "_NtryRef", "_RvslInd", "_Sts", "_TechInptChanl", "_ValDt"]
	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if type(value) != base_types.auto else self.make_default("AcctSvcrRef")

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = None

	@property
	def AddtlInfInd(self):
		return self._AddtlInfInd

	@AddtlInfInd.setter
	def AddtlInfInd(self, value):
		self._AddtlInfInd = value if type(value) != base_types.auto else self.make_default("AddtlInfInd")

	@AddtlInfInd.deleter
	def AddtlInfInd(self):
		del self._AddtlInfInd
		self._AddtlInfInd = None

	@property
	def AddtlNtryInf(self):
		return self._AddtlNtryInf

	@AddtlNtryInf.setter
	def AddtlNtryInf(self, value):
		self._AddtlNtryInf = value if type(value) != base_types.auto else self.make_default("AddtlNtryInf")

	@AddtlNtryInf.deleter
	def AddtlNtryInf(self):
		del self._AddtlNtryInf
		self._AddtlNtryInf = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != base_types.auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def Avlbty(self):
		return self._Avlbty

	@Avlbty.setter
	def Avlbty(self, value):
		self._Avlbty = value if type(value) != base_types.auto else self.make_default("Avlbty")

	@Avlbty.deleter
	def Avlbty(self):
		del self._Avlbty
		self._Avlbty = None

	@property
	def BkTxCd(self):
		return self._BkTxCd

	@BkTxCd.setter
	def BkTxCd(self, value):
		self._BkTxCd = value if type(value) != base_types.auto else self.make_default("BkTxCd")

	@BkTxCd.deleter
	def BkTxCd(self):
		del self._BkTxCd
		self._BkTxCd = None

	@property
	def BookgDt(self):
		return self._BookgDt

	@BookgDt.setter
	def BookgDt(self, value):
		self._BookgDt = value if type(value) != base_types.auto else self.make_default("BookgDt")

	@BookgDt.deleter
	def BookgDt(self):
		del self._BookgDt
		self._BookgDt = None

	@property
	def CardTx(self):
		return self._CardTx

	@CardTx.setter
	def CardTx(self, value):
		self._CardTx = value if type(value) != base_types.auto else self.make_default("CardTx")

	@CardTx.deleter
	def CardTx(self):
		del self._CardTx
		self._CardTx = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != base_types.auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def ComssnWvrInd(self):
		return self._ComssnWvrInd

	@ComssnWvrInd.setter
	def ComssnWvrInd(self, value):
		self._ComssnWvrInd = value if type(value) != base_types.auto else self.make_default("ComssnWvrInd")

	@ComssnWvrInd.deleter
	def ComssnWvrInd(self):
		del self._ComssnWvrInd
		self._ComssnWvrInd = None

	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != base_types.auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def NtryDtls(self):
		return self._NtryDtls

	@NtryDtls.setter
	def NtryDtls(self, value):
		self._NtryDtls = value if type(value) != base_types.auto else self.make_default("NtryDtls")

	@NtryDtls.deleter
	def NtryDtls(self):
		del self._NtryDtls
		self._NtryDtls = None

	@property
	def NtryRef(self):
		return self._NtryRef

	@NtryRef.setter
	def NtryRef(self, value):
		self._NtryRef = value if type(value) != base_types.auto else self.make_default("NtryRef")

	@NtryRef.deleter
	def NtryRef(self):
		del self._NtryRef
		self._NtryRef = None

	@property
	def RvslInd(self):
		return self._RvslInd

	@RvslInd.setter
	def RvslInd(self, value):
		self._RvslInd = value if type(value) != base_types.auto else self.make_default("RvslInd")

	@RvslInd.deleter
	def RvslInd(self):
		del self._RvslInd
		self._RvslInd = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def TechInptChanl(self):
		return self._TechInptChanl

	@TechInptChanl.setter
	def TechInptChanl(self, value):
		self._TechInptChanl = value if type(value) != base_types.auto else self.make_default("TechInptChanl")

	@TechInptChanl.deleter
	def TechInptChanl(self):
		del self._TechInptChanl
		self._TechInptChanl = None

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
		base_types.FieldEntry(name='AcctSvcrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInfInd', type=MessageIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlNtryInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtDtls', type=AmountAndCurrencyExchange4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Avlbty', type=CashAvailability1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkTxCd', type=BankTransactionCodeStructure4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookgDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardTx', type=CardEntry5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=Charges15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnWvrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=TransactionInterest4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryDtls', type=EntryDetails16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=EntryStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechInptChanl', type=TechnicalInputChannel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

