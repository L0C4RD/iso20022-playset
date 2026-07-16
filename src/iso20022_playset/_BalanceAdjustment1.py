# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BalanceAdjustmentType1Code
from . import DecimalNumber
from . import ISODate
from . import Max105Text

class BalanceAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_AvrgAmt", "_BalAmt", "_Days", "_Desc", "_EarngsAdjstmntAmt", "_ErrDt", "_PstngDt", "_Tp"]
	@property
	def AvrgAmt(self):
		return self._AvrgAmt

	@AvrgAmt.setter
	def AvrgAmt(self, value):
		self._AvrgAmt = value if value is not None else base_types.UninitialisedField(self, 'AvrgAmt', AmountAndDirection34, False)

	@AvrgAmt.deleter
	def AvrgAmt(self):
		del self._AvrgAmt
		self._AvrgAmt = base_types.UninitialisedField(self, 'AvrgAmt', AmountAndDirection34, False)

	@property
	def BalAmt(self):
		return self._BalAmt

	@BalAmt.setter
	def BalAmt(self, value):
		self._BalAmt = value if value is not None else base_types.UninitialisedField(self, 'BalAmt', AmountAndDirection34, False)

	@BalAmt.deleter
	def BalAmt(self):
		del self._BalAmt
		self._BalAmt = base_types.UninitialisedField(self, 'BalAmt', AmountAndDirection34, False)

	@property
	def Days(self):
		return self._Days

	@Days.setter
	def Days(self, value):
		self._Days = value if value is not None else base_types.UninitialisedField(self, 'Days', DecimalNumber, False)

	@Days.deleter
	def Days(self):
		del self._Days
		self._Days = base_types.UninitialisedField(self, 'Days', DecimalNumber, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max105Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max105Text, False)

	@property
	def EarngsAdjstmntAmt(self):
		return self._EarngsAdjstmntAmt

	@EarngsAdjstmntAmt.setter
	def EarngsAdjstmntAmt(self, value):
		self._EarngsAdjstmntAmt = value if value is not None else base_types.UninitialisedField(self, 'EarngsAdjstmntAmt', AmountAndDirection34, False)

	@EarngsAdjstmntAmt.deleter
	def EarngsAdjstmntAmt(self):
		del self._EarngsAdjstmntAmt
		self._EarngsAdjstmntAmt = base_types.UninitialisedField(self, 'EarngsAdjstmntAmt', AmountAndDirection34, False)

	@property
	def ErrDt(self):
		return self._ErrDt

	@ErrDt.setter
	def ErrDt(self, value):
		self._ErrDt = value if value is not None else base_types.UninitialisedField(self, 'ErrDt', ISODate, False)

	@ErrDt.deleter
	def ErrDt(self):
		del self._ErrDt
		self._ErrDt = base_types.UninitialisedField(self, 'ErrDt', ISODate, False)

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if value is not None else base_types.UninitialisedField(self, 'PstngDt', ISODate, False)

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = base_types.UninitialisedField(self, 'PstngDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BalanceAdjustmentType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BalanceAdjustmentType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Days', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarngsAdjstmntAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceAdjustmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))