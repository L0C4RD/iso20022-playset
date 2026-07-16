# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber5Choice
from . import Identification32

class DocumentNumber22(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_Refs"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', DocumentNumber5Choice, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', DocumentNumber5Choice, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', Identification32, True)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', Identification32, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=DocumentNumber5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=Identification32, min=1, max=None, mutex_group=None, array=True),
	))