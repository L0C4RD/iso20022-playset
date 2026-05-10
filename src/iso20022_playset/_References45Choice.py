from . import base_types
from ._GenericDocumentIdentification4 import GenericDocumentIdentification4
from ._SettlementTypeAndIdentification18 import SettlementTypeAndIdentification18
from ._Max35Text import Max35Text

class References45Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesFincgTxId", "_OthrTxId", "_SctiesSttlmTxId", "_IntraPosMvmntId"]
	@property
	def IntraPosMvmntId(self):
		return self._IntraPosMvmntId

	@IntraPosMvmntId.setter
	def IntraPosMvmntId(self, value):
		self._IntraPosMvmntId = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntId")

	@IntraPosMvmntId.deleter
	def IntraPosMvmntId(self):
		del self._IntraPosMvmntId
		self._IntraPosMvmntId = None

	@property
	def OthrTxId(self):
		return self._OthrTxId

	@OthrTxId.setter
	def OthrTxId(self, value):
		self._OthrTxId = value if type(value) != base_types.auto else self.make_default("OthrTxId")

	@OthrTxId.deleter
	def OthrTxId(self):
		del self._OthrTxId
		self._OthrTxId = None

	@property
	def SctiesFincgTxId(self):
		return self._SctiesFincgTxId

	@SctiesFincgTxId.setter
	def SctiesFincgTxId(self, value):
		self._SctiesFincgTxId = value if type(value) != base_types.auto else self.make_default("SctiesFincgTxId")

	@SctiesFincgTxId.deleter
	def SctiesFincgTxId(self):
		del self._SctiesFincgTxId
		self._SctiesFincgTxId = None

	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxId")

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrTxId', type=GenericDocumentIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgTxId', type=SettlementTypeAndIdentification18, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=SettlementTypeAndIdentification18, min=0, max=1, mutex_group=1, array=False),
	))

