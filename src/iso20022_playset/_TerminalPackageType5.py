from . import base_types
from ._PackageType5 import PackageType5
from ._PointOfInteractionComponentIdentification2 import PointOfInteractionComponentIdentification2

class TerminalPackageType5(base_types._BaseFieldType):

	__slots__ = ["_POICmpntId", "_Packg"]
	@property
	def POICmpntId(self):
		return self._POICmpntId

	@POICmpntId.setter
	def POICmpntId(self, value):
		self._POICmpntId = value if type(value) != base_types.auto else self.make_default("POICmpntId")

	@POICmpntId.deleter
	def POICmpntId(self):
		del self._POICmpntId
		self._POICmpntId = None

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if type(value) != base_types.auto else self.make_default("Packg")

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POICmpntId', type=PointOfInteractionComponentIdentification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Packg', type=PackageType5, min=1, max=None, mutex_group=None, array=True),
	))

