# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class References41Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrTxId", "_IntraBalMvmntId", "_IntraPosMvmntId", "_MktInfrstrctrTxId", "_OthrTxId", "_PoolId", "_SctiesSttlmTxId"]
	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@property
	def IntraBalMvmntId(self):
		return self._IntraBalMvmntId

	@IntraBalMvmntId.setter
	def IntraBalMvmntId(self, value):
		self._IntraBalMvmntId = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntId', Max35Text, False)

	@IntraBalMvmntId.deleter
	def IntraBalMvmntId(self):
		del self._IntraBalMvmntId
		self._IntraBalMvmntId = base_types.UninitialisedField(self, 'IntraBalMvmntId', Max35Text, False)

	@property
	def IntraPosMvmntId(self):
		return self._IntraPosMvmntId

	@IntraPosMvmntId.setter
	def IntraPosMvmntId(self, value):
		self._IntraPosMvmntId = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntId', Max35Text, False)

	@IntraPosMvmntId.deleter
	def IntraPosMvmntId(self):
		del self._IntraPosMvmntId
		self._IntraPosMvmntId = base_types.UninitialisedField(self, 'IntraPosMvmntId', Max35Text, False)

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@property
	def OthrTxId(self):
		return self._OthrTxId

	@OthrTxId.setter
	def OthrTxId(self, value):
		self._OthrTxId = value if value is not None else base_types.UninitialisedField(self, 'OthrTxId', Max35Text, False)

	@OthrTxId.deleter
	def OthrTxId(self):
		del self._OthrTxId
		self._OthrTxId = base_types.UninitialisedField(self, 'OthrTxId', Max35Text, False)

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if value is not None else base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxId', Max35Text, False)

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = base_types.UninitialisedField(self, 'SctiesSttlmTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraBalMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntraPosMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))