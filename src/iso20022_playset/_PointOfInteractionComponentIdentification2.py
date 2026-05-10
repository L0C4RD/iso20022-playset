from . import base_types
from ._Max35Text import Max35Text
from ._Max256Text import Max256Text

class PointOfInteractionComponentIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_SrlNb", "_ItmNb", "_PrvdrId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
	def ItmNb(self):
		return self._ItmNb

	@ItmNb.setter
	def ItmNb(self, value):
		self._ItmNb = value if type(value) != base_types.auto else self.make_default("ItmNb")

	@ItmNb.deleter
	def ItmNb(self):
		del self._ItmNb
		self._ItmNb = None

	@property
	def PrvdrId(self):
		return self._PrvdrId

	@PrvdrId.setter
	def PrvdrId(self, value):
		self._PrvdrId = value if type(value) != base_types.auto else self.make_default("PrvdrId")

	@PrvdrId.deleter
	def PrvdrId(self):
		del self._PrvdrId
		self._PrvdrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

