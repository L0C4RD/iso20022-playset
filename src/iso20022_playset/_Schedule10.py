# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import LongFraction19DecimalNumber
from . import UnitOfMeasure8Choice

class Schedule10(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_UadjstdEndDt", "_UadjstdFctvDt", "_UnitOfMeasr"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	@property
	def UadjstdEndDt(self):
		return self._UadjstdEndDt

	@UadjstdEndDt.setter
	def UadjstdEndDt(self, value):
		self._UadjstdEndDt = value if value is not None else base_types.UninitialisedField(self, 'UadjstdEndDt', ISODate, False)

	@UadjstdEndDt.deleter
	def UadjstdEndDt(self):
		del self._UadjstdEndDt
		self._UadjstdEndDt = base_types.UninitialisedField(self, 'UadjstdEndDt', ISODate, False)

	@property
	def UadjstdFctvDt(self):
		return self._UadjstdFctvDt

	@UadjstdFctvDt.setter
	def UadjstdFctvDt(self, value):
		self._UadjstdFctvDt = value if value is not None else base_types.UninitialisedField(self, 'UadjstdFctvDt', ISODate, False)

	@UadjstdFctvDt.deleter
	def UadjstdFctvDt(self):
		del self._UadjstdFctvDt
		self._UadjstdFctvDt = base_types.UninitialisedField(self, 'UadjstdFctvDt', ISODate, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdFctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))