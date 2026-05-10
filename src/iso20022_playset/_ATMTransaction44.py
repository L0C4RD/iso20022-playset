from . import base_types
from .TransactionIdentifier3 import TransactionIdentifier3
from .ATMCommand7 import ATMCommand7
from .DetailedAmount13 import DetailedAmount13
from .ATMDepositComponent1 import ATMDepositComponent1
from .Max10000Binary import Max10000Binary
from .ATMDepositedMedia4 import ATMDepositedMedia4
from .Max35Text import Max35Text
from .TrueFalseIndicator import TrueFalseIndicator
from .AmountAndCurrency1 import AmountAndCurrency1
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .CardAccount18 import CardAccount18
from .AuthorisationResult20 import AuthorisationResult20

class ATMTransaction44(base_types._BaseFieldType):

	__slots__ = ["_DpstdMdia", "_AcctInf", "_TtlAuthrsdAmt", "_RcncltnId", "_AuthstnRslt", "_ICCRltdData", "_Cmd", "_CmpltnReqrd", "_TtlReqdAmt", "_AddtlChrg", "_SubDpst", "_TxId"]
	@property
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if type(value) != base_types.auto else self.make_default("DpstdMdia")

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = None

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
	def SubDpst(self):
		return self._SubDpst

	@SubDpst.setter
	def SubDpst(self, value):
		self._SubDpst = value if type(value) != base_types.auto else self.make_default("SubDpst")

	@SubDpst.deleter
	def SubDpst(self):
		del self._SubDpst
		self._SubDpst = None

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
		base_types.FieldEntry(name='DpstdMdia', type=ATMDepositedMedia4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=AmountAndCurrency1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltnReqrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubDpst', type=ATMDepositComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))

