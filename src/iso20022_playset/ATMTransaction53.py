import base_types
import TransactionIdentifier3
import ATMTransactionAmounts6
import Max70Text
import AuthorisationResult20
import Max10000Binary
import DetailedAmount12
import DetailedAmount13
import Max35Text
import ImpliedCurrencyAndAmount
import TrueFalseIndicator
import CardAccount17
import AmountAndCurrency1
import CurrencyConversion32
import ATMCassette3
import ATMTotals4
import ATMTransactionStatus1Code
import ATMTransactionStatus2Code
import FailureReason9Code
import ContentInformationType10

class ATMTransaction53(base_types._BaseFieldType):

	__slots__ = ["_ATMTtls", "_MultiBndl", "_CcyConvsRslt", "_IncdntDtl", "_DtldReqdAmt", "_AddtlChrg", "_CstmrCnsnt", "_Incdnt", "_TtlAuthrsdAmt", "_AcctData", "_Lmts", "_Csstt", "_TxId", "_AuthstnRslt", "_TtlReqdAmt", "_RctPrtd", "_TxSts", "_BndlPresntdAmt", "_TtlPresntdAmt", "_ICCRltdData", "_PrtctdAcctData", "_RcncltnId", "_ReqdRct", "_PresntdAmtSts"]
	@property
	def ATMTtls(self):
		return self._ATMTtls

	@ATMTtls.setter
	def ATMTtls(self, value):
		self._ATMTtls = value if type(value) != auto else self.make_default("ATMTtls")

	@ATMTtls.deleter
	def ATMTtls(self):
		del self._ATMTtls
		self._ATMTtls = None

	@property
	def MultiBndl(self):
		return self._MultiBndl

	@MultiBndl.setter
	def MultiBndl(self, value):
		self._MultiBndl = value if type(value) != auto else self.make_default("MultiBndl")

	@MultiBndl.deleter
	def MultiBndl(self):
		del self._MultiBndl
		self._MultiBndl = None

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if type(value) != auto else self.make_default("CcyConvsRslt")

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = None

	@property
	def IncdntDtl(self):
		return self._IncdntDtl

	@IncdntDtl.setter
	def IncdntDtl(self, value):
		self._IncdntDtl = value if type(value) != auto else self.make_default("IncdntDtl")

	@IncdntDtl.deleter
	def IncdntDtl(self):
		del self._IncdntDtl
		self._IncdntDtl = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def AddtlChrg(self):
		return self._AddtlChrg

	@AddtlChrg.setter
	def AddtlChrg(self, value):
		self._AddtlChrg = value if type(value) != auto else self.make_default("AddtlChrg")

	@AddtlChrg.deleter
	def AddtlChrg(self):
		del self._AddtlChrg
		self._AddtlChrg = None

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if type(value) != auto else self.make_default("CstmrCnsnt")

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = None

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if type(value) != auto else self.make_default("Incdnt")

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = None

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if type(value) != auto else self.make_default("TtlAuthrsdAmt")

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = None

	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	@property
	def Lmts(self):
		return self._Lmts

	@Lmts.setter
	def Lmts(self, value):
		self._Lmts = value if type(value) != auto else self.make_default("Lmts")

	@Lmts.deleter
	def Lmts(self):
		del self._Lmts
		self._Lmts = None

	@property
	def Csstt(self):
		return self._Csstt

	@Csstt.setter
	def Csstt(self, value):
		self._Csstt = value if type(value) != auto else self.make_default("Csstt")

	@Csstt.deleter
	def Csstt(self):
		del self._Csstt
		self._Csstt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if type(value) != auto else self.make_default("TtlReqdAmt")

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = None

	@property
	def RctPrtd(self):
		return self._RctPrtd

	@RctPrtd.setter
	def RctPrtd(self, value):
		self._RctPrtd = value if type(value) != auto else self.make_default("RctPrtd")

	@RctPrtd.deleter
	def RctPrtd(self):
		del self._RctPrtd
		self._RctPrtd = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def BndlPresntdAmt(self):
		return self._BndlPresntdAmt

	@BndlPresntdAmt.setter
	def BndlPresntdAmt(self, value):
		self._BndlPresntdAmt = value if type(value) != auto else self.make_default("BndlPresntdAmt")

	@BndlPresntdAmt.deleter
	def BndlPresntdAmt(self):
		del self._BndlPresntdAmt
		self._BndlPresntdAmt = None

	@property
	def TtlPresntdAmt(self):
		return self._TtlPresntdAmt

	@TtlPresntdAmt.setter
	def TtlPresntdAmt(self, value):
		self._TtlPresntdAmt = value if type(value) != auto else self.make_default("TtlPresntdAmt")

	@TtlPresntdAmt.deleter
	def TtlPresntdAmt(self):
		del self._TtlPresntdAmt
		self._TtlPresntdAmt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if type(value) != auto else self.make_default("ReqdRct")

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = None

	@property
	def PresntdAmtSts(self):
		return self._PresntdAmtSts

	@PresntdAmtSts.setter
	def PresntdAmtSts(self, value):
		self._PresntdAmtSts = value if type(value) != auto else self.make_default("PresntdAmtSts")

	@PresntdAmtSts.deleter
	def PresntdAmtSts(self):
		del self._PresntdAmtSts
		self._PresntdAmtSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMTtls', type=ATMTotals4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MultiBndl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncdntDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctData', type=CardAccount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=ATMTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BndlPresntdAmt', type=ImpliedCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlPresntdAmt', type=AmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntdAmtSts', type=ATMTransactionStatus2Code, min=1, max=1, mutex_group=None, array=False),
	))

