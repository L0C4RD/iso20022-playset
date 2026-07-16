# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationSource1Choice
from . import Max35Text

class AlternateSecurityIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdSrc"]
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
	def IdSrc(self):
		return self._IdSrc

	@IdSrc.setter
	def IdSrc(self, value):
		self._IdSrc = value if value is not None else base_types.UninitialisedField(self, 'IdSrc', IdentificationSource1Choice, False)

	@IdSrc.deleter
	def IdSrc(self):
		del self._IdSrc
		self._IdSrc = base_types.UninitialisedField(self, 'IdSrc', IdentificationSource1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdSrc', type=IdentificationSource1Choice, min=1, max=1, mutex_group=None, array=False),
	))