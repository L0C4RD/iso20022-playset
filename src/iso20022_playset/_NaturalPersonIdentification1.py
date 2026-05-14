# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IdentificationType45Choice import IdentificationType45Choice
from ._Max35Text import Max35Text

class NaturalPersonIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdTp"]
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
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != base_types.auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=IdentificationType45Choice, min=0, max=1, mutex_group=None, array=False),
	))