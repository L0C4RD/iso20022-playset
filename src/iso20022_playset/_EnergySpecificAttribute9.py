# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeliveryInterconnectionPoint1Choice
from . import EnergyDeliveryAttribute10
from . import EnergyLoadType1Code

class EnergySpecificAttribute9(base_types._BaseFieldType):

	__slots__ = ["_DlvryAttr", "_DlvryPtOrZone", "_IntrCnnctnPt", "_LdTp"]
	@property
	def DlvryAttr(self):
		return self._DlvryAttr

	@DlvryAttr.setter
	def DlvryAttr(self, value):
		self._DlvryAttr = value if value is not None else base_types.UninitialisedField(self, 'DlvryAttr', EnergyDeliveryAttribute10, True)

	@DlvryAttr.deleter
	def DlvryAttr(self):
		del self._DlvryAttr
		self._DlvryAttr = base_types.UninitialisedField(self, 'DlvryAttr', EnergyDeliveryAttribute10, True)

	@property
	def DlvryPtOrZone(self):
		return self._DlvryPtOrZone

	@DlvryPtOrZone.setter
	def DlvryPtOrZone(self, value):
		self._DlvryPtOrZone = value if value is not None else base_types.UninitialisedField(self, 'DlvryPtOrZone', DeliveryInterconnectionPoint1Choice, True)

	@DlvryPtOrZone.deleter
	def DlvryPtOrZone(self):
		del self._DlvryPtOrZone
		self._DlvryPtOrZone = base_types.UninitialisedField(self, 'DlvryPtOrZone', DeliveryInterconnectionPoint1Choice, True)

	@property
	def IntrCnnctnPt(self):
		return self._IntrCnnctnPt

	@IntrCnnctnPt.setter
	def IntrCnnctnPt(self, value):
		self._IntrCnnctnPt = value if value is not None else base_types.UninitialisedField(self, 'IntrCnnctnPt', DeliveryInterconnectionPoint1Choice, False)

	@IntrCnnctnPt.deleter
	def IntrCnnctnPt(self):
		del self._IntrCnnctnPt
		self._IntrCnnctnPt = base_types.UninitialisedField(self, 'IntrCnnctnPt', DeliveryInterconnectionPoint1Choice, False)

	@property
	def LdTp(self):
		return self._LdTp

	@LdTp.setter
	def LdTp(self, value):
		self._LdTp = value if value is not None else base_types.UninitialisedField(self, 'LdTp', EnergyLoadType1Code, False)

	@LdTp.deleter
	def LdTp(self):
		del self._LdTp
		self._LdTp = base_types.UninitialisedField(self, 'LdTp', EnergyLoadType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryAttr', type=EnergyDeliveryAttribute10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryPtOrZone', type=DeliveryInterconnectionPoint1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrCnnctnPt', type=DeliveryInterconnectionPoint1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LdTp', type=EnergyLoadType1Code, min=0, max=1, mutex_group=None, array=False),
	))