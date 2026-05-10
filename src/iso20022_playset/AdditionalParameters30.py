import base_types
import Max35Text
import PartialSettlement2Code
import PreConfirmation1Code

class AdditionalParameters30(base_types._BaseFieldType):

	__slots__ = ["_TrptyAgtSvcPrvdrCollTxId", "_PrtlSttlm", "_ClntTrptyCollTxId", "_PreConf"]
	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if type(value) != auto else self.make_default("PrtlSttlm")

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = None

	@property
	def ClntTrptyCollTxId(self):
		return self._ClntTrptyCollTxId

	@ClntTrptyCollTxId.setter
	def ClntTrptyCollTxId(self, value):
		self._ClntTrptyCollTxId = value if type(value) != auto else self.make_default("ClntTrptyCollTxId")

	@ClntTrptyCollTxId.deleter
	def ClntTrptyCollTxId(self):
		del self._ClntTrptyCollTxId
		self._ClntTrptyCollTxId = None

	@property
	def PreConf(self):
		return self._PreConf

	@PreConf.setter
	def PreConf(self, value):
		self._PreConf = value if type(value) != auto else self.make_default("PreConf")

	@PreConf.deleter
	def PreConf(self):
		del self._PreConf
		self._PreConf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlm', type=PartialSettlement2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreConf', type=PreConfirmation1Code, min=0, max=1, mutex_group=None, array=False),
	))

