from . import base_types
from .Max35Text import Max35Text
from .NameAndAddress8 import NameAndAddress8
from .LEIIdentifier import LEIIdentifier

class PartyIdentification60(base_types._BaseFieldType):

	__slots__ = ["_FndId", "_NmAndAdr", "_LglNttyIdr"]
	@property
	def FndId(self):
		return self._FndId

	@FndId.setter
	def FndId(self, value):
		self._FndId = value if type(value) != base_types.auto else self.make_default("FndId")

	@FndId.deleter
	def FndId(self):
		del self._FndId
		self._FndId = None

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

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if type(value) != base_types.auto else self.make_default("LglNttyIdr")

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

