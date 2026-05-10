from . import base_types
from ._DetailedAmount13 import DetailedAmount13
from ._ATMMediaMix1 import ATMMediaMix1
from ._CurrencyConversion32 import CurrencyConversion32
from ._ContentInformationType10 import ContentInformationType10
from ._ATMTransactionAmounts6 import ATMTransactionAmounts6
from ._Max10000Binary import Max10000Binary
from ._AuthorisationResult20 import AuthorisationResult20
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ATMCommand7 import ATMCommand7
from ._AmountAndCurrency1 import AmountAndCurrency1
from ._CardAccount18 import CardAccount18
from ._DetailedAmount12 import DetailedAmount12
from ._TransactionIdentifier3 import TransactionIdentifier3
from ._Max35Text import Max35Text
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._CardAccount22 import CardAccount22

class ATMTransaction49(base_types._BaseFieldType):

	__slots__ = ["_Lmts", "_AddtlChrg", "_CmpltnReqrd", "_AcctData", "_TtlAuthrsdAmt", "_Cmd", "_MixTp", "_AuthstnRslt", "_ICCRltdData", "_TxId", "_DtldReqdAmt", "_TtlReqdAmt", "_PrtctdAcctData", "_AcctInf", "_Mix", "_RcncltnId", "_CcyConvsElgblty"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != base_types.auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	@property
	def AcctInf(self):
		return self._AcctInf

	@AcctInf.setter
	def AcctInf(self, value):
		self._AcctInf = value if type(value) != base_types.auto else self.make_default("AcctInf")

	@AcctInf.deleter
	def AcctInf(self):
		del self._AcctInf
		self._AcctInf = None

	@property
	def AddtlChrg(self):
		return self._AddtlChrg

	@AddtlChrg.setter
	def AddtlChrg(self, value):
		self._AddtlChrg = value if type(value) != base_types.auto else self.make_default("AddtlChrg")

	@AddtlChrg.deleter
	def AddtlChrg(self):
		del self._AddtlChrg
		self._AddtlChrg = None

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != base_types.auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	@property
	def CcyConvsElgblty(self):
		return self._CcyConvsElgblty

	@CcyConvsElgblty.setter
	def CcyConvsElgblty(self, value):
		self._CcyConvsElgblty = value if type(value) != base_types.auto else self.make_default("CcyConvsElgblty")

	@CcyConvsElgblty.deleter
	def CcyConvsElgblty(self):
		del self._CcyConvsElgblty
		self._CcyConvsElgblty = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != base_types.auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def CmpltnReqrd(self):
		return self._CmpltnReqrd

	@CmpltnReqrd.setter
	def CmpltnReqrd(self, value):
		self._CmpltnReqrd = value if type(value) != base_types.auto else self.make_default("CmpltnReqrd")

	@CmpltnReqrd.deleter
	def CmpltnReqrd(self):
		del self._CmpltnReqrd
		self._CmpltnReqrd = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != base_types.auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def Lmts(self):
		return self._Lmts

	@Lmts.setter
	def Lmts(self, value):
		self._Lmts = value if type(value) != base_types.auto else self.make_default("Lmts")

	@Lmts.deleter
	def Lmts(self):
		del self._Lmts
		self._Lmts = None

	@property
	def Mix(self):
		return self._Mix

	@Mix.setter
	def Mix(self, value):
		self._Mix = value if type(value) != base_types.auto else self.make_default("Mix")

	@Mix.deleter
	def Mix(self):
		del self._Mix
		self._Mix = None

	@property
	def MixTp(self):
		return self._MixTp

	@MixTp.setter
	def MixTp(self, value):
		self._MixTp = value if type(value) != base_types.auto else self.make_default("MixTp")

	@MixTp.deleter
	def MixTp(self):
		del self._MixTp
		self._MixTp = None

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != base_types.auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if type(value) != base_types.auto else self.make_default("TtlAuthrsdAmt")

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = None

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if type(value) != base_types.auto else self.make_default("TtlReqdAmt")

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctData', type=CardAccount22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsElgblty', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltnReqrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mix', type=ATMMediaMix1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MixTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=AmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))

