from . import base_types
from .GenericIdentification1 import GenericIdentification1
from .BICFIIdentifier import BICFIIdentifier
from .NameAndAddress5 import NameAndAddress5

class PartyIdentification62(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_PrtryId", "_NmAndAdr"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != base_types.auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

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
		base_types.FieldEntry(name='BICFI', type=BICFIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
	))

