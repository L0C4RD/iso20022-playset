from . import base_types
import ISODate
import Max10000Binary
import TransactionIdentifier3
import ContentInformationType10
import Max35Text
import RecurringTransaction3
import DetailedAmount17
import TrueFalseIndicator
import CardAccount20
import ImpliedCurrencyAndAmount

class ATMTransaction38(base_types._BaseFieldType):

	__slots__ = ["_PrtctdAcctTo", "_ReqdRct", "_DbtrLabl", "_TxId", "_PmtRef", "_RcncltnId", "_CdtrLabl", "_TtlReqdAmt", "_InstntTrfPrgm", "_ReqdExctnDt", "_RcrngTrf", "_ICCRltdData", "_DtldReqdAmt", "_AcctFr", "_PrtctdAcctFr", "_AcctTo"]
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
	def CdtrLabl(self):
		return self._CdtrLabl

	@CdtrLabl.setter
	def CdtrLabl(self, value):
		self._CdtrLabl = value if type(value) != auto else self.make_default("CdtrLabl")

	@CdtrLabl.deleter
	def CdtrLabl(self):
		del self._CdtrLabl
		self._CdtrLabl = None

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
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if type(value) != auto else self.make_default("AcctTo")

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdAcctTo', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstntTrfPrgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrngTrf', type=RecurringTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctFr', type=CardAccount20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctFr', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=CardAccount20, min=0, max=None, mutex_group=None, array=True),
	))

