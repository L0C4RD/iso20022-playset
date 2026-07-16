# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification32
from . import Max35Text
from . import Max70Text
from . import PointOfInteractionCapabilities1
from . import PointOfInteractionComponent1

class PointOfInteraction1(base_types._BaseFieldType):

	__slots__ = ["_Cmpnt", "_Cpblties", "_GrpId", "_Id", "_SysNm"]
	@property
	def Cmpnt(self):
		return self._Cmpnt

	@Cmpnt.setter
	def Cmpnt(self, value):
		self._Cmpnt = value if value is not None else base_types.UninitialisedField(self, 'Cmpnt', PointOfInteractionComponent1, True)

	@Cmpnt.deleter
	def Cmpnt(self):
		del self._Cmpnt
		self._Cmpnt = base_types.UninitialisedField(self, 'Cmpnt', PointOfInteractionComponent1, True)

	@property
	def Cpblties(self):
		return self._Cpblties

	@Cpblties.setter
	def Cpblties(self, value):
		self._Cpblties = value if value is not None else base_types.UninitialisedField(self, 'Cpblties', PointOfInteractionCapabilities1, False)

	@Cpblties.deleter
	def Cpblties(self):
		del self._Cpblties
		self._Cpblties = base_types.UninitialisedField(self, 'Cpblties', PointOfInteractionCapabilities1, False)

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if value is not None else base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification32, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification32, False)

	@property
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if value is not None else base_types.UninitialisedField(self, 'SysNm', Max70Text, False)

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = base_types.UninitialisedField(self, 'SysNm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmpnt', type=PointOfInteractionComponent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cpblties', type=PointOfInteractionCapabilities1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))