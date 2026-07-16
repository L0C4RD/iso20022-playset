# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AmountAndCurrencyExchange4
from . import BankTransactionCodeStructure4
from . import CardEntry5
from . import CashAvailability1
from . import Charges15
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import EntryDetails16
from . import EntryStatus1Choice
from . import Max35Text
from . import Max500Text
from . import MessageIdentification2
from . import TechnicalInputChannel1Choice
from . import TransactionInterest4
from . import TrueFalseIndicator
from . import YesNoIndicator

class ReportEntry16(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrRef", "_AddtlInfInd", "_AddtlNtryInf", "_Amt", "_AmtDtls", "_Avlbty", "_BkTxCd", "_BookgDt", "_CardTx", "_CdtDbtInd", "_Chrgs", "_ComssnWvrInd", "_Intrst", "_NtryDtls", "_NtryRef", "_RvslInd", "_Sts", "_TechInptChanl", "_ValDt"]
	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrRef', Max35Text, False)

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = base_types.UninitialisedField(self, 'AcctSvcrRef', Max35Text, False)

	@property
	def AddtlInfInd(self):
		return self._AddtlInfInd

	@AddtlInfInd.setter
	def AddtlInfInd(self, value):
		self._AddtlInfInd = value if value is not None else base_types.UninitialisedField(self, 'AddtlInfInd', MessageIdentification2, False)

	@AddtlInfInd.deleter
	def AddtlInfInd(self):
		del self._AddtlInfInd
		self._AddtlInfInd = base_types.UninitialisedField(self, 'AddtlInfInd', MessageIdentification2, False)

	@property
	def AddtlNtryInf(self):
		return self._AddtlNtryInf

	@AddtlNtryInf.setter
	def AddtlNtryInf(self, value):
		self._AddtlNtryInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlNtryInf', Max500Text, False)

	@AddtlNtryInf.deleter
	def AddtlNtryInf(self):
		del self._AddtlNtryInf
		self._AddtlNtryInf = base_types.UninitialisedField(self, 'AddtlNtryInf', Max500Text, False)

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
	def BookgDt(self):
		return self._BookgDt

	@BookgDt.setter
	def BookgDt(self, value):
		self._BookgDt = value if value is not None else base_types.UninitialisedField(self, 'BookgDt', DateAndDateTime2Choice, False)

	@BookgDt.deleter
	def BookgDt(self):
		del self._BookgDt
		self._BookgDt = base_types.UninitialisedField(self, 'BookgDt', DateAndDateTime2Choice, False)

	@property
	def CardTx(self):
		return self._CardTx

	@CardTx.setter
	def CardTx(self, value):
		self._CardTx = value if value is not None else base_types.UninitialisedField(self, 'CardTx', CardEntry5, False)

	@CardTx.deleter
	def CardTx(self):
		del self._CardTx
		self._CardTx = base_types.UninitialisedField(self, 'CardTx', CardEntry5, False)

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
	def ComssnWvrInd(self):
		return self._ComssnWvrInd

	@ComssnWvrInd.setter
	def ComssnWvrInd(self, value):
		self._ComssnWvrInd = value if value is not None else base_types.UninitialisedField(self, 'ComssnWvrInd', YesNoIndicator, False)

	@ComssnWvrInd.deleter
	def ComssnWvrInd(self):
		del self._ComssnWvrInd
		self._ComssnWvrInd = base_types.UninitialisedField(self, 'ComssnWvrInd', YesNoIndicator, False)

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
	def NtryDtls(self):
		return self._NtryDtls

	@NtryDtls.setter
	def NtryDtls(self, value):
		self._NtryDtls = value if value is not None else base_types.UninitialisedField(self, 'NtryDtls', EntryDetails16, True)

	@NtryDtls.deleter
	def NtryDtls(self):
		del self._NtryDtls
		self._NtryDtls = base_types.UninitialisedField(self, 'NtryDtls', EntryDetails16, True)

	@property
	def NtryRef(self):
		return self._NtryRef

	@NtryRef.setter
	def NtryRef(self, value):
		self._NtryRef = value if value is not None else base_types.UninitialisedField(self, 'NtryRef', Max35Text, False)

	@NtryRef.deleter
	def NtryRef(self):
		del self._NtryRef
		self._NtryRef = base_types.UninitialisedField(self, 'NtryRef', Max35Text, False)

	@property
	def RvslInd(self):
		return self._RvslInd

	@RvslInd.setter
	def RvslInd(self, value):
		self._RvslInd = value if value is not None else base_types.UninitialisedField(self, 'RvslInd', TrueFalseIndicator, False)

	@RvslInd.deleter
	def RvslInd(self):
		del self._RvslInd
		self._RvslInd = base_types.UninitialisedField(self, 'RvslInd', TrueFalseIndicator, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', EntryStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', EntryStatus1Choice, False)

	@property
	def TechInptChanl(self):
		return self._TechInptChanl

	@TechInptChanl.setter
	def TechInptChanl(self, value):
		self._TechInptChanl = value if value is not None else base_types.UninitialisedField(self, 'TechInptChanl', TechnicalInputChannel1Choice, False)

	@TechInptChanl.deleter
	def TechInptChanl(self):
		del self._TechInptChanl
		self._TechInptChanl = base_types.UninitialisedField(self, 'TechInptChanl', TechnicalInputChannel1Choice, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

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