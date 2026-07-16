# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class IdentificationReference8Choice(base_types._BaseFieldType):

	__slots__ = ["_AllcnId", "_BlckId", "_ClntOrdrLkId", "_CmonId", "_CmplcId", "_CollTxId", "_ExctgPtyTxId", "_IndvAllcnId", "_IndxId", "_InstgPtyTxId", "_MktInfrstrctrTxId", "_PoolId", "_ScndryAllcnId"]
	@property
	def AllcnId(self):
		return self._AllcnId

	@AllcnId.setter
	def AllcnId(self, value):
		self._AllcnId = value if value is not None else base_types.UninitialisedField(self, 'AllcnId', Max35Text, False)

	@AllcnId.deleter
	def AllcnId(self):
		del self._AllcnId
		self._AllcnId = base_types.UninitialisedField(self, 'AllcnId', Max35Text, False)

	@property
	def BlckId(self):
		return self._BlckId

	@BlckId.setter
	def BlckId(self, value):
		self._BlckId = value if value is not None else base_types.UninitialisedField(self, 'BlckId', Max35Text, False)

	@BlckId.deleter
	def BlckId(self):
		del self._BlckId
		self._BlckId = base_types.UninitialisedField(self, 'BlckId', Max35Text, False)

	@property
	def ClntOrdrLkId(self):
		return self._ClntOrdrLkId

	@ClntOrdrLkId.setter
	def ClntOrdrLkId(self, value):
		self._ClntOrdrLkId = value if value is not None else base_types.UninitialisedField(self, 'ClntOrdrLkId', Max35Text, False)

	@ClntOrdrLkId.deleter
	def ClntOrdrLkId(self):
		del self._ClntOrdrLkId
		self._ClntOrdrLkId = base_types.UninitialisedField(self, 'ClntOrdrLkId', Max35Text, False)

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@property
	def CmplcId(self):
		return self._CmplcId

	@CmplcId.setter
	def CmplcId(self, value):
		self._CmplcId = value if value is not None else base_types.UninitialisedField(self, 'CmplcId', Max35Text, False)

	@CmplcId.deleter
	def CmplcId(self):
		del self._CmplcId
		self._CmplcId = base_types.UninitialisedField(self, 'CmplcId', Max35Text, False)

	@property
	def CollTxId(self):
		return self._CollTxId

	@CollTxId.setter
	def CollTxId(self, value):
		self._CollTxId = value if value is not None else base_types.UninitialisedField(self, 'CollTxId', Max35Text, False)

	@CollTxId.deleter
	def CollTxId(self):
		del self._CollTxId
		self._CollTxId = base_types.UninitialisedField(self, 'CollTxId', Max35Text, False)

	@property
	def ExctgPtyTxId(self):
		return self._ExctgPtyTxId

	@ExctgPtyTxId.setter
	def ExctgPtyTxId(self, value):
		self._ExctgPtyTxId = value if value is not None else base_types.UninitialisedField(self, 'ExctgPtyTxId', Max35Text, False)

	@ExctgPtyTxId.deleter
	def ExctgPtyTxId(self):
		del self._ExctgPtyTxId
		self._ExctgPtyTxId = base_types.UninitialisedField(self, 'ExctgPtyTxId', Max35Text, False)

	@property
	def IndvAllcnId(self):
		return self._IndvAllcnId

	@IndvAllcnId.setter
	def IndvAllcnId(self, value):
		self._IndvAllcnId = value if value is not None else base_types.UninitialisedField(self, 'IndvAllcnId', Max35Text, False)

	@IndvAllcnId.deleter
	def IndvAllcnId(self):
		del self._IndvAllcnId
		self._IndvAllcnId = base_types.UninitialisedField(self, 'IndvAllcnId', Max35Text, False)

	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if value is not None else base_types.UninitialisedField(self, 'IndxId', Max35Text, False)

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = base_types.UninitialisedField(self, 'IndxId', Max35Text, False)

	@property
	def InstgPtyTxId(self):
		return self._InstgPtyTxId

	@InstgPtyTxId.setter
	def InstgPtyTxId(self, value):
		self._InstgPtyTxId = value if value is not None else base_types.UninitialisedField(self, 'InstgPtyTxId', Max35Text, False)

	@InstgPtyTxId.deleter
	def InstgPtyTxId(self):
		del self._InstgPtyTxId
		self._InstgPtyTxId = base_types.UninitialisedField(self, 'InstgPtyTxId', Max35Text, False)

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
	def ScndryAllcnId(self):
		return self._ScndryAllcnId

	@ScndryAllcnId.setter
	def ScndryAllcnId(self, value):
		self._ScndryAllcnId = value if value is not None else base_types.UninitialisedField(self, 'ScndryAllcnId', Max35Text, False)

	@ScndryAllcnId.deleter
	def ScndryAllcnId(self):
		del self._ScndryAllcnId
		self._ScndryAllcnId = base_types.UninitialisedField(self, 'ScndryAllcnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BlckId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntOrdrLkId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmplcId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ExctgPtyTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvAllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstgPtyTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ScndryAllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))