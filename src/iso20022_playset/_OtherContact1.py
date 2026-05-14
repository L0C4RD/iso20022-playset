# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max128Text import Max128Text
from ._Max4Text import Max4Text

class OtherContact1(base_types._BaseFieldType):

	__slots__ = ["_ChanlTp", "_Id"]
	@property
	def ChanlTp(self):
		return self._ChanlTp

	@ChanlTp.setter
	def ChanlTp(self, value):
		self._ChanlTp = value if type(value) != base_types.auto else self.make_default("ChanlTp")

	@ChanlTp.deleter
	def ChanlTp(self):
		del self._ChanlTp
		self._ChanlTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChanlTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max128Text, min=0, max=1, mutex_group=None, array=False),
	))