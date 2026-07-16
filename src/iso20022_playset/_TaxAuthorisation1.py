# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text

class TaxAuthorisation1(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_Titl"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def Titl(self):
		return self._Titl

	@Titl.setter
	def Titl(self, value):
		self._Titl = value if value is not None else base_types.UninitialisedField(self, 'Titl', Max35Text, False)

	@Titl.deleter
	def Titl(self):
		del self._Titl
		self._Titl = base_types.UninitialisedField(self, 'Titl', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Titl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))