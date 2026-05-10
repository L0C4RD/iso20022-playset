from . import base_types
import ISODate
import TaxParty2
import TaxParty1
import Max140Text
import TaxRecord3
import Max35Text
import Number
import ActiveOrHistoricCurrencyAndAmount

class TaxData1(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_Cdtr", "_AdmstnZone", "_Mtd", "_TtlTaxblBaseAmt", "_Dt", "_TtlTaxAmt", "_Dbtr", "_SeqNb", "_UltmtDbtr", "_RefNb"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def AdmstnZone(self):
		return self._AdmstnZone

	@AdmstnZone.setter
	def AdmstnZone(self, value):
		self._AdmstnZone = value if type(value) != auto else self.make_default("AdmstnZone")

	@AdmstnZone.deleter
	def AdmstnZone(self):
		del self._AdmstnZone
		self._AdmstnZone = None

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def TtlTaxblBaseAmt(self):
		return self._TtlTaxblBaseAmt

	@TtlTaxblBaseAmt.setter
	def TtlTaxblBaseAmt(self, value):
		self._TtlTaxblBaseAmt = value if type(value) != auto else self.make_default("TtlTaxblBaseAmt")

	@TtlTaxblBaseAmt.deleter
	def TtlTaxblBaseAmt(self):
		del self._TtlTaxblBaseAmt
		self._TtlTaxblBaseAmt = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if type(value) != auto else self.make_default("TtlTaxAmt")

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if type(value) != auto else self.make_default("RefNb")

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=TaxRecord3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cdtr', type=TaxParty1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdmstnZone', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblBaseAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=TaxParty2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=TaxParty2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

