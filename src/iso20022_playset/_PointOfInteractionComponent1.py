from . import base_types
from ._Max16Text import Max16Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._POIComponentType1Code import POIComponentType1Code

class PointOfInteractionComponent1(base_types._BaseFieldType):

	__slots__ = ["_ApprvlNb", "_ManfctrId", "_Mdl", "_POICmpntTp", "_SrlNb", "_VrsnNb"]
	@property
	def ApprvlNb(self):
		return self._ApprvlNb

	@ApprvlNb.setter
	def ApprvlNb(self, value):
		self._ApprvlNb = value if type(value) != base_types.auto else self.make_default("ApprvlNb")

	@ApprvlNb.deleter
	def ApprvlNb(self):
		del self._ApprvlNb
		self._ApprvlNb = None

	@property
	def ManfctrId(self):
		return self._ManfctrId

	@ManfctrId.setter
	def ManfctrId(self, value):
		self._ManfctrId = value if type(value) != base_types.auto else self.make_default("ManfctrId")

	@ManfctrId.deleter
	def ManfctrId(self):
		del self._ManfctrId
		self._ManfctrId = None

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if type(value) != base_types.auto else self.make_default("Mdl")

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = None

	@property
	def POICmpntTp(self):
		return self._POICmpntTp

	@POICmpntTp.setter
	def POICmpntTp(self, value):
		self._POICmpntTp = value if type(value) != base_types.auto else self.make_default("POICmpntTp")

	@POICmpntTp.deleter
	def POICmpntTp(self):
		del self._POICmpntTp
		self._POICmpntTp = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != base_types.auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if type(value) != base_types.auto else self.make_default("VrsnNb")

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlNb', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ManfctrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpntTp', type=POIComponentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))

