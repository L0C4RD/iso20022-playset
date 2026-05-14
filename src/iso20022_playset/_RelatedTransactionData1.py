# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UUIDv4Identifier import UUIDv4Identifier

class RelatedTransactionData1(base_types._BaseFieldType):

	__slots__ = ["_MstrUETR", "_SubUETR"]
	@property
	def MstrUETR(self):
		return self._MstrUETR

	@MstrUETR.setter
	def MstrUETR(self, value):
		self._MstrUETR = value if type(value) != base_types.auto else self.make_default("MstrUETR")

	@MstrUETR.deleter
	def MstrUETR(self):
		del self._MstrUETR
		self._MstrUETR = None

	@property
	def SubUETR(self):
		return self._SubUETR

	@SubUETR.setter
	def SubUETR(self, value):
		self._SubUETR = value if type(value) != base_types.auto else self.make_default("SubUETR")

	@SubUETR.deleter
	def SubUETR(self):
		del self._SubUETR
		self._SubUETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MstrUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubUETR', type=UUIDv4Identifier, min=0, max=None, mutex_group=None, array=True),
	))