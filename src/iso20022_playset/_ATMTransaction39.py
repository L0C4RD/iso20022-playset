# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7
from . import ATMTransactionAmounts6
from . import Action7
from . import AmountAndCurrency1
from . import AuthorisationResult20
from . import CardAccount18
from . import CardAccount19
from . import ContentInformationType10
from . import DetailedAmount17
from . import DetailedAmount18
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import Max70Text
from . import RecurringTransaction3
from . import ResponseType12
from . import TransactionIdentifier3

class ATMTransaction39(base_types._BaseFieldType):

	__slots__ = ["_AcctFr", "_AcctInf", "_AcctTo", "_Actn", "_AddtlChrg", "_AuthstnRslt", "_CdtrLabl", "_Cmd", "_DbtrLabl", "_DtldReqdAmt", "_ICCRltdData", "_InstntTrfPrgm", "_Lmts", "_PmtRef", "_PropsdExctnDt", "_PrtctdAcctFr", "_PrtctdAcctTo", "_RcncltnId", "_RcrngTrf", "_ReqdExctnDt", "_TrfIdr", "_TtlAuthrsdAmt", "_TtlReqdAmt", "_TxId", "_TxRspn"]
	@property
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if value is not None else base_types.UninitialisedField(self, 'AcctFr', CardAccount19, False)

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = base_types.UninitialisedField(self, 'AcctFr', CardAccount19, False)

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
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if value is not None else base_types.UninitialisedField(self, 'AcctTo', CardAccount19, True)

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = base_types.UninitialisedField(self, 'AcctTo', CardAccount19, True)

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', Action7, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', Action7, True)

	@property
	def AddtlChrg(self):
		return self._AddtlChrg

	@AddtlChrg.setter
	def AddtlChrg(self, value):
		self._AddtlChrg = value if value is not None else base_types.UninitialisedField(self, 'AddtlChrg', DetailedAmount18, True)

	@AddtlChrg.deleter
	def AddtlChrg(self):
		del self._AddtlChrg
		self._AddtlChrg = base_types.UninitialisedField(self, 'AddtlChrg', DetailedAmount18, True)

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
	def CdtrLabl(self):
		return self._CdtrLabl

	@CdtrLabl.setter
	def CdtrLabl(self, value):
		self._CdtrLabl = value if value is not None else base_types.UninitialisedField(self, 'CdtrLabl', Max35Text, False)

	@CdtrLabl.deleter
	def CdtrLabl(self):
		del self._CdtrLabl
		self._CdtrLabl = base_types.UninitialisedField(self, 'CdtrLabl', Max35Text, False)

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
	def DbtrLabl(self):
		return self._DbtrLabl

	@DbtrLabl.setter
	def DbtrLabl(self, value):
		self._DbtrLabl = value if value is not None else base_types.UninitialisedField(self, 'DbtrLabl', Max35Text, False)

	@DbtrLabl.deleter
	def DbtrLabl(self):
		del self._DbtrLabl
		self._DbtrLabl = base_types.UninitialisedField(self, 'DbtrLabl', Max35Text, False)

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount17, False)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount17, False)

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
	def InstntTrfPrgm(self):
		return self._InstntTrfPrgm

	@InstntTrfPrgm.setter
	def InstntTrfPrgm(self, value):
		self._InstntTrfPrgm = value if value is not None else base_types.UninitialisedField(self, 'InstntTrfPrgm', Max35Text, False)

	@InstntTrfPrgm.deleter
	def InstntTrfPrgm(self):
		del self._InstntTrfPrgm
		self._InstntTrfPrgm = base_types.UninitialisedField(self, 'InstntTrfPrgm', Max35Text, False)

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
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if value is not None else base_types.UninitialisedField(self, 'PmtRef', Max35Text, False)

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = base_types.UninitialisedField(self, 'PmtRef', Max35Text, False)

	@property
	def PropsdExctnDt(self):
		return self._PropsdExctnDt

	@PropsdExctnDt.setter
	def PropsdExctnDt(self, value):
		self._PropsdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'PropsdExctnDt', ISODate, False)

	@PropsdExctnDt.deleter
	def PropsdExctnDt(self):
		del self._PropsdExctnDt
		self._PropsdExctnDt = base_types.UninitialisedField(self, 'PropsdExctnDt', ISODate, False)

	@property
	def PrtctdAcctFr(self):
		return self._PrtctdAcctFr

	@PrtctdAcctFr.setter
	def PrtctdAcctFr(self, value):
		self._PrtctdAcctFr = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctFr', ContentInformationType10, False)

	@PrtctdAcctFr.deleter
	def PrtctdAcctFr(self):
		del self._PrtctdAcctFr
		self._PrtctdAcctFr = base_types.UninitialisedField(self, 'PrtctdAcctFr', ContentInformationType10, False)

	@property
	def PrtctdAcctTo(self):
		return self._PrtctdAcctTo

	@PrtctdAcctTo.setter
	def PrtctdAcctTo(self, value):
		self._PrtctdAcctTo = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctTo', ContentInformationType10, False)

	@PrtctdAcctTo.deleter
	def PrtctdAcctTo(self):
		del self._PrtctdAcctTo
		self._PrtctdAcctTo = base_types.UninitialisedField(self, 'PrtctdAcctTo', ContentInformationType10, False)

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
	def RcrngTrf(self):
		return self._RcrngTrf

	@RcrngTrf.setter
	def RcrngTrf(self, value):
		self._RcrngTrf = value if value is not None else base_types.UninitialisedField(self, 'RcrngTrf', RecurringTransaction3, False)

	@RcrngTrf.deleter
	def RcrngTrf(self):
		del self._RcrngTrf
		self._RcrngTrf = base_types.UninitialisedField(self, 'RcrngTrf', RecurringTransaction3, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	@property
	def TrfIdr(self):
		return self._TrfIdr

	@TrfIdr.setter
	def TrfIdr(self, value):
		self._TrfIdr = value if value is not None else base_types.UninitialisedField(self, 'TrfIdr', Max70Text, False)

	@TrfIdr.deleter
	def TrfIdr(self):
		del self._TrfIdr
		self._TrfIdr = base_types.UninitialisedField(self, 'TrfIdr', Max70Text, False)

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

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if value is not None else base_types.UninitialisedField(self, 'TxRspn', ResponseType12, False)

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = base_types.UninitialisedField(self, 'TxRspn', ResponseType12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctFr', type=CardAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctTo', type=CardAccount19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DbtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstntTrfPrgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctFr', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctTo', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrngTrf', type=RecurringTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfIdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=AmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
	))