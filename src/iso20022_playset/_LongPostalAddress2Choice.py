# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import PostalAddress1

class LongPostalAddress2Choice(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_Ustrd"]
	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if value is not None else base_types.UninitialisedField(self, 'Strd', PostalAddress1, False)

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = base_types.UninitialisedField(self, 'Strd', PostalAddress1, False)

	@property
	def Ustrd(self):
		return self._Ustrd

	@Ustrd.setter
	def Ustrd(self, value):
		self._Ustrd = value if value is not None else base_types.UninitialisedField(self, 'Ustrd', Max350Text, False)

	@Ustrd.deleter
	def Ustrd(self):
		del self._Ustrd
		self._Ustrd = base_types.UninitialisedField(self, 'Ustrd', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strd', type=PostalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ustrd', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
	))