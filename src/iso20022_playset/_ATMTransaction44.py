# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7
from . import ATMDepositComponent1
from . import ATMDepositedMedia4
from . import AmountAndCurrency1
from . import AuthorisationResult20
from . import CardAccount18
from . import DetailedAmount13
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction44(base_types._BaseFieldType):

	__slots__ = ["_AcctInf", "_AddtlChrg", "_AuthstnRslt", "_Cmd", "_CmpltnReqrd", "_DpstdMdia", "_ICCRltdData", "_RcncltnId", "_SubDpst", "_TtlAuthrsdAmt", "_TtlReqdAmt", "_TxId"]
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
	def DpstdMdia(self):
		return self._DpstdMdia

	@DpstdMdia.setter
	def DpstdMdia(self, value):
		self._DpstdMdia = value if value is not None else base_types.UninitialisedField(self, 'DpstdMdia', ATMDepositedMedia4, True)

	@DpstdMdia.deleter
	def DpstdMdia(self):
		del self._DpstdMdia
		self._DpstdMdia = base_types.UninitialisedField(self, 'DpstdMdia', ATMDepositedMedia4, True)

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
	def SubDpst(self):
		return self._SubDpst

	@SubDpst.setter
	def SubDpst(self, value):
		self._SubDpst = value if value is not None else base_types.UninitialisedField(self, 'SubDpst', ATMDepositComponent1, True)

	@SubDpst.deleter
	def SubDpst(self):
		del self._SubDpst
		self._SubDpst = base_types.UninitialisedField(self, 'SubDpst', ATMDepositComponent1, True)

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAuthrsdAmt', AmountAndCurrency1, True)

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = base_types.UninitialisedField(self, 'TtlAuthrsdAmt', AmountAndCurrency1, True)

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, True)

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, True)

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
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltnReqrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstdMdia', type=ATMDepositedMedia4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDpst', type=ATMDepositComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=AmountAndCurrency1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))