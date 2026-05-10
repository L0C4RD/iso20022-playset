from . import base_types
from ._AlternatePartyIdentification7 import AlternatePartyIdentification7
from ._GenericIdentification36 import GenericIdentification36
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._NameAndAddress5 import NameAndAddress5

class PartyIdentification229Choice(base_types._BaseFieldType):

	__slots__ = ["_NmAndAdr", "_IndvOwnrId", "_PrtryId", "_AnyBIC"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def IndvOwnrId(self):
		return self._IndvOwnrId

	@IndvOwnrId.setter
	def IndvOwnrId(self, value):
		self._IndvOwnrId = value if type(value) != base_types.auto else self.make_default("IndvOwnrId")

	@IndvOwnrId.deleter
	def IndvOwnrId(self):
		del self._IndvOwnrId
		self._IndvOwnrId = None

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
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvOwnrId', type=AlternatePartyIdentification7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))

