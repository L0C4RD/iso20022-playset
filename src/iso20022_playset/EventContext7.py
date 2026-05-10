import base_types
import Max35Text
import PointOfInteractionComponent17
import RetailerService1Code

class EventContext7(base_types._BaseFieldType):

	__slots__ = ["_CmpntId", "_SvcTp", "_SaleId"]
	@property
	def CmpntId(self):
		return self._CmpntId

	@CmpntId.setter
	def CmpntId(self, value):
		self._CmpntId = value if type(value) != auto else self.make_default("CmpntId")

	@CmpntId.deleter
	def CmpntId(self):
		del self._CmpntId
		self._CmpntId = None

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if type(value) != auto else self.make_default("SaleId")

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpntId', type=PointOfInteractionComponent17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=RetailerService1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

