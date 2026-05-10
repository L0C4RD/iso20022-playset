from . import base_types
from ._ISODate import ISODate
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Max1025Text import Max1025Text

class InterestPaymentSchedule1(base_types._BaseFieldType):

	__slots__ = ["_XpctdDt", "_DueDt", "_Amt", "_AddtlInf", "_IntrstSchdlId"]
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
	def IntrstSchdlId(self):
		return self._IntrstSchdlId

	@IntrstSchdlId.setter
	def IntrstSchdlId(self, value):
		self._IntrstSchdlId = value if type(value) != base_types.auto else self.make_default("IntrstSchdlId")

	@IntrstSchdlId.deleter
	def IntrstSchdlId(self):
		del self._IntrstSchdlId
		self._IntrstSchdlId = None

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
		base_types.FieldEntry(name='IntrstSchdlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

