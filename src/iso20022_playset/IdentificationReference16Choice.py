import base_types
import Max35Text
import UTIIdentifier

class IdentificationReference16Choice(base_types._BaseFieldType):

	__slots__ = ["_IndvAllcnId", "_CollTxId", "_UnqTxIdr", "_CmonId", "_CxlReqId", "_ScndryAllcnId", "_InstgPtyTxId", "_ClntOrdrLkId", "_CmplcId", "_IndxId", "_ExctgPtyTxId", "_MktInfrstrctrTxId", "_BlckId", "_AllcnId", "_PoolId"]
	@property
	def IndvAllcnId(self):
		return self._IndvAllcnId

	@IndvAllcnId.setter
	def IndvAllcnId(self, value):
		self._IndvAllcnId = value if type(value) != auto else self.make_default("IndvAllcnId")

	@IndvAllcnId.deleter
	def IndvAllcnId(self):
		del self._IndvAllcnId
		self._IndvAllcnId = None

	@property
	def CollTxId(self):
		return self._CollTxId

	@CollTxId.setter
	def CollTxId(self, value):
		self._CollTxId = value if type(value) != auto else self.make_default("CollTxId")

	@CollTxId.deleter
	def CollTxId(self):
		del self._CollTxId
		self._CollTxId = None

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
	def CxlReqId(self):
		return self._CxlReqId

	@CxlReqId.setter
	def CxlReqId(self, value):
		self._CxlReqId = value if type(value) != auto else self.make_default("CxlReqId")

	@CxlReqId.deleter
	def CxlReqId(self):
		del self._CxlReqId
		self._CxlReqId = None

	@property
	def ScndryAllcnId(self):
		return self._ScndryAllcnId

	@ScndryAllcnId.setter
	def ScndryAllcnId(self, value):
		self._ScndryAllcnId = value if type(value) != auto else self.make_default("ScndryAllcnId")

	@ScndryAllcnId.deleter
	def ScndryAllcnId(self):
		del self._ScndryAllcnId
		self._ScndryAllcnId = None

	@property
	def InstgPtyTxId(self):
		return self._InstgPtyTxId

	@InstgPtyTxId.setter
	def InstgPtyTxId(self, value):
		self._InstgPtyTxId = value if type(value) != auto else self.make_default("InstgPtyTxId")

	@InstgPtyTxId.deleter
	def InstgPtyTxId(self):
		del self._InstgPtyTxId
		self._InstgPtyTxId = None

	@property
	def ClntOrdrLkId(self):
		return self._ClntOrdrLkId

	@ClntOrdrLkId.setter
	def ClntOrdrLkId(self, value):
		self._ClntOrdrLkId = value if type(value) != auto else self.make_default("ClntOrdrLkId")

	@ClntOrdrLkId.deleter
	def ClntOrdrLkId(self):
		del self._ClntOrdrLkId
		self._ClntOrdrLkId = None

	@property
	def CmplcId(self):
		return self._CmplcId

	@CmplcId.setter
	def CmplcId(self, value):
		self._CmplcId = value if type(value) != auto else self.make_default("CmplcId")

	@CmplcId.deleter
	def CmplcId(self):
		del self._CmplcId
		self._CmplcId = None

	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if type(value) != auto else self.make_default("IndxId")

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = None

	@property
	def ExctgPtyTxId(self):
		return self._ExctgPtyTxId

	@ExctgPtyTxId.setter
	def ExctgPtyTxId(self, value):
		self._ExctgPtyTxId = value if type(value) != auto else self.make_default("ExctgPtyTxId")

	@ExctgPtyTxId.deleter
	def ExctgPtyTxId(self):
		del self._ExctgPtyTxId
		self._ExctgPtyTxId = None

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
	def BlckId(self):
		return self._BlckId

	@BlckId.setter
	def BlckId(self, value):
		self._BlckId = value if type(value) != auto else self.make_default("BlckId")

	@BlckId.deleter
	def BlckId(self):
		del self._BlckId
		self._BlckId = None

	@property
	def AllcnId(self):
		return self._AllcnId

	@AllcnId.setter
	def AllcnId(self, value):
		self._AllcnId = value if type(value) != auto else self.make_default("AllcnId")

	@AllcnId.deleter
	def AllcnId(self):
		del self._AllcnId
		self._AllcnId = None

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
		base_types.FieldEntry(name='IndvAllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ScndryAllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstgPtyTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntOrdrLkId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CmplcId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ExctgPtyTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BlckId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllcnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

