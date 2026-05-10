from . import base_types
from .NameAndAddress5 import NameAndAddress5
from .AnyBICIdentifier import AnyBICIdentifier
from .GenericIdentification1 import GenericIdentification1

class PartyIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryId", "_BICOrBEI", "_NmAndAdr"]
	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if type(value) != base_types.auto else self.make_default("BICOrBEI")

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=1, array=False),
	))

