import base_types
import Max4Text
import Max500Text
import CurrencyAndAmount
import PercentageRate
import CurrencyReference3

class SettlementSubTotalCalculatedTax2(base_types._BaseFieldType):

	__slots__ = ["_ClctdAmt", "_TaxCcyXchg", "_ClctdRate", "_XmptnRsnCd", "_XmptnRsnTxt", "_BsisAmt", "_TpCd"]
	@property
	def ClctdAmt(self):
		return self._ClctdAmt

	@ClctdAmt.setter
	def ClctdAmt(self, value):
		self._ClctdAmt = value if type(value) != auto else self.make_default("ClctdAmt")

	@ClctdAmt.deleter
	def ClctdAmt(self):
		del self._ClctdAmt
		self._ClctdAmt = None

	@property
	def TaxCcyXchg(self):
		return self._TaxCcyXchg

	@TaxCcyXchg.setter
	def TaxCcyXchg(self, value):
		self._TaxCcyXchg = value if type(value) != auto else self.make_default("TaxCcyXchg")

	@TaxCcyXchg.deleter
	def TaxCcyXchg(self):
		del self._TaxCcyXchg
		self._TaxCcyXchg = None

	@property
	def ClctdRate(self):
		return self._ClctdRate

	@ClctdRate.setter
	def ClctdRate(self, value):
		self._ClctdRate = value if type(value) != auto else self.make_default("ClctdRate")

	@ClctdRate.deleter
	def ClctdRate(self):
		del self._ClctdRate
		self._ClctdRate = None

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
	def XmptnRsnTxt(self):
		return self._XmptnRsnTxt

	@XmptnRsnTxt.setter
	def XmptnRsnTxt(self, value):
		self._XmptnRsnTxt = value if type(value) != auto else self.make_default("XmptnRsnTxt")

	@XmptnRsnTxt.deleter
	def XmptnRsnTxt(self):
		del self._XmptnRsnTxt
		self._XmptnRsnTxt = None

	@property
	def BsisAmt(self):
		return self._BsisAmt

	@BsisAmt.setter
	def BsisAmt(self, value):
		self._BsisAmt = value if type(value) != auto else self.make_default("BsisAmt")

	@BsisAmt.deleter
	def BsisAmt(self):
		del self._BsisAmt
		self._BsisAmt = None

	@property
	def TpCd(self):
		return self._TpCd

	@TpCd.setter
	def TpCd(self, value):
		self._TpCd = value if type(value) != auto else self.make_default("TpCd")

	@TpCd.deleter
	def TpCd(self):
		del self._TpCd
		self._TpCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctdAmt', type=CurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCcyXchg', type=CurrencyReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnTxt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisAmt', type=CurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TpCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
	))

