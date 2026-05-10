import base_types
import HoldingTransferable1Code
import Number
import Max350Text
import DecimalNumber
import ActiveCurrencyAndAmount
import AdditionalInformation15
import Max70Text

class InvestmentRestrictions3(base_types._BaseFieldType):

	__slots__ = ["_MinHldgAmt", "_MinSwtchSbcptUnits", "_OthrSwtchRstrctns", "_MinHldgUnits", "_AddtlInf", "_MinHldgPrd", "_MaxRedAmt", "_MaxSwtchRedAmt", "_MinSbsqntSbcptUnits", "_MinRedPctg", "_HldgTrfbl", "_OthrRedRstrctns", "_MinInitlSbcptUnits", "_MaxRedUnits", "_MaxSwtchRedUnits", "_MinInitlSbcptAmt", "_MinSwtchSbcptAmt", "_MinSbsqntSbcptAmt"]
	@property
	def MinHldgAmt(self):
		return self._MinHldgAmt

	@MinHldgAmt.setter
	def MinHldgAmt(self, value):
		self._MinHldgAmt = value if type(value) != auto else self.make_default("MinHldgAmt")

	@MinHldgAmt.deleter
	def MinHldgAmt(self):
		del self._MinHldgAmt
		self._MinHldgAmt = None

	@property
	def MinSwtchSbcptUnits(self):
		return self._MinSwtchSbcptUnits

	@MinSwtchSbcptUnits.setter
	def MinSwtchSbcptUnits(self, value):
		self._MinSwtchSbcptUnits = value if type(value) != auto else self.make_default("MinSwtchSbcptUnits")

	@MinSwtchSbcptUnits.deleter
	def MinSwtchSbcptUnits(self):
		del self._MinSwtchSbcptUnits
		self._MinSwtchSbcptUnits = None

	@property
	def OthrSwtchRstrctns(self):
		return self._OthrSwtchRstrctns

	@OthrSwtchRstrctns.setter
	def OthrSwtchRstrctns(self, value):
		self._OthrSwtchRstrctns = value if type(value) != auto else self.make_default("OthrSwtchRstrctns")

	@OthrSwtchRstrctns.deleter
	def OthrSwtchRstrctns(self):
		del self._OthrSwtchRstrctns
		self._OthrSwtchRstrctns = None

	@property
	def MinHldgUnits(self):
		return self._MinHldgUnits

	@MinHldgUnits.setter
	def MinHldgUnits(self, value):
		self._MinHldgUnits = value if type(value) != auto else self.make_default("MinHldgUnits")

	@MinHldgUnits.deleter
	def MinHldgUnits(self):
		del self._MinHldgUnits
		self._MinHldgUnits = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def MinHldgPrd(self):
		return self._MinHldgPrd

	@MinHldgPrd.setter
	def MinHldgPrd(self, value):
		self._MinHldgPrd = value if type(value) != auto else self.make_default("MinHldgPrd")

	@MinHldgPrd.deleter
	def MinHldgPrd(self):
		del self._MinHldgPrd
		self._MinHldgPrd = None

	@property
	def MaxRedAmt(self):
		return self._MaxRedAmt

	@MaxRedAmt.setter
	def MaxRedAmt(self, value):
		self._MaxRedAmt = value if type(value) != auto else self.make_default("MaxRedAmt")

	@MaxRedAmt.deleter
	def MaxRedAmt(self):
		del self._MaxRedAmt
		self._MaxRedAmt = None

	@property
	def MaxSwtchRedAmt(self):
		return self._MaxSwtchRedAmt

	@MaxSwtchRedAmt.setter
	def MaxSwtchRedAmt(self, value):
		self._MaxSwtchRedAmt = value if type(value) != auto else self.make_default("MaxSwtchRedAmt")

	@MaxSwtchRedAmt.deleter
	def MaxSwtchRedAmt(self):
		del self._MaxSwtchRedAmt
		self._MaxSwtchRedAmt = None

	@property
	def MinSbsqntSbcptUnits(self):
		return self._MinSbsqntSbcptUnits

	@MinSbsqntSbcptUnits.setter
	def MinSbsqntSbcptUnits(self, value):
		self._MinSbsqntSbcptUnits = value if type(value) != auto else self.make_default("MinSbsqntSbcptUnits")

	@MinSbsqntSbcptUnits.deleter
	def MinSbsqntSbcptUnits(self):
		del self._MinSbsqntSbcptUnits
		self._MinSbsqntSbcptUnits = None

	@property
	def MinRedPctg(self):
		return self._MinRedPctg

	@MinRedPctg.setter
	def MinRedPctg(self, value):
		self._MinRedPctg = value if type(value) != auto else self.make_default("MinRedPctg")

	@MinRedPctg.deleter
	def MinRedPctg(self):
		del self._MinRedPctg
		self._MinRedPctg = None

	@property
	def HldgTrfbl(self):
		return self._HldgTrfbl

	@HldgTrfbl.setter
	def HldgTrfbl(self, value):
		self._HldgTrfbl = value if type(value) != auto else self.make_default("HldgTrfbl")

	@HldgTrfbl.deleter
	def HldgTrfbl(self):
		del self._HldgTrfbl
		self._HldgTrfbl = None

	@property
	def OthrRedRstrctns(self):
		return self._OthrRedRstrctns

	@OthrRedRstrctns.setter
	def OthrRedRstrctns(self, value):
		self._OthrRedRstrctns = value if type(value) != auto else self.make_default("OthrRedRstrctns")

	@OthrRedRstrctns.deleter
	def OthrRedRstrctns(self):
		del self._OthrRedRstrctns
		self._OthrRedRstrctns = None

	@property
	def MinInitlSbcptUnits(self):
		return self._MinInitlSbcptUnits

	@MinInitlSbcptUnits.setter
	def MinInitlSbcptUnits(self, value):
		self._MinInitlSbcptUnits = value if type(value) != auto else self.make_default("MinInitlSbcptUnits")

	@MinInitlSbcptUnits.deleter
	def MinInitlSbcptUnits(self):
		del self._MinInitlSbcptUnits
		self._MinInitlSbcptUnits = None

	@property
	def MaxRedUnits(self):
		return self._MaxRedUnits

	@MaxRedUnits.setter
	def MaxRedUnits(self, value):
		self._MaxRedUnits = value if type(value) != auto else self.make_default("MaxRedUnits")

	@MaxRedUnits.deleter
	def MaxRedUnits(self):
		del self._MaxRedUnits
		self._MaxRedUnits = None

	@property
	def MaxSwtchRedUnits(self):
		return self._MaxSwtchRedUnits

	@MaxSwtchRedUnits.setter
	def MaxSwtchRedUnits(self, value):
		self._MaxSwtchRedUnits = value if type(value) != auto else self.make_default("MaxSwtchRedUnits")

	@MaxSwtchRedUnits.deleter
	def MaxSwtchRedUnits(self):
		del self._MaxSwtchRedUnits
		self._MaxSwtchRedUnits = None

	@property
	def MinInitlSbcptAmt(self):
		return self._MinInitlSbcptAmt

	@MinInitlSbcptAmt.setter
	def MinInitlSbcptAmt(self, value):
		self._MinInitlSbcptAmt = value if type(value) != auto else self.make_default("MinInitlSbcptAmt")

	@MinInitlSbcptAmt.deleter
	def MinInitlSbcptAmt(self):
		del self._MinInitlSbcptAmt
		self._MinInitlSbcptAmt = None

	@property
	def MinSwtchSbcptAmt(self):
		return self._MinSwtchSbcptAmt

	@MinSwtchSbcptAmt.setter
	def MinSwtchSbcptAmt(self, value):
		self._MinSwtchSbcptAmt = value if type(value) != auto else self.make_default("MinSwtchSbcptAmt")

	@MinSwtchSbcptAmt.deleter
	def MinSwtchSbcptAmt(self):
		del self._MinSwtchSbcptAmt
		self._MinSwtchSbcptAmt = None

	@property
	def MinSbsqntSbcptAmt(self):
		return self._MinSbsqntSbcptAmt

	@MinSbsqntSbcptAmt.setter
	def MinSbsqntSbcptAmt(self, value):
		self._MinSbsqntSbcptAmt = value if type(value) != auto else self.make_default("MinSbsqntSbcptAmt")

	@MinSbsqntSbcptAmt.deleter
	def MinSbsqntSbcptAmt(self):
		del self._MinSbsqntSbcptAmt
		self._MinSbsqntSbcptAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinHldgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSwtchSbcptUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSwtchRstrctns', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinHldgUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MinHldgPrd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRedAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSwtchRedAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSbsqntSbcptUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinRedPctg', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgTrfbl', type=HoldingTransferable1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRedRstrctns', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinInitlSbcptUnits', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRedUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSwtchRedUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinInitlSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSwtchSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSbsqntSbcptAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

