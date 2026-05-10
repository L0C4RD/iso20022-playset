from . import base_types
import ReturnExcessCash1
import ThresholdType1Code
import ActiveCurrencyAndAmount

class SummaryAmounts2(base_types._BaseFieldType):

	__slots__ = ["_TtlAcrdIntrstAmt", "_MinTrfAmt", "_TtlPdgOutgngColl", "_PreHrcutCollVal", "_RtrXcssCshAndCollCcy", "_PrvsXpsrVal", "_RndgAmt", "_TtlFees", "_TtlPdgIncmgColl", "_CollReqrd", "_AdjstdXpsr", "_ThrshldTp", "_ThrshldAmt", "_PrvsCollVal"]
	@property
	def TtlAcrdIntrstAmt(self):
		return self._TtlAcrdIntrstAmt

	@TtlAcrdIntrstAmt.setter
	def TtlAcrdIntrstAmt(self, value):
		self._TtlAcrdIntrstAmt = value if type(value) != auto else self.make_default("TtlAcrdIntrstAmt")

	@TtlAcrdIntrstAmt.deleter
	def TtlAcrdIntrstAmt(self):
		del self._TtlAcrdIntrstAmt
		self._TtlAcrdIntrstAmt = None

	@property
	def MinTrfAmt(self):
		return self._MinTrfAmt

	@MinTrfAmt.setter
	def MinTrfAmt(self, value):
		self._MinTrfAmt = value if type(value) != auto else self.make_default("MinTrfAmt")

	@MinTrfAmt.deleter
	def MinTrfAmt(self):
		del self._MinTrfAmt
		self._MinTrfAmt = None

	@property
	def TtlPdgOutgngColl(self):
		return self._TtlPdgOutgngColl

	@TtlPdgOutgngColl.setter
	def TtlPdgOutgngColl(self, value):
		self._TtlPdgOutgngColl = value if type(value) != auto else self.make_default("TtlPdgOutgngColl")

	@TtlPdgOutgngColl.deleter
	def TtlPdgOutgngColl(self):
		del self._TtlPdgOutgngColl
		self._TtlPdgOutgngColl = None

	@property
	def PreHrcutCollVal(self):
		return self._PreHrcutCollVal

	@PreHrcutCollVal.setter
	def PreHrcutCollVal(self, value):
		self._PreHrcutCollVal = value if type(value) != auto else self.make_default("PreHrcutCollVal")

	@PreHrcutCollVal.deleter
	def PreHrcutCollVal(self):
		del self._PreHrcutCollVal
		self._PreHrcutCollVal = None

	@property
	def RtrXcssCshAndCollCcy(self):
		return self._RtrXcssCshAndCollCcy

	@RtrXcssCshAndCollCcy.setter
	def RtrXcssCshAndCollCcy(self, value):
		self._RtrXcssCshAndCollCcy = value if type(value) != auto else self.make_default("RtrXcssCshAndCollCcy")

	@RtrXcssCshAndCollCcy.deleter
	def RtrXcssCshAndCollCcy(self):
		del self._RtrXcssCshAndCollCcy
		self._RtrXcssCshAndCollCcy = None

	@property
	def PrvsXpsrVal(self):
		return self._PrvsXpsrVal

	@PrvsXpsrVal.setter
	def PrvsXpsrVal(self, value):
		self._PrvsXpsrVal = value if type(value) != auto else self.make_default("PrvsXpsrVal")

	@PrvsXpsrVal.deleter
	def PrvsXpsrVal(self):
		del self._PrvsXpsrVal
		self._PrvsXpsrVal = None

	@property
	def RndgAmt(self):
		return self._RndgAmt

	@RndgAmt.setter
	def RndgAmt(self, value):
		self._RndgAmt = value if type(value) != auto else self.make_default("RndgAmt")

	@RndgAmt.deleter
	def RndgAmt(self):
		del self._RndgAmt
		self._RndgAmt = None

	@property
	def TtlFees(self):
		return self._TtlFees

	@TtlFees.setter
	def TtlFees(self, value):
		self._TtlFees = value if type(value) != auto else self.make_default("TtlFees")

	@TtlFees.deleter
	def TtlFees(self):
		del self._TtlFees
		self._TtlFees = None

	@property
	def TtlPdgIncmgColl(self):
		return self._TtlPdgIncmgColl

	@TtlPdgIncmgColl.setter
	def TtlPdgIncmgColl(self, value):
		self._TtlPdgIncmgColl = value if type(value) != auto else self.make_default("TtlPdgIncmgColl")

	@TtlPdgIncmgColl.deleter
	def TtlPdgIncmgColl(self):
		del self._TtlPdgIncmgColl
		self._TtlPdgIncmgColl = None

	@property
	def CollReqrd(self):
		return self._CollReqrd

	@CollReqrd.setter
	def CollReqrd(self, value):
		self._CollReqrd = value if type(value) != auto else self.make_default("CollReqrd")

	@CollReqrd.deleter
	def CollReqrd(self):
		del self._CollReqrd
		self._CollReqrd = None

	@property
	def AdjstdXpsr(self):
		return self._AdjstdXpsr

	@AdjstdXpsr.setter
	def AdjstdXpsr(self, value):
		self._AdjstdXpsr = value if type(value) != auto else self.make_default("AdjstdXpsr")

	@AdjstdXpsr.deleter
	def AdjstdXpsr(self):
		del self._AdjstdXpsr
		self._AdjstdXpsr = None

	@property
	def ThrshldTp(self):
		return self._ThrshldTp

	@ThrshldTp.setter
	def ThrshldTp(self, value):
		self._ThrshldTp = value if type(value) != auto else self.make_default("ThrshldTp")

	@ThrshldTp.deleter
	def ThrshldTp(self):
		del self._ThrshldTp
		self._ThrshldTp = None

	@property
	def ThrshldAmt(self):
		return self._ThrshldAmt

	@ThrshldAmt.setter
	def ThrshldAmt(self, value):
		self._ThrshldAmt = value if type(value) != auto else self.make_default("ThrshldAmt")

	@ThrshldAmt.deleter
	def ThrshldAmt(self):
		del self._ThrshldAmt
		self._ThrshldAmt = None

	@property
	def PrvsCollVal(self):
		return self._PrvsCollVal

	@PrvsCollVal.setter
	def PrvsCollVal(self, value):
		self._PrvsCollVal = value if type(value) != auto else self.make_default("PrvsCollVal")

	@PrvsCollVal.deleter
	def PrvsCollVal(self):
		del self._PrvsCollVal
		self._PrvsCollVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlAcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinTrfAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgOutgngColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreHrcutCollVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrXcssCshAndCollCcy', type=ReturnExcessCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsXpsrVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgIncmgColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollReqrd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstdXpsr', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldTp', type=ThresholdType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsCollVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

