from . import base_types
import ActiveCurrencyAnd13DecimalAmount
import ISODate
import AdditionalInformation15

class Capped1(base_types._BaseFieldType):

	__slots__ = ["_IncmCurPrd", "_IncmLmtNxtPrd", "_IncmLmtCurPrd", "_StartDt", "_AddtlInf"]
	@property
	def IncmCurPrd(self):
		return self._IncmCurPrd

	@IncmCurPrd.setter
	def IncmCurPrd(self, value):
		self._IncmCurPrd = value if type(value) != auto else self.make_default("IncmCurPrd")

	@IncmCurPrd.deleter
	def IncmCurPrd(self):
		del self._IncmCurPrd
		self._IncmCurPrd = None

	@property
	def IncmLmtNxtPrd(self):
		return self._IncmLmtNxtPrd

	@IncmLmtNxtPrd.setter
	def IncmLmtNxtPrd(self, value):
		self._IncmLmtNxtPrd = value if type(value) != auto else self.make_default("IncmLmtNxtPrd")

	@IncmLmtNxtPrd.deleter
	def IncmLmtNxtPrd(self):
		del self._IncmLmtNxtPrd
		self._IncmLmtNxtPrd = None

	@property
	def IncmLmtCurPrd(self):
		return self._IncmLmtCurPrd

	@IncmLmtCurPrd.setter
	def IncmLmtCurPrd(self, value):
		self._IncmLmtCurPrd = value if type(value) != auto else self.make_default("IncmLmtCurPrd")

	@IncmLmtCurPrd.deleter
	def IncmLmtCurPrd(self):
		del self._IncmLmtCurPrd
		self._IncmLmtCurPrd = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncmCurPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmLmtNxtPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmLmtCurPrd', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

