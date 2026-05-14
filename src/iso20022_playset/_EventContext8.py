from . import base_types
from ._Max35Text import Max35Text
from ._PointOfInteractionComponent18 import PointOfInteractionComponent18
from ._RetailerService1Code import RetailerService1Code

class EventContext8(base_types._BaseFieldType):

	__slots__ = ["_CmpntId", "_SaleId", "_SvcTp"]
	@property
	def CmpntId(self):
		return self._CmpntId

	@CmpntId.setter
	def CmpntId(self, value):
		self._CmpntId = value if type(value) != base_types.auto else self.make_default("CmpntId")

	@CmpntId.deleter
	def CmpntId(self):
		del self._CmpntId
		self._CmpntId = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != base_types.auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != base_types.auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpntId', type=PointOfInteractionComponent18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=RetailerService1Code, min=1, max=1, mutex_group=None, array=False),
	))

