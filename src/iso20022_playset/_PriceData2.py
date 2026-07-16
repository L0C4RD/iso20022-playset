# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LongFraction19DecimalNumber
from . import Schedule1
from . import SecuritiesTransactionPrice17Choice
from . import UnitOfMeasure8Choice

class PriceData2(base_types._BaseFieldType):

	__slots__ = ["_Pric", "_PricMltplr", "_SchdlPrd", "_UnitOfMeasr"]
	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice17Choice, False)

	@property
	def PricMltplr(self):
		return self._PricMltplr

	@PricMltplr.setter
	def PricMltplr(self, value):
		self._PricMltplr = value if value is not None else base_types.UninitialisedField(self, 'PricMltplr', LongFraction19DecimalNumber, False)

	@PricMltplr.deleter
	def PricMltplr(self):
		del self._PricMltplr
		self._PricMltplr = base_types.UninitialisedField(self, 'PricMltplr', LongFraction19DecimalNumber, False)

	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if value is not None else base_types.UninitialisedField(self, 'SchdlPrd', Schedule1, True)

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = base_types.UninitialisedField(self, 'SchdlPrd', Schedule1, True)

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
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMltplr', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdlPrd', type=Schedule1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))