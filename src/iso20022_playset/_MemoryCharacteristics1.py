# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max35Text
from . import MemoryUnit1Code

class MemoryCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_FreeSz", "_Id", "_TtlSz", "_Unit"]
	@property
	def FreeSz(self):
		return self._FreeSz

	@FreeSz.setter
	def FreeSz(self, value):
		self._FreeSz = value if value is not None else base_types.UninitialisedField(self, 'FreeSz', DecimalNumber, False)

	@FreeSz.deleter
	def FreeSz(self):
		del self._FreeSz
		self._FreeSz = base_types.UninitialisedField(self, 'FreeSz', DecimalNumber, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def TtlSz(self):
		return self._TtlSz

	@TtlSz.setter
	def TtlSz(self, value):
		self._TtlSz = value if value is not None else base_types.UninitialisedField(self, 'TtlSz', DecimalNumber, False)

	@TtlSz.deleter
	def TtlSz(self):
		del self._TtlSz
		self._TtlSz = base_types.UninitialisedField(self, 'TtlSz', DecimalNumber, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', MemoryUnit1Code, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', MemoryUnit1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FreeSz', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSz', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=MemoryUnit1Code, min=1, max=1, mutex_group=None, array=False),
	))