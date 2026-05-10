from . import base_types
from ._Max35Text import Max35Text

class TransactionIdentification15(base_types._BaseFieldType):

	__slots__ = ["_MktInfrstrctrTxId"]
	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

