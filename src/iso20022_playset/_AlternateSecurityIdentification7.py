# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IdentificationSource1Choice import IdentificationSource1Choice
from ._Max35Text import Max35Text

class AlternateSecurityIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdSrc"]
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
	def IdSrc(self):
		return self._IdSrc

	@IdSrc.setter
	def IdSrc(self, value):
		self._IdSrc = value if type(value) != base_types.auto else self.make_default("IdSrc")

	@IdSrc.deleter
	def IdSrc(self):
		del self._IdSrc
		self._IdSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdSrc', type=IdentificationSource1Choice, min=1, max=1, mutex_group=None, array=False),
	))