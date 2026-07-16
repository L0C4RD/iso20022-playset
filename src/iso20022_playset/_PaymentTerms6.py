# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import ISODate
from . import Max140Text
from . import Max35Text
from . import PaymentPeriod1
from . import PercentageRate

class PaymentTerms6(base_types._BaseFieldType):

	__slots__ = ["_BsisAmt", "_Desc", "_DrctDbtMndtId", "_DscntAmt", "_DscntPctRate", "_DueDt", "_PmtPrd", "_PnltyAmt", "_PnltyPctRate", "_PrtlPmtPct"]
	@property
	def BsisAmt(self):
		return self._BsisAmt

	@BsisAmt.setter
	def BsisAmt(self, value):
		self._BsisAmt = value if value is not None else base_types.UninitialisedField(self, 'BsisAmt', CurrencyAndAmount, False)

	@BsisAmt.deleter
	def BsisAmt(self):
		del self._BsisAmt
		self._BsisAmt = base_types.UninitialisedField(self, 'BsisAmt', CurrencyAndAmount, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, True)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, True)

	@property
	def DrctDbtMndtId(self):
		return self._DrctDbtMndtId

	@DrctDbtMndtId.setter
	def DrctDbtMndtId(self, value):
		self._DrctDbtMndtId = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtMndtId', Max35Text, True)

	@DrctDbtMndtId.deleter
	def DrctDbtMndtId(self):
		del self._DrctDbtMndtId
		self._DrctDbtMndtId = base_types.UninitialisedField(self, 'DrctDbtMndtId', Max35Text, True)

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntAmt', CurrencyAndAmount, False)

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = base_types.UninitialisedField(self, 'DscntAmt', CurrencyAndAmount, False)

	@property
	def DscntPctRate(self):
		return self._DscntPctRate

	@DscntPctRate.setter
	def DscntPctRate(self, value):
		self._DscntPctRate = value if value is not None else base_types.UninitialisedField(self, 'DscntPctRate', PercentageRate, False)

	@DscntPctRate.deleter
	def DscntPctRate(self):
		del self._DscntPctRate
		self._DscntPctRate = base_types.UninitialisedField(self, 'DscntPctRate', PercentageRate, False)

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@property
	def PmtPrd(self):
		return self._PmtPrd

	@PmtPrd.setter
	def PmtPrd(self, value):
		self._PmtPrd = value if value is not None else base_types.UninitialisedField(self, 'PmtPrd', PaymentPeriod1, False)

	@PmtPrd.deleter
	def PmtPrd(self):
		del self._PmtPrd
		self._PmtPrd = base_types.UninitialisedField(self, 'PmtPrd', PaymentPeriod1, False)

	@property
	def PnltyAmt(self):
		return self._PnltyAmt

	@PnltyAmt.setter
	def PnltyAmt(self, value):
		self._PnltyAmt = value if value is not None else base_types.UninitialisedField(self, 'PnltyAmt', CurrencyAndAmount, False)

	@PnltyAmt.deleter
	def PnltyAmt(self):
		del self._PnltyAmt
		self._PnltyAmt = base_types.UninitialisedField(self, 'PnltyAmt', CurrencyAndAmount, False)

	@property
	def PnltyPctRate(self):
		return self._PnltyPctRate

	@PnltyPctRate.setter
	def PnltyPctRate(self, value):
		self._PnltyPctRate = value if value is not None else base_types.UninitialisedField(self, 'PnltyPctRate', PercentageRate, False)

	@PnltyPctRate.deleter
	def PnltyPctRate(self):
		del self._PnltyPctRate
		self._PnltyPctRate = base_types.UninitialisedField(self, 'PnltyPctRate', PercentageRate, False)

	@property
	def PrtlPmtPct(self):
		return self._PrtlPmtPct

	@PrtlPmtPct.setter
	def PrtlPmtPct(self, value):
		self._PrtlPmtPct = value if value is not None else base_types.UninitialisedField(self, 'PrtlPmtPct', PercentageRate, False)

	@PrtlPmtPct.deleter
	def PrtlPmtPct(self):
		del self._PrtlPmtPct
		self._PrtlPmtPct = base_types.UninitialisedField(self, 'PrtlPmtPct', PercentageRate, False)

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