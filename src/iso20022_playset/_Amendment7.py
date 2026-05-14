# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Amendment8 import Amendment8
from ._UndertakingStatus2Code import UndertakingStatus2Code

class Amendment7(base_types._BaseFieldType):

	__slots__ = ["_AmdmntId", "_AmdmntSts"]
	@property
	def AmdmntId(self):
		return self._AmdmntId

	@AmdmntId.setter
	def AmdmntId(self, value):
		self._AmdmntId = value if type(value) != base_types.auto else self.make_default("AmdmntId")

	@AmdmntId.deleter
	def AmdmntId(self):
		del self._AmdmntId
		self._AmdmntId = None

	@property
	def AmdmntSts(self):
		return self._AmdmntSts

	@AmdmntSts.setter
	def AmdmntSts(self, value):
		self._AmdmntSts = value if type(value) != base_types.auto else self.make_default("AmdmntSts")

	@AmdmntSts.deleter
	def AmdmntSts(self):
		del self._AmdmntSts
		self._AmdmntSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntId', type=Amendment8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntSts', type=UndertakingStatus2Code, min=1, max=1, mutex_group=None, array=False),
	))