# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import ISODate

class Capped1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_IncmCurPrd", "_IncmLmtCurPrd", "_IncmLmtNxtPrd", "_StartDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def IncmCurPrd(self):
		return self._IncmCurPrd

	@IncmCurPrd.setter
	def IncmCurPrd(self, value):
		self._IncmCurPrd = value if value is not None else base_types.UninitialisedField(self, 'IncmCurPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@IncmCurPrd.deleter
	def IncmCurPrd(self):
		del self._IncmCurPrd
		self._IncmCurPrd = base_types.UninitialisedField(self, 'IncmCurPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def IncmLmtCurPrd(self):
		return self._IncmLmtCurPrd

	@IncmLmtCurPrd.setter
	def IncmLmtCurPrd(self, value):
		self._IncmLmtCurPrd = value if value is not None else base_types.UninitialisedField(self, 'IncmLmtCurPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@IncmLmtCurPrd.deleter
	def IncmLmtCurPrd(self):
		del self._IncmLmtCurPrd
		self._IncmLmtCurPrd = base_types.UninitialisedField(self, 'IncmLmtCurPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def IncmLmtNxtPrd(self):
		return self._IncmLmtNxtPrd

	@IncmLmtNxtPrd.setter
	def IncmLmtNxtPrd(self, value):
		self._IncmLmtNxtPrd = value if value is not None else base_types.UninitialisedField(self, 'IncmLmtNxtPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@IncmLmtNxtPrd.deleter
	def IncmLmtNxtPrd(self):
		del self._IncmLmtNxtPrd
		self._IncmLmtNxtPrd = base_types.UninitialisedField(self, 'IncmLmtNxtPrd', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncmCurPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmLmtCurPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmLmtNxtPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))