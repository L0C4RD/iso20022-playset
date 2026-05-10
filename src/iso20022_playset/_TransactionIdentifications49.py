from . import base_types
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text

class TransactionIdentifications49(base_types._BaseFieldType):

	__slots__ = ["_CmonId", "_AcctSvcrTxId", "_AcctOwnrTxId", "_PrcrTxId", "_MktInfrstrctrTxId", "_CtrPtyMktInfrstrctrTxId", "_NetgSvcPrvdrId"]
	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if type(value) != base_types.auto else self.make_default("CmonId")

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = None

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if type(value) != base_types.auto else self.make_default("AcctSvcrTxId")

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = None

	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if type(value) != base_types.auto else self.make_default("AcctOwnrTxId")

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != base_types.auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

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

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if type(value) != base_types.auto else self.make_default("CtrPtyMktInfrstrctrTxId")

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = None

	@property
	def NetgSvcPrvdrId(self):
		return self._NetgSvcPrvdrId

	@NetgSvcPrvdrId.setter
	def NetgSvcPrvdrId(self, value):
		self._NetgSvcPrvdrId = value if type(value) != base_types.auto else self.make_default("NetgSvcPrvdrId")

	@NetgSvcPrvdrId.deleter
	def NetgSvcPrvdrId(self):
		del self._NetgSvcPrvdrId
		self._NetgSvcPrvdrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrTxId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetgSvcPrvdrId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))

