# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PositiveNumber import PositiveNumber
from ._UnitOfMeasure5Choice import UnitOfMeasure5Choice

class ContractSize1(base_types._BaseFieldType):

	__slots__ = ["_LotSz", "_Unit"]
	@property
	def LotSz(self):
		return self._LotSz

	@LotSz.setter
	def LotSz(self, value):
		self._LotSz = value if type(value) != base_types.auto else self.make_default("LotSz")

	@LotSz.deleter
	def LotSz(self):
		del self._LotSz
		self._LotSz = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotSz', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=UnitOfMeasure5Choice, min=0, max=1, mutex_group=None, array=False),
	))