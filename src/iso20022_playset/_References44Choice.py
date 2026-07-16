# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericDocumentIdentification4
from . import Max35Text
from . import SettlementTypeAndIdentification18

class References44Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmntId", "_OthrTxId", "_SctiesFincgTxId", "_SctiesSttlmTxId"]
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
	def OthrTxId(self):
		return self._OthrTxId

	@OthrTxId.setter
	def OthrTxId(self, value):
		self._OthrTxId = value if value is not None else base_types.UninitialisedField(self, 'OthrTxId', GenericDocumentIdentification4, False)

	@OthrTxId.deleter
	def OthrTxId(self):
		del self._OthrTxId
		self._OthrTxId = base_types.UninitialisedField(self, 'OthrTxId', GenericDocumentIdentification4, False)

	@property
	def SctiesFincgTxId(self):
		return self._SctiesFincgTxId

	@SctiesFincgTxId.setter
	def SctiesFincgTxId(self, value):
		self._SctiesFincgTxId = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTxId', SettlementTypeAndIdentification18, False)

	@SctiesFincgTxId.deleter
	def SctiesFincgTxId(self):
		del self._SctiesFincgTxId
		self._SctiesFincgTxId = base_types.UninitialisedField(self, 'SctiesFincgTxId', SettlementTypeAndIdentification18, False)

	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmTxId', SettlementTypeAndIdentification18, False)

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = base_types.UninitialisedField(self, 'SctiesSttlmTxId', SettlementTypeAndIdentification18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmntId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrTxId', type=GenericDocumentIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgTxId', type=SettlementTypeAndIdentification18, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=SettlementTypeAndIdentification18, min=0, max=1, mutex_group=1, array=False),
	))