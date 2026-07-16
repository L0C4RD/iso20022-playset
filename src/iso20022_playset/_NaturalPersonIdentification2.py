# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification175
from . import Max105Text
from . import Max500Text

class NaturalPersonIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Dmcl", "_Id", "_Nm"]
	@property
	def Dmcl(self):
		return self._Dmcl

	@Dmcl.setter
	def Dmcl(self, value):
		self._Dmcl = value if value is not None else base_types.UninitialisedField(self, 'Dmcl', Max500Text, False)

	@Dmcl.deleter
	def Dmcl(self):
		del self._Dmcl
		self._Dmcl = base_types.UninitialisedField(self, 'Dmcl', Max500Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification175, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification175, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max105Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max105Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmcl', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification175, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
	))