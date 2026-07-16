# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Frequency19Code
from . import LongFraction19DecimalNumber
from . import Max3Number
from . import UnitOfMeasure8Choice

class QuantityTerm1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_TmUnit", "_UnitOfMeasr", "_Val"]
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
	def TmUnit(self):
		return self._TmUnit

	@TmUnit.setter
	def TmUnit(self, value):
		self._TmUnit = value if value is not None else base_types.UninitialisedField(self, 'TmUnit', Frequency19Code, False)

	@TmUnit.deleter
	def TmUnit(self):
		del self._TmUnit
		self._TmUnit = base_types.UninitialisedField(self, 'TmUnit', Frequency19Code, False)

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

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max3Number, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max3Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmUnit', type=Frequency19Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
	))