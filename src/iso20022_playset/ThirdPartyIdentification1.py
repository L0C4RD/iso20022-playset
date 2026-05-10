import base_types
import PartyIdentification221
import PartyRole3Code

class ThirdPartyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_LglPrsnId", "_Role"]
	@property
	def LglPrsnId(self):
		return self._LglPrsnId

	@LglPrsnId.setter
	def LglPrsnId(self, value):
		self._LglPrsnId = value if type(value) != auto else self.make_default("LglPrsnId")

	@LglPrsnId.deleter
	def LglPrsnId(self):
		del self._LglPrsnId
		self._LglPrsnId = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglPrsnId', type=PartyIdentification221, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PartyRole3Code, min=1, max=1, mutex_group=None, array=False),
	))

