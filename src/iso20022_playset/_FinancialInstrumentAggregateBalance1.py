# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAggregateBalance1Choice
from . import ISODate
from . import Price6

class FinancialInstrumentAggregateBalance1(base_types._BaseFieldType):

	__slots__ = ["_Hldgs", "_ItmDt", "_Pric"]
	@property
	def Hldgs(self):
		return self._Hldgs

	@Hldgs.setter
	def Hldgs(self, value):
		self._Hldgs = value if value is not None else base_types.UninitialisedField(self, 'Hldgs', FinancialInstrumentAggregateBalance1Choice, False)

	@Hldgs.deleter
	def Hldgs(self):
		del self._Hldgs
		self._Hldgs = base_types.UninitialisedField(self, 'Hldgs', FinancialInstrumentAggregateBalance1Choice, False)

	@property
	def ItmDt(self):
		return self._ItmDt

	@ItmDt.setter
	def ItmDt(self, value):
		self._ItmDt = value if value is not None else base_types.UninitialisedField(self, 'ItmDt', ISODate, False)

	@ItmDt.deleter
	def ItmDt(self):
		del self._ItmDt
		self._ItmDt = base_types.UninitialisedField(self, 'ItmDt', ISODate, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', Price6, True)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', Price6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hldgs', type=FinancialInstrumentAggregateBalance1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price6, min=0, max=None, mutex_group=None, array=True),
	))