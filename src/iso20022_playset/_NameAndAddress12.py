# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax140Text

class NameAndAddress12(base_types._BaseFieldType):

	__slots__ = ["_Nm"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', RestrictedFINXMax140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', RestrictedFINXMax140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=RestrictedFINXMax140Text, min=1, max=1, mutex_group=None, array=False),
	))