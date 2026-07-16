# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text

class RemittanceInformation2(base_types._BaseFieldType):

	__slots__ = ["_Ustrd"]
	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if value is not None else base_types.UninitialisedField(self, 'Ustrd', Max140Text, True)

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = base_types.UninitialisedField(self, 'Ustrd', Max140Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))