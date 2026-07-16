# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import StructuredRemittanceInformation16

class RemittanceInformation16(base_types._BaseFieldType):

	__slots__ = ["_Strd", "_Ustrd"]
	@property
	def Strd(self):
		return self._Strd

	@Strd.setter
	def Strd(self, value):
		self._Strd = value if value is not None else base_types.UninitialisedField(self, 'Strd', StructuredRemittanceInformation16, True)

	@Strd.deleter
	def Strd(self):
		del self._Strd
		self._Strd = base_types.UninitialisedField(self, 'Strd', StructuredRemittanceInformation16, True)

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
		base_types.FieldEntry(name='Strd', type=StructuredRemittanceInformation16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ustrd', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))