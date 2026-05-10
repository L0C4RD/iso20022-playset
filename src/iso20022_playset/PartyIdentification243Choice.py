from . import base_types
import GenericIdentification30
import AnyBICDec2014Identifier

class PartyIdentification243Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryId", "_BIC"]
	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
	))

