from . import base_types
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._UpdateLogPartyRecord2Choice import UpdateLogPartyRecord2Choice
from ._ISODateTime import ISODateTime

class PartyReferenceDataChange3(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_PtyId", "_OprTmStmp"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != base_types.auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if type(value) != base_types.auto else self.make_default("OprTmStmp")

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=UpdateLogPartyRecord2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

