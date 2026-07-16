# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class SubAccount5(base_types._BaseFieldType):

	__slots__ = ["_Chrtc", "_Id", "_Nm"]
	@property
	def Chrtc(self):
		return self._Chrtc

	@Chrtc.setter
	def Chrtc(self, value):
		self._Chrtc = value if value is not None else base_types.UninitialisedField(self, 'Chrtc', Max35Text, False)

	@Chrtc.deleter
	def Chrtc(self):
		del self._Chrtc
		self._Chrtc = base_types.UninitialisedField(self, 'Chrtc', Max35Text, False)

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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrtc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))