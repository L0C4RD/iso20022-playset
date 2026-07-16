# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment8
from . import UndertakingStatus2Code

class Amendment7(base_types._BaseFieldType):

	__slots__ = ["_AmdmntId", "_AmdmntSts"]
	@property
	def AmdmntId(self):
		return self._AmdmntId

	@AmdmntId.setter
	def AmdmntId(self, value):
		self._AmdmntId = value if value is not None else base_types.UninitialisedField(self, 'AmdmntId', Amendment8, False)

	@AmdmntId.deleter
	def AmdmntId(self):
		del self._AmdmntId
		self._AmdmntId = base_types.UninitialisedField(self, 'AmdmntId', Amendment8, False)

	@property
	def AmdmntSts(self):
		return self._AmdmntSts

	@AmdmntSts.setter
	def AmdmntSts(self, value):
		self._AmdmntSts = value if value is not None else base_types.UninitialisedField(self, 'AmdmntSts', UndertakingStatus2Code, False)

	@AmdmntSts.deleter
	def AmdmntSts(self):
		del self._AmdmntSts
		self._AmdmntSts = base_types.UninitialisedField(self, 'AmdmntSts', UndertakingStatus2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntId', type=Amendment8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntSts', type=UndertakingStatus2Code, min=1, max=1, mutex_group=None, array=False),
	))