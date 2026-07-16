# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositiveNumber
from . import UnitOfMeasure5Choice

class ContractSize1(base_types._BaseFieldType):

	__slots__ = ["_LotSz", "_Unit"]
	@property
	def LotSz(self):
		return self._LotSz

	@LotSz.setter
	def LotSz(self, value):
		self._LotSz = value if value is not None else base_types.UninitialisedField(self, 'LotSz', PositiveNumber, False)

	@LotSz.deleter
	def LotSz(self):
		del self._LotSz
		self._LotSz = base_types.UninitialisedField(self, 'LotSz', PositiveNumber, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', UnitOfMeasure5Choice, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', UnitOfMeasure5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotSz', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=UnitOfMeasure5Choice, min=0, max=1, mutex_group=None, array=False),
	))