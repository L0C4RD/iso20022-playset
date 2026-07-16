# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINMax30Text
from . import RestrictedFINMax8Text

class GenericIdentification39(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Issr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', RestrictedFINMax30Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', RestrictedFINMax30Text, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', RestrictedFINMax8Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', RestrictedFINMax8Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=RestrictedFINMax30Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=RestrictedFINMax8Text, min=0, max=1, mutex_group=None, array=False),
	))