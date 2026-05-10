from . import base_types
from ._AmountAndDirection34 import AmountAndDirection34
from ._BalanceAdjustmentType1Code import BalanceAdjustmentType1Code
from ._Max105Text import Max105Text
from ._ISODate import ISODate
from ._DecimalNumber import DecimalNumber

class BalanceAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_BalAmt", "_ErrDt", "_Tp", "_Desc", "_AvrgAmt", "_Days", "_PstngDt", "_EarngsAdjstmntAmt"]
	@property
	def BalAmt(self):
		return self._BalAmt

	@BalAmt.setter
	def BalAmt(self, value):
		self._BalAmt = value if type(value) != base_types.auto else self.make_default("BalAmt")

	@BalAmt.deleter
	def BalAmt(self):
		del self._BalAmt
		self._BalAmt = None

	@property
	def ErrDt(self):
		return self._ErrDt

	@ErrDt.setter
	def ErrDt(self, value):
		self._ErrDt = value if type(value) != base_types.auto else self.make_default("ErrDt")

	@ErrDt.deleter
	def ErrDt(self):
		del self._ErrDt
		self._ErrDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
	def AvrgAmt(self):
		return self._AvrgAmt

	@AvrgAmt.setter
	def AvrgAmt(self, value):
		self._AvrgAmt = value if type(value) != base_types.auto else self.make_default("AvrgAmt")

	@AvrgAmt.deleter
	def AvrgAmt(self):
		del self._AvrgAmt
		self._AvrgAmt = None

	@property
	def Days(self):
		return self._Days

	@Days.setter
	def Days(self, value):
		self._Days = value if type(value) != base_types.auto else self.make_default("Days")

	@Days.deleter
	def Days(self):
		del self._Days
		self._Days = None

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if type(value) != base_types.auto else self.make_default("PstngDt")

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = None

	@property
	def EarngsAdjstmntAmt(self):
		return self._EarngsAdjstmntAmt

	@EarngsAdjstmntAmt.setter
	def EarngsAdjstmntAmt(self, value):
		self._EarngsAdjstmntAmt = value if type(value) != base_types.auto else self.make_default("EarngsAdjstmntAmt")

	@EarngsAdjstmntAmt.deleter
	def EarngsAdjstmntAmt(self):
		del self._EarngsAdjstmntAmt
		self._EarngsAdjstmntAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceAdjustmentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Days', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarngsAdjstmntAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))

