# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._Max52Text import Max52Text

class TransactionIdentifications44(base_types._BaseFieldType):

	__slots__ = ["_ClntCollInstrId", "_ClntCollTxId", "_CmonTxId", "_CtrPtyCollInstrId", "_CtrPtyCollTxId", "_TrptyAgtSvcPrvdrCollInstrId", "_TrptyAgtSvcPrvdrCollTxId"]
	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if type(value) != base_types.auto else self.make_default("ClntCollInstrId")

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = None

	@property
	def ClntCollTxId(self):
		return self._ClntCollTxId

	@ClntCollTxId.setter
	def ClntCollTxId(self, value):
		self._ClntCollTxId = value if type(value) != base_types.auto else self.make_default("ClntCollTxId")

	@ClntCollTxId.deleter
	def ClntCollTxId(self):
		del self._ClntCollTxId
		self._ClntCollTxId = None

	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if type(value) != base_types.auto else self.make_default("CmonTxId")

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = None

	@property
	def CtrPtyCollInstrId(self):
		return self._CtrPtyCollInstrId

	@CtrPtyCollInstrId.setter
	def CtrPtyCollInstrId(self, value):
		self._CtrPtyCollInstrId = value if type(value) != base_types.auto else self.make_default("CtrPtyCollInstrId")

	@CtrPtyCollInstrId.deleter
	def CtrPtyCollInstrId(self):
		del self._CtrPtyCollInstrId
		self._CtrPtyCollInstrId = None

	@property
	def CtrPtyCollTxId(self):
		return self._CtrPtyCollTxId

	@CtrPtyCollTxId.setter
	def CtrPtyCollTxId(self, value):
		self._CtrPtyCollTxId = value if type(value) != base_types.auto else self.make_default("CtrPtyCollTxId")

	@CtrPtyCollTxId.deleter
	def CtrPtyCollTxId(self):
		del self._CtrPtyCollTxId
		self._CtrPtyCollTxId = None

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollInstrId")

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = None

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))