# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import Max1025Text
from . import Max35Text

class PaymentSchedule1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_DueDt", "_PmtSchdlId", "_XpctdDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

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
	def PmtSchdlId(self):
		return self._PmtSchdlId

	@PmtSchdlId.setter
	def PmtSchdlId(self, value):
		self._PmtSchdlId = value if value is not None else base_types.UninitialisedField(self, 'PmtSchdlId', Max35Text, False)

	@PmtSchdlId.deleter
	def PmtSchdlId(self):
		del self._PmtSchdlId
		self._PmtSchdlId = base_types.UninitialisedField(self, 'PmtSchdlId', Max35Text, False)

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))