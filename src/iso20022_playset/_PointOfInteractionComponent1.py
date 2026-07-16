# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max16Text
from . import Max35Text
from . import Max70Text
from . import POIComponentType1Code

class PointOfInteractionComponent1(base_types._BaseFieldType):

	__slots__ = ["_ApprvlNb", "_ManfctrId", "_Mdl", "_POICmpntTp", "_SrlNb", "_VrsnNb"]
	@property
	def ApprvlNb(self):
		return self._ApprvlNb

	@ApprvlNb.setter
	def ApprvlNb(self, value):
		self._ApprvlNb = value if value is not None else base_types.UninitialisedField(self, 'ApprvlNb', Max70Text, True)

	@ApprvlNb.deleter
	def ApprvlNb(self):
		del self._ApprvlNb
		self._ApprvlNb = base_types.UninitialisedField(self, 'ApprvlNb', Max70Text, True)

	@property
	def ManfctrId(self):
		return self._ManfctrId

	@ManfctrId.setter
	def ManfctrId(self, value):
		self._ManfctrId = value if value is not None else base_types.UninitialisedField(self, 'ManfctrId', Max35Text, False)

	@ManfctrId.deleter
	def ManfctrId(self):
		del self._ManfctrId
		self._ManfctrId = base_types.UninitialisedField(self, 'ManfctrId', Max35Text, False)

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if value is not None else base_types.UninitialisedField(self, 'Mdl', Max35Text, False)

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = base_types.UninitialisedField(self, 'Mdl', Max35Text, False)

	@property
	def POICmpntTp(self):
		return self._POICmpntTp

	@POICmpntTp.setter
	def POICmpntTp(self, value):
		self._POICmpntTp = value if value is not None else base_types.UninitialisedField(self, 'POICmpntTp', POIComponentType1Code, False)

	@POICmpntTp.deleter
	def POICmpntTp(self):
		del self._POICmpntTp
		self._POICmpntTp = base_types.UninitialisedField(self, 'POICmpntTp', POIComponentType1Code, False)

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if value is not None else base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = base_types.UninitialisedField(self, 'SrlNb', Max35Text, False)

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if value is not None else base_types.UninitialisedField(self, 'VrsnNb', Max16Text, False)

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = base_types.UninitialisedField(self, 'VrsnNb', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlNb', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ManfctrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpntTp', type=POIComponentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))