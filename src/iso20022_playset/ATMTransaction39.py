import base_types
import DetailedAmount18
import ATMTransactionAmounts6
import ContentInformationType10
import DetailedAmount17
import AmountAndCurrency1
import TransactionIdentifier3
import ATMCommand7
import Max10000Binary
import Max70Text
import CardAccount18
import CardAccount19
import ResponseType12
import Action7
import ImpliedCurrencyAndAmount
import RecurringTransaction3
import Max35Text
import ISODate
import AuthorisationResult20

class ATMTransaction39(base_types._BaseFieldType):

	__slots__ = ["_ICCRltdData", "_RcrngTrf", "_AcctInf", "_AcctFr", "_TrfIdr", "_AcctTo", "_PropsdExctnDt", "_RcncltnId", "_PrtctdAcctTo", "_TxId", "_AuthstnRslt", "_DtldReqdAmt", "_TxRspn", "_TtlAuthrsdAmt", "_Lmts", "_PrtctdAcctFr", "_Cmd", "_PmtRef", "_TtlReqdAmt", "_AddtlChrg", "_ReqdExctnDt", "_Actn", "_DbtrLabl", "_InstntTrfPrgm", "_CdtrLabl"]
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
	def RcrngTrf(self):
		return self._RcrngTrf

	@RcrngTrf.setter
	def RcrngTrf(self, value):
		self._RcrngTrf = value if type(value) != auto else self.make_default("RcrngTrf")

	@RcrngTrf.deleter
	def RcrngTrf(self):
		del self._RcrngTrf
		self._RcrngTrf = None

	@property
	def AcctInf(self):
		return self._AcctInf

	@AcctInf.setter
	def AcctInf(self, value):
		self._AcctInf = value if type(value) != auto else self.make_default("AcctInf")

	@AcctInf.deleter
	def AcctInf(self):
		del self._AcctInf
		self._AcctInf = None

	@property
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if type(value) != auto else self.make_default("AcctFr")

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = None

	@property
	def TrfIdr(self):
		return self._TrfIdr

	@TrfIdr.setter
	def TrfIdr(self, value):
		self._TrfIdr = value if type(value) != auto else self.make_default("TrfIdr")

	@TrfIdr.deleter
	def TrfIdr(self):
		del self._TrfIdr
		self._TrfIdr = None

	@property
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if type(value) != auto else self.make_default("AcctTo")

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = None

	@property
	def PropsdExctnDt(self):
		return self._PropsdExctnDt

	@PropsdExctnDt.setter
	def PropsdExctnDt(self, value):
		self._PropsdExctnDt = value if type(value) != auto else self.make_default("PropsdExctnDt")

	@PropsdExctnDt.deleter
	def PropsdExctnDt(self):
		del self._PropsdExctnDt
		self._PropsdExctnDt = None

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
	def PrtctdAcctTo(self):
		return self._PrtctdAcctTo

	@PrtctdAcctTo.setter
	def PrtctdAcctTo(self, value):
		self._PrtctdAcctTo = value if type(value) != auto else self.make_default("PrtctdAcctTo")

	@PrtctdAcctTo.deleter
	def PrtctdAcctTo(self):
		del self._PrtctdAcctTo
		self._PrtctdAcctTo = None

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
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

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
	def PrtctdAcctFr(self):
		return self._PrtctdAcctFr

	@PrtctdAcctFr.setter
	def PrtctdAcctFr(self, value):
		self._PrtctdAcctFr = value if type(value) != auto else self.make_default("PrtctdAcctFr")

	@PrtctdAcctFr.deleter
	def PrtctdAcctFr(self):
		del self._PrtctdAcctFr
		self._PrtctdAcctFr = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if type(value) != auto else self.make_default("PmtRef")

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = None

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
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def DbtrLabl(self):
		return self._DbtrLabl

	@DbtrLabl.setter
	def DbtrLabl(self, value):
		self._DbtrLabl = value if type(value) != auto else self.make_default("DbtrLabl")

	@DbtrLabl.deleter
	def DbtrLabl(self):
		del self._DbtrLabl
		self._DbtrLabl = None

	@property
	def InstntTrfPrgm(self):
		return self._InstntTrfPrgm

	@InstntTrfPrgm.setter
	def InstntTrfPrgm(self, value):
		self._InstntTrfPrgm = value if type(value) != auto else self.make_default("InstntTrfPrgm")

	@InstntTrfPrgm.deleter
	def InstntTrfPrgm(self):
		del self._InstntTrfPrgm
		self._InstntTrfPrgm = None

	@property
	def CdtrLabl(self):
		return self._CdtrLabl

	@CdtrLabl.setter
	def CdtrLabl(self, value):
		self._CdtrLabl = value if type(value) != auto else self.make_default("CdtrLabl")

	@CdtrLabl.deleter
	def CdtrLabl(self):
		del self._CdtrLabl
		self._CdtrLabl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrngTrf', type=RecurringTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctFr', type=CardAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfIdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=CardAccount19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PropsdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctTo', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAuthrsdAmt', type=AmountAndCurrency1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctFr', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlChrg', type=DetailedAmount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DbtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstntTrfPrgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

