from . import base_types
from ._CurrencyAndAmount import CurrencyAndAmount
from ._ISODate import ISODate
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._PaymentPeriod1 import PaymentPeriod1
from ._PercentageRate import PercentageRate

class PaymentTerms6(base_types._BaseFieldType):

	__slots__ = ["_BsisAmt", "_Desc", "_DrctDbtMndtId", "_DscntAmt", "_DscntPctRate", "_DueDt", "_PmtPrd", "_PnltyAmt", "_PnltyPctRate", "_PrtlPmtPct"]
	@property
	def BsisAmt(self):
		return self._BsisAmt

	@BsisAmt.setter
	def BsisAmt(self, value):
		self._BsisAmt = value if type(value) != base_types.auto else self.make_default("BsisAmt")

	@BsisAmt.deleter
	def BsisAmt(self):
		del self._BsisAmt
		self._BsisAmt = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def DrctDbtMndtId(self):
		return self._DrctDbtMndtId

	@DrctDbtMndtId.setter
	def DrctDbtMndtId(self, value):
		self._DrctDbtMndtId = value if type(value) != base_types.auto else self.make_default("DrctDbtMndtId")

	@DrctDbtMndtId.deleter
	def DrctDbtMndtId(self):
		del self._DrctDbtMndtId
		self._DrctDbtMndtId = None

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if type(value) != base_types.auto else self.make_default("DscntAmt")

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = None

	@property
	def DscntPctRate(self):
		return self._DscntPctRate

	@DscntPctRate.setter
	def DscntPctRate(self, value):
		self._DscntPctRate = value if type(value) != base_types.auto else self.make_default("DscntPctRate")

	@DscntPctRate.deleter
	def DscntPctRate(self):
		del self._DscntPctRate
		self._DscntPctRate = None

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != base_types.auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def PmtPrd(self):
		return self._PmtPrd

	@PmtPrd.setter
	def PmtPrd(self, value):
		self._PmtPrd = value if type(value) != base_types.auto else self.make_default("PmtPrd")

	@PmtPrd.deleter
	def PmtPrd(self):
		del self._PmtPrd
		self._PmtPrd = None

	@property
	def PnltyAmt(self):
		return self._PnltyAmt

	@PnltyAmt.setter
	def PnltyAmt(self, value):
		self._PnltyAmt = value if type(value) != base_types.auto else self.make_default("PnltyAmt")

	@PnltyAmt.deleter
	def PnltyAmt(self):
		del self._PnltyAmt
		self._PnltyAmt = None

	@property
	def PnltyPctRate(self):
		return self._PnltyPctRate

	@PnltyPctRate.setter
	def PnltyPctRate(self, value):
		self._PnltyPctRate = value if type(value) != base_types.auto else self.make_default("PnltyPctRate")

	@PnltyPctRate.deleter
	def PnltyPctRate(self):
		del self._PnltyPctRate
		self._PnltyPctRate = None

	@property
	def PrtlPmtPct(self):
		return self._PrtlPmtPct

	@PrtlPmtPct.setter
	def PrtlPmtPct(self, value):
		self._PrtlPmtPct = value if type(value) != base_types.auto else self.make_default("PrtlPmtPct")

	@PrtlPmtPct.deleter
	def PrtlPmtPct(self):
		del self._PrtlPmtPct
		self._PrtlPmtPct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisAmt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrctDbtMndtId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DscntAmt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPctRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtPrd', type=PaymentPeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyAmt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnltyPctRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlPmtPct', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

