# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DisputeResolutionType1Code
from . import GenericIdentification30

class DisputeResolutionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_PrtryId"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', DisputeResolutionType1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', DisputeResolutionType1Code, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=DisputeResolutionType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))