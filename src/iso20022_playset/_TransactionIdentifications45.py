# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max52Text

class TransactionIdentifications45(base_types._BaseFieldType):

	__slots__ = ["_ClntCollInstrId", "_ClntCollTxId", "_CmonTxId", "_TrptyAgtSvcPrvdrCollInstrId", "_TrptyAgtSvcPrvdrCollTxId"]
	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if value is not None else base_types.UninitialisedField(self, 'ClntCollInstrId', Max35Text, False)

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = base_types.UninitialisedField(self, 'ClntCollInstrId', Max35Text, False)

	@property
	def ClntCollTxId(self):
		return self._ClntCollTxId

	@ClntCollTxId.setter
	def ClntCollTxId(self, value):
		self._ClntCollTxId = value if value is not None else base_types.UninitialisedField(self, 'ClntCollTxId', Max35Text, False)

	@ClntCollTxId.deleter
	def ClntCollTxId(self):
		del self._ClntCollTxId
		self._ClntCollTxId = base_types.UninitialisedField(self, 'ClntCollTxId', Max35Text, False)

	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if value is not None else base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollInstrId', Max35Text, False)

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollInstrId', Max35Text, False)

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))