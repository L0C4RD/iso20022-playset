from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .DisputeResolutionType2Code import DisputeResolutionType2Code

class DisputeResolutionType2Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryId", "_Cd"]
	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=DisputeResolutionType2Code, min=0, max=1, mutex_group=1, array=False),
	))

