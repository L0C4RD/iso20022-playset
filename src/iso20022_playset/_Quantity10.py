# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import UnitOfMeasure3Choice

class Quantity10(base_types._BaseFieldType):

	__slots__ = ["_UnitOfMeasr", "_Val"]
	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure3Choice, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure3Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', DecimalNumber, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))