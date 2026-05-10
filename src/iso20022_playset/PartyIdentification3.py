from . import base_types
from .AnyBICIdentifier import AnyBICIdentifier

class PartyIdentification3(base_types._BaseFieldType):

	__slots__ = ["_BICOrBEI"]
	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if type(value) != auto else self.make_default("BICOrBEI")

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

