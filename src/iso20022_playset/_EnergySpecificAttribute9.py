from . import base_types
from ._DeliveryInterconnectionPoint1Choice import DeliveryInterconnectionPoint1Choice
from ._EnergyLoadType1Code import EnergyLoadType1Code
from ._EnergyDeliveryAttribute10 import EnergyDeliveryAttribute10

class EnergySpecificAttribute9(base_types._BaseFieldType):

	__slots__ = ["_LdTp", "_DlvryPtOrZone", "_DlvryAttr", "_IntrCnnctnPt"]
	@property
	def LdTp(self):
		return self._LdTp

	@LdTp.setter
	def LdTp(self, value):
		self._LdTp = value if type(value) != base_types.auto else self.make_default("LdTp")

	@LdTp.deleter
	def LdTp(self):
		del self._LdTp
		self._LdTp = None

	@property
	def DlvryPtOrZone(self):
		return self._DlvryPtOrZone

	@DlvryPtOrZone.setter
	def DlvryPtOrZone(self, value):
		self._DlvryPtOrZone = value if type(value) != base_types.auto else self.make_default("DlvryPtOrZone")

	@DlvryPtOrZone.deleter
	def DlvryPtOrZone(self):
		del self._DlvryPtOrZone
		self._DlvryPtOrZone = None

	@property
	def DlvryAttr(self):
		return self._DlvryAttr

	@DlvryAttr.setter
	def DlvryAttr(self, value):
		self._DlvryAttr = value if type(value) != base_types.auto else self.make_default("DlvryAttr")

	@DlvryAttr.deleter
	def DlvryAttr(self):
		del self._DlvryAttr
		self._DlvryAttr = None

	@property
	def IntrCnnctnPt(self):
		return self._IntrCnnctnPt

	@IntrCnnctnPt.setter
	def IntrCnnctnPt(self, value):
		self._IntrCnnctnPt = value if type(value) != base_types.auto else self.make_default("IntrCnnctnPt")

	@IntrCnnctnPt.deleter
	def IntrCnnctnPt(self):
		del self._IntrCnnctnPt
		self._IntrCnnctnPt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LdTp', type=EnergyLoadType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryPtOrZone', type=DeliveryInterconnectionPoint1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryAttr', type=EnergyDeliveryAttribute10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrCnnctnPt', type=DeliveryInterconnectionPoint1Choice, min=0, max=1, mutex_group=None, array=False),
	))

