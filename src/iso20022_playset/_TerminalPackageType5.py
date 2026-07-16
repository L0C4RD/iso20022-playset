# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PackageType5
from . import PointOfInteractionComponentIdentification2

class TerminalPackageType5(base_types._BaseFieldType):

	__slots__ = ["_POICmpntId", "_Packg"]
	@property
	def POICmpntId(self):
		return self._POICmpntId

	@POICmpntId.setter
	def POICmpntId(self, value):
		self._POICmpntId = value if value is not None else base_types.UninitialisedField(self, 'POICmpntId', PointOfInteractionComponentIdentification2, True)

	@POICmpntId.deleter
	def POICmpntId(self):
		del self._POICmpntId
		self._POICmpntId = base_types.UninitialisedField(self, 'POICmpntId', PointOfInteractionComponentIdentification2, True)

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if value is not None else base_types.UninitialisedField(self, 'Packg', PackageType5, True)

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = base_types.UninitialisedField(self, 'Packg', PackageType5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='POICmpntId', type=PointOfInteractionComponentIdentification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Packg', type=PackageType5, min=1, max=None, mutex_group=None, array=True),
	))