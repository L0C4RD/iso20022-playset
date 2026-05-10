from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISODate import ISODate
from ._Max1025Text import Max1025Text
from ._Max35Text import Max35Text

class PaymentSchedule1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_DueDt", "_PmtSchdlId", "_XpctdDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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
	def PmtSchdlId(self):
		return self._PmtSchdlId

	@PmtSchdlId.setter
	def PmtSchdlId(self, value):
		self._PmtSchdlId = value if type(value) != base_types.auto else self.make_default("PmtSchdlId")

	@PmtSchdlId.deleter
	def PmtSchdlId(self):
		del self._PmtSchdlId
		self._PmtSchdlId = None

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if type(value) != base_types.auto else self.make_default("XpctdDt")

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

