from . import base_types
from .Referred1Code import Referred1Code
from .PartyIdentification125Choice import PartyIdentification125Choice

class ReferredAgent3(base_types._BaseFieldType):

	__slots__ = ["_Rfrd", "_RfrdPlcmntAgt"]
	@property
	def Rfrd(self):
		return self._Rfrd

	@Rfrd.setter
	def Rfrd(self, value):
		self._Rfrd = value if type(value) != base_types.auto else self.make_default("Rfrd")

	@Rfrd.deleter
	def Rfrd(self):
		del self._Rfrd
		self._Rfrd = None

	@property
	def RfrdPlcmntAgt(self):
		return self._RfrdPlcmntAgt

	@RfrdPlcmntAgt.setter
	def RfrdPlcmntAgt(self, value):
		self._RfrdPlcmntAgt = value if type(value) != base_types.auto else self.make_default("RfrdPlcmntAgt")

	@RfrdPlcmntAgt.deleter
	def RfrdPlcmntAgt(self):
		del self._RfrdPlcmntAgt
		self._RfrdPlcmntAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rfrd', type=Referred1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdPlcmntAgt', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
	))

