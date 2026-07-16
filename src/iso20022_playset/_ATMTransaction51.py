# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassette3
from . import ATMDepositComponent1
from . import ATMDepositedMedia4
from . import ATMTotals4
from . import ATMTransactionStatus1Code
from . import AmountAndCurrency1
from . import AuthorisationResult20
from . import DetailedAmount13
from . import DetailedAmount16
from . import FailureReason9Code
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction51(base_types._BaseFieldType):

	__slots__ = ["_ATMTtls", "_AddtlChrg", "_AuthstnRslt", "_Csstt", "_DtldReqdAmt", "_ICCRltdData", "_Incdnt", "_IncdntDtl", "_RcncltnId", "_RctPrtd", "_ReqdRct", "_SubDpst", "_ToBeRcncldMdiaCntrs", "_TtlAuthrsdAmt", "_TtlDpstdAmt", "_TtlReqdAmt", "_TxId", "_TxSts"]
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
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount16, False)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount16, False)

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
	def ToBeRcncldMdiaCntrs(self):
		return self._ToBeRcncldMdiaCntrs

	@ToBeRcncldMdiaCntrs.setter
	def ToBeRcncldMdiaCntrs(self, value):
		self._ToBeRcncldMdiaCntrs = value if value is not None else base_types.UninitialisedField(self, 'ToBeRcncldMdiaCntrs', ATMDepositedMedia4, True)

	@ToBeRcncldMdiaCntrs.deleter
	def ToBeRcncldMdiaCntrs(self):
		del self._ToBeRcncldMdiaCntrs
		self._ToBeRcncldMdiaCntrs = base_types.UninitialisedField(self, 'ToBeRcncldMdiaCntrs', ATMDepositedMedia4, True)

	@property
	def TtlAuthrsdAmt(self):
		return self._TtlAuthrsdAmt

	@TtlAuthrsdAmt.setter
	def TtlAuthrsdAmt(self, value):
		self._TtlAuthrsdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, True)

	@TtlAuthrsdAmt.deleter
	def TtlAuthrsdAmt(self):
		del self._TtlAuthrsdAmt
		self._TtlAuthrsdAmt = base_types.UninitialisedField(self, 'TtlAuthrsdAmt', ImpliedCurrencyAndAmount, True)

	@property
	def TtlDpstdAmt(self):
		return self._TtlDpstdAmt

	@TtlDpstdAmt.setter
	def TtlDpstdAmt(self, value):
		self._TtlDpstdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlDpstdAmt', AmountAndCurrency1, True)

	@TtlDpstdAmt.deleter
	def TtlDpstdAmt(self):
		del self._TtlDpstdAmt
		self._TtlDpstdAmt = base_types.UninitialisedField(self, 'TtlDpstdAmt', AmountAndCurrency1, True)

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
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncdntDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubDpst', type=ATMDepositComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ToBeRcncldMdiaCntrs', type=ATMDepositedMedia4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=ImpliedCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlDpstdAmt', type=AmountAndCurrency1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=ATMTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))