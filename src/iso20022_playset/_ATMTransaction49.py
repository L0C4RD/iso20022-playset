# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7
from . import ATMMediaMix1
from . import ATMTransactionAmounts6
from . import AmountAndCurrency1
from . import AuthorisationResult20
from . import CardAccount18
from . import CardAccount22
from . import ContentInformationType10
from . import CurrencyConversion32
from . import DetailedAmount12
from . import DetailedAmount13
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction49(base_types._BaseFieldType):

	__slots__ = ["_AcctData", "_AcctInf", "_AddtlChrg", "_AuthstnRslt", "_CcyConvsElgblty", "_Cmd", "_CmpltnReqrd", "_DtldReqdAmt", "_ICCRltdData", "_Lmts", "_Mix", "_MixTp", "_PrtctdAcctData", "_RcncltnId", "_TtlAuthrsdAmt", "_TtlReqdAmt", "_TxId"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if value is not None else base_types.UninitialisedField(self, 'AcctData', CardAccount22, False)

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = base_types.UninitialisedField(self, 'AcctData', CardAccount22, False)

	@property
	def AcctInf(self):
		return self._AcctInf

	@AcctInf.setter
	def AcctInf(self, value):
		self._AcctInf = value if value is not None else base_types.UninitialisedField(self, 'AcctInf', CardAccount18, True)

	@AcctInf.deleter
	def AcctInf(self):
		del self._AcctInf
		self._AcctInf = base_types.UninitialisedField(self, 'AcctInf', CardAccount18, True)

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
	def CcyConvsElgblty(self):
		return self._CcyConvsElgblty

	@CcyConvsElgblty.setter
	def CcyConvsElgblty(self, value):
		self._CcyConvsElgblty = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsElgblty', CurrencyConversion32, False)

	@CcyConvsElgblty.deleter
	def CcyConvsElgblty(self):
		del self._CcyConvsElgblty
		self._CcyConvsElgblty = base_types.UninitialisedField(self, 'CcyConvsElgblty', CurrencyConversion32, False)

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@property
	def CmpltnReqrd(self):
		return self._CmpltnReqrd

	@CmpltnReqrd.setter
	def CmpltnReqrd(self, value):
		self._CmpltnReqrd = value if value is not None else base_types.UninitialisedField(self, 'CmpltnReqrd', TrueFalseIndicator, False)

	@CmpltnReqrd.deleter
	def CmpltnReqrd(self):
		del self._CmpltnReqrd
		self._CmpltnReqrd = base_types.UninitialisedField(self, 'CmpltnReqrd', TrueFalseIndicator, False)

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
	def Mix(self):
		return self._Mix

	@Mix.setter
	def Mix(self, value):
		self._Mix = value if value is not None else base_types.UninitialisedField(self, 'Mix', ATMMediaMix1, True)

	@Mix.deleter
	def Mix(self):
		del self._Mix
		self._Mix = base_types.UninitialisedField(self, 'Mix', ATMMediaMix1, True)

	@property
	def MixTp(self):
		return self._MixTp

	@MixTp.setter
	def MixTp(self, value):
		self._MixTp = value if value is not None else base_types.UninitialisedField(self, 'MixTp', Max35Text, False)

	@MixTp.deleter
	def MixTp(self):
		del self._MixTp
		self._MixTp = base_types.UninitialisedField(self, 'MixTp', Max35Text, False)

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
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAuthrsdAmt', AmountAndCurrency1, False)

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = base_types.UninitialisedField(self, 'TtlAuthrsdAmt', AmountAndCurrency1, False)

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