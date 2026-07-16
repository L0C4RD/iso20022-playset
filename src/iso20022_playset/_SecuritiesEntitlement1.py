# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityIdentification7
from . import UnitOrFaceAmount1Choice

class SecuritiesEntitlement1(base_types._BaseFieldType):

	__slots__ = ["_EntitldSctiesQty", "_SctyId"]
	@property
	def EntitldSctiesQty(self):
		return self._EntitldSctiesQty

	@EntitldSctiesQty.setter
	def EntitldSctiesQty(self, value):
		self._EntitldSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'EntitldSctiesQty', UnitOrFaceAmount1Choice, False)

	@EntitldSctiesQty.deleter
	def EntitldSctiesQty(self):
		del self._EntitldSctiesQty
		self._EntitldSctiesQty = base_types.UninitialisedField(self, 'EntitldSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EntitldSctiesQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))