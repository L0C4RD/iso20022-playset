from . import base_types
import ISODate
import EarlyPayment1
import Period2
import CurrencyReference3
import SettlementSubTotalCalculatedTax2
import CreditorReferenceInformation2
import Max500Text
import CurrencyAndAmount
import Max4Text

class TradeSettlement2(base_types._BaseFieldType):

	__slots__ = ["_PmtRef", "_XmptnRsn", "_DuePyblAmt", "_BllgPrd", "_DueDt", "_XmptnRsnCd", "_DlvryDt", "_TaxTtlAmt", "_SubTtlClctdTax", "_EarlyPmts", "_InvcCcyXchg"]
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
	def XmptnRsn(self):
		return self._XmptnRsn

	@XmptnRsn.setter
	def XmptnRsn(self, value):
		self._XmptnRsn = value if type(value) != auto else self.make_default("XmptnRsn")

	@XmptnRsn.deleter
	def XmptnRsn(self):
		del self._XmptnRsn
		self._XmptnRsn = None

	@property
	def DuePyblAmt(self):
		return self._DuePyblAmt

	@DuePyblAmt.setter
	def DuePyblAmt(self, value):
		self._DuePyblAmt = value if type(value) != auto else self.make_default("DuePyblAmt")

	@DuePyblAmt.deleter
	def DuePyblAmt(self):
		del self._DuePyblAmt
		self._DuePyblAmt = None

	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if type(value) != auto else self.make_default("BllgPrd")

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = None

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def XmptnRsnCd(self):
		return self._XmptnRsnCd

	@XmptnRsnCd.setter
	def XmptnRsnCd(self, value):
		self._XmptnRsnCd = value if type(value) != auto else self.make_default("XmptnRsnCd")

	@XmptnRsnCd.deleter
	def XmptnRsnCd(self):
		del self._XmptnRsnCd
		self._XmptnRsnCd = None

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if type(value) != auto else self.make_default("DlvryDt")

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = None

	@property
	def TaxTtlAmt(self):
		return self._TaxTtlAmt

	@TaxTtlAmt.setter
	def TaxTtlAmt(self, value):
		self._TaxTtlAmt = value if type(value) != auto else self.make_default("TaxTtlAmt")

	@TaxTtlAmt.deleter
	def TaxTtlAmt(self):
		del self._TaxTtlAmt
		self._TaxTtlAmt = None

	@property
	def SubTtlClctdTax(self):
		return self._SubTtlClctdTax

	@SubTtlClctdTax.setter
	def SubTtlClctdTax(self, value):
		self._SubTtlClctdTax = value if type(value) != auto else self.make_default("SubTtlClctdTax")

	@SubTtlClctdTax.deleter
	def SubTtlClctdTax(self):
		del self._SubTtlClctdTax
		self._SubTtlClctdTax = None

	@property
	def EarlyPmts(self):
		return self._EarlyPmts

	@EarlyPmts.setter
	def EarlyPmts(self, value):
		self._EarlyPmts = value if type(value) != auto else self.make_default("EarlyPmts")

	@EarlyPmts.deleter
	def EarlyPmts(self):
		del self._EarlyPmts
		self._EarlyPmts = None

	@property
	def InvcCcyXchg(self):
		return self._InvcCcyXchg

	@InvcCcyXchg.setter
	def InvcCcyXchg(self, value):
		self._InvcCcyXchg = value if type(value) != auto else self.make_default("InvcCcyXchg")

	@InvcCcyXchg.deleter
	def InvcCcyXchg(self):
		del self._InvcCcyXchg
		self._InvcCcyXchg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtRef', type=CreditorReferenceInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsn', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DuePyblAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=Period2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTtlClctdTax', type=SettlementSubTotalCalculatedTax2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlyPmts', type=EarlyPayment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcCcyXchg', type=CurrencyReference3, min=0, max=1, mutex_group=None, array=False),
	))

