from . import base_types
import RestrictedFINXMax16Text

class References58Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrTxId", "_SctiesSttlmTxId", "_IntraPosMvmntId", "_AcctSvcrTxId", "_PoolId"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraPosMvmntId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))

