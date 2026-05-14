# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BICIdentification1 import BICIdentification1
from ._Max35Text import Max35Text

class DocumentIdentification5(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdIssr"]
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

	@property
	def IdIssr(self):
		return self._IdIssr

	@IdIssr.setter
	def IdIssr(self, value):
		self._IdIssr = value if type(value) != base_types.auto else self.make_default("IdIssr")

	@IdIssr.deleter
	def IdIssr(self):
		del self._IdIssr
		self._IdIssr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdIssr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))