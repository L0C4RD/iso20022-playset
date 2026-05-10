import base_types
import Max35Text
import UTIIdentifier

class References80Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmntId", "_CmonId", "_IntraBalMvmntId", "_AcctSvcrTxId", "_PoolId", "_TradId", "_SctiesSttlmTxId", "_UnqTxIdr", "_OthrTxId", "_CtrPtyMktInfrstrctrTxId", "_MktInfrstrctrTxId"]
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
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if type(value) != auto else self.make_default("CmonId")

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = None

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
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

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
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

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
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraBalMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

