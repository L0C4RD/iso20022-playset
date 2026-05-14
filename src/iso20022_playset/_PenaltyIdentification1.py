from . import base_types
from ._Max35Text import Max35Text
from ._PenaltyIdentification2 import PenaltyIdentification2

class PenaltyIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_MktInfrstrctrId", "_RallcnId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def MktInfrstrctrId(self):
		return self._MktInfrstrctrId

	@MktInfrstrctrId.setter
	def MktInfrstrctrId(self, value):
		self._MktInfrstrctrId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrId")

	@MktInfrstrctrId.deleter
	def MktInfrstrctrId(self):
		del self._MktInfrstrctrId
		self._MktInfrstrctrId = None

	@property
	def RallcnId(self):
		return self._RallcnId

	@RallcnId.setter
	def RallcnId(self, value):
		self._RallcnId = value if type(value) != base_types.auto else self.make_default("RallcnId")

	@RallcnId.deleter
	def RallcnId(self):
		del self._RallcnId
		self._RallcnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RallcnId', type=PenaltyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))

