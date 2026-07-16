# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max35Text
from . import PostalAddress1

class NameAndAddress8(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_AltrntvIdr", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', PostalAddress1, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', PostalAddress1, False)

	@property
	def AltrntvIdr(self):
		return self._AltrntvIdr

	@AltrntvIdr.setter
	def AltrntvIdr(self, value):
		self._AltrntvIdr = value if value is not None else base_types.UninitialisedField(self, 'AltrntvIdr', Max35Text, True)

	@AltrntvIdr.deleter
	def AltrntvIdr(self):
		del self._AltrntvIdr
		self._AltrntvIdr = base_types.UninitialisedField(self, 'AltrntvIdr', Max35Text, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvIdr', type=Max35Text, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))