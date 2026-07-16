# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max16Text

class QueueTransactionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_PosInQ", "_QId"]
	@property
	def PosInQ(self):
		return self._PosInQ

	@PosInQ.setter
	def PosInQ(self, value):
		self._PosInQ = value if value is not None else base_types.UninitialisedField(self, 'PosInQ', Max16Text, False)

	@PosInQ.deleter
	def PosInQ(self):
		del self._PosInQ
		self._PosInQ = base_types.UninitialisedField(self, 'PosInQ', Max16Text, False)

	@property
	def QId(self):
		return self._QId

	@QId.setter
	def QId(self, value):
		self._QId = value if value is not None else base_types.UninitialisedField(self, 'QId', Max16Text, False)

	@QId.deleter
	def QId(self):
		del self._QId
		self._QId = base_types.UninitialisedField(self, 'QId', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PosInQ', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QId', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
	))