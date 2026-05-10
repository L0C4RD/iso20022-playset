import base_types
import RestrictedFINXMax16Text

class References78Choice(base_types._BaseFieldType):

	__slots__ = ["_MktInfrstrctrTxId", "_OthrTxId", "_AcctSvcrTxId", "_PoolId", "_CtrPtyMktInfrstrctrTxId", "_SctiesSttlmTxId", "_IntraPosMvmntId", "_IntraBalMvmntId"]
	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	@property
	def OthrTxId(self):
		return self._OthrTxId

	@OthrTxId.setter
	def OthrTxId(self, value):
		self._OthrTxId = value if type(value) != auto else self.make_default("OthrTxId")

	@OthrTxId.deleter
	def OthrTxId(self):
		del self._OthrTxId
		self._OthrTxId = None

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if type(value) != auto else self.make_default("AcctSvcrTxId")

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = None

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if type(value) != auto else self.make_default("PoolId")

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = None

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if type(value) != auto else self.make_default("CtrPtyMktInfrstrctrTxId")

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = None

	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if type(value) != auto else self.make_default("SctiesSttlmTxId")

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = None

	@property
	def IntraPosMvmntId(self):
		return self._IntraPosMvmntId

	@IntraPosMvmntId.setter
	def IntraPosMvmntId(self, value):
		self._IntraPosMvmntId = value if type(value) != auto else self.make_default("IntraPosMvmntId")

	@IntraPosMvmntId.deleter
	def IntraPosMvmntId(self):
		del self._IntraPosMvmntId
		self._IntraPosMvmntId = None

	@property
	def IntraBalMvmntId(self):
		return self._IntraBalMvmntId

	@IntraBalMvmntId.setter
	def IntraBalMvmntId(self, value):
		self._IntraBalMvmntId = value if type(value) != auto else self.make_default("IntraBalMvmntId")

	@IntraBalMvmntId.deleter
	def IntraBalMvmntId(self):
		del self._IntraBalMvmntId
		self._IntraBalMvmntId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraPosMvmntId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraBalMvmntId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))

