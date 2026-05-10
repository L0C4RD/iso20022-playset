from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._Notification1 import Notification1
from ._SimpleIdentificationInformation import SimpleIdentificationInformation

class SpecialRequestV01(base_types._BaseFieldType):

	__slots__ = ["_Ntfctn", "_ReqId", "_SubmitrTxRef", "_TxId"]
	@property
	def Ntfctn(self):
		return self._Ntfctn

	@Ntfctn.setter
	def Ntfctn(self, value):
		self._Ntfctn = value if type(value) != base_types.auto else self.make_default("Ntfctn")

	@Ntfctn.deleter
	def Ntfctn(self):
		del self._Ntfctn
		self._Ntfctn = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != base_types.auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != base_types.auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ntfctn', type=Notification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))

