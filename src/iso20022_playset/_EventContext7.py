# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PointOfInteractionComponent17
from . import RetailerService1Code

class EventContext7(base_types._BaseFieldType):

	__slots__ = ["_CmpntId", "_SaleId", "_SvcTp"]
	@property
	def CmpntId(self):
		return self._CmpntId

	@CmpntId.setter
	def CmpntId(self, value):
		self._CmpntId = value if value is not None else base_types.UninitialisedField(self, 'CmpntId', PointOfInteractionComponent17, False)

	@CmpntId.deleter
	def CmpntId(self):
		del self._CmpntId
		self._CmpntId = base_types.UninitialisedField(self, 'CmpntId', PointOfInteractionComponent17, False)

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if value is not None else base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', RetailerService1Code, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', RetailerService1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpntId', type=PointOfInteractionComponent17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTp', type=RetailerService1Code, min=1, max=1, mutex_group=None, array=False),
	))