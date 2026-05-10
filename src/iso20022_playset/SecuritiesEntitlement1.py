import base_types
import SecurityIdentification7
import UnitOrFaceAmount1Choice

class SecuritiesEntitlement1(base_types._BaseFieldType):

	__slots__ = ["_SctyId", "_EntitldSctiesQty"]
	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def EntitldSctiesQty(self):
		return self._EntitldSctiesQty

	@EntitldSctiesQty.setter
	def EntitldSctiesQty(self, value):
		self._EntitldSctiesQty = value if type(value) != auto else self.make_default("EntitldSctiesQty")

	@EntitldSctiesQty.deleter
	def EntitldSctiesQty(self):
		del self._EntitldSctiesQty
		self._EntitldSctiesQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldSctiesQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
	))

