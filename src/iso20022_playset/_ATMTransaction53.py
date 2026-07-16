# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassette3
from . import ATMTotals4
from . import ATMTransactionAmounts6
from . import ATMTransactionStatus1Code
from . import ATMTransactionStatus2Code
from . import AmountAndCurrency1
from . import AuthorisationResult20
from . import CardAccount17
from . import ContentInformationType10
from . import CurrencyConversion32
from . import DetailedAmount12
from . import DetailedAmount13
from . import FailureReason9Code
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction53(base_types._BaseFieldType):

	__slots__ = ["_ATMTtls", "_AcctData", "_AddtlChrg", "_AuthstnRslt", "_BndlPresntdAmt", "_CcyConvsRslt", "_Csstt", "_CstmrCnsnt", "_DtldReqdAmt", "_ICCRltdData", "_Incdnt", "_IncdntDtl", "_Lmts", "_MultiBndl", "_PresntdAmtSts", "_PrtctdAcctData", "_RcncltnId", "_RctPrtd", "_ReqdRct", "_TtlAuthrsdAmt", "_TtlPresntdAmt", "_TtlReqdAmt", "_TxId", "_TxSts"]
	@property
	def ATMTtls(self):
		return self._ATMTtls

	@ATMTtls.setter
	def ATMTtls(self, value):
		self._ATMTtls = value if value is not None else base_types.UninitialisedField(self, 'ATMTtls', ATMTotals4, True)

	@ATMTtls.deleter
	def ATMTtls(self):
		del self._ATMTtls
		self._ATMTtls = base_types.UninitialisedField(self, 'ATMTtls', ATMTotals4, True)

	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if value is not None else base_types.UninitialisedField(self, 'AcctData', CardAccount17, False)

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = base_types.UninitialisedField(self, 'AcctData', CardAccount17, False)

	@property
	def AddtlChrg(self):
		return self._AddtlChrg

	@AddtlChrg.setter
	def AddtlChrg(self, value):
		self._AddtlChrg = value if value is not None else base_types.UninitialisedField(self, 'AddtlChrg', DetailedAmount13, True)

	@AddtlChrg.deleter
	def AddtlChrg(self):
		del self._AddtlChrg
		self._AddtlChrg = base_types.UninitialisedField(self, 'AddtlChrg', DetailedAmount13, True)

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult20, False)

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult20, False)

	@property
	def BndlPresntdAmt(self):
		return self._BndlPresntdAmt

	@BndlPresntdAmt.setter
	def BndlPresntdAmt(self, value):
		self._BndlPresntdAmt = value if value is not None else base_types.UninitialisedField(self, 'BndlPresntdAmt', ImpliedCurrencyAndAmount, True)

	@BndlPresntdAmt.deleter
	def BndlPresntdAmt(self):
		del self._BndlPresntdAmt
		self._BndlPresntdAmt = base_types.UninitialisedField(self, 'BndlPresntdAmt', ImpliedCurrencyAndAmount, True)

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion32, False)

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion32, False)

	@property
	def Csstt(self):
		return self._Csstt

	@Csstt.setter
	def Csstt(self, value):
		self._Csstt = value if value is not None else base_types.UninitialisedField(self, 'Csstt', ATMCassette3, True)

	@Csstt.deleter
	def Csstt(self):
		del self._Csstt
		self._Csstt = base_types.UninitialisedField(self, 'Csstt', ATMCassette3, True)

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if value is not None else base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount12, False)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount12, False)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if value is not None else base_types.UninitialisedField(self, 'Incdnt', FailureReason9Code, True)

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = base_types.UninitialisedField(self, 'Incdnt', FailureReason9Code, True)

	@property
	def IncdntDtl(self):
		return self._IncdntDtl

	@IncdntDtl.setter
	def IncdntDtl(self, value):
		self._IncdntDtl = value if value is not None else base_types.UninitialisedField(self, 'IncdntDtl', Max70Text, True)

	@IncdntDtl.deleter
	def IncdntDtl(self):
		del self._IncdntDtl
		self._IncdntDtl = base_types.UninitialisedField(self, 'IncdntDtl', Max70Text, True)

	@property
	def Lmts(self):
		return self._Lmts

	@Lmts.setter
	def Lmts(self, value):
		self._Lmts = value if value is not None else base_types.UninitialisedField(self, 'Lmts', ATMTransactionAmounts6, False)

	@Lmts.deleter
	def Lmts(self):
		del self._Lmts
		self._Lmts = base_types.UninitialisedField(self, 'Lmts', ATMTransactionAmounts6, False)

	@property
	def MultiBndl(self):
		return self._MultiBndl

	@MultiBndl.setter
	def MultiBndl(self, value):
		self._MultiBndl = value if value is not None else base_types.UninitialisedField(self, 'MultiBndl', TrueFalseIndicator, False)

	@MultiBndl.deleter
	def MultiBndl(self):
		del self._MultiBndl
		self._MultiBndl = base_types.UninitialisedField(self, 'MultiBndl', TrueFalseIndicator, False)

	@property
	def PresntdAmtSts(self):
		return self._PresntdAmtSts

	@PresntdAmtSts.setter
	def PresntdAmtSts(self, value):
		self._PresntdAmtSts = value if value is not None else base_types.UninitialisedField(self, 'PresntdAmtSts', ATMTransactionStatus2Code, False)

	@PresntdAmtSts.deleter
	def PresntdAmtSts(self):
		del self._PresntdAmtSts
		self._PresntdAmtSts = base_types.UninitialisedField(self, 'PresntdAmtSts', ATMTransactionStatus2Code, False)

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, False)

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, False)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def RctPrtd(self):
		return self._RctPrtd

	@RctPrtd.setter
	def RctPrtd(self, value):
		self._RctPrtd = value if value is not None else base_types.UninitialisedField(self, 'RctPrtd', TrueFalseIndicator, False)

	@RctPrtd.deleter
	def RctPrtd(self):
		del self._RctPrtd
		self._RctPrtd = base_types.UninitialisedField(self, 'RctPrtd', TrueFalseIndicator, False)

	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if value is not None else base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TtlPresntdAmt(self):
		return self._TtlPresntdAmt

	@TtlPresntdAmt.setter
	def TtlPresntdAmt(self, value):
		self._TtlPresntdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlPresntdAmt', AmountAndCurrency1, False)

	@TtlPresntdAmt.deleter
	def TtlPresntdAmt(self):
		del self._TtlPresntdAmt
		self._TtlPresntdAmt = base_types.UninitialisedField(self, 'TtlPresntdAmt', AmountAndCurrency1, False)

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, False)

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', ATMTransactionStatus1Code, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', ATMTransactionStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMTtls', type=ATMTotals4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctData', type=CardAccount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BndlPresntdAmt', type=ImpliedCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncdntDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MultiBndl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntdAmtSts', type=ATMTransactionStatus2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPresntdAmt', type=AmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=ATMTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))