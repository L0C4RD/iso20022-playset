from . import base_types
from .Max35Text import Max35Text
from .ExternalDocumentType1Code import ExternalDocumentType1Code
from .Max140Text import Max140Text
from .BinaryFile1 import BinaryFile1
from .Max256Text import Max256Text
from .ISODate import ISODate
from .SignatureEnvelopeReference import SignatureEnvelopeReference

class DocumentGeneralInformation5(base_types._BaseFieldType):

	__slots__ = ["_IsseDt", "_SndrRcvrSeqId", "_LkFileHash", "_AttchdBinryFile", "_DocNm", "_URL", "_DocNb", "_DocTp"]
	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def SndrRcvrSeqId(self):
		return self._SndrRcvrSeqId

	@SndrRcvrSeqId.setter
	def SndrRcvrSeqId(self, value):
		self._SndrRcvrSeqId = value if type(value) != auto else self.make_default("SndrRcvrSeqId")

	@SndrRcvrSeqId.deleter
	def SndrRcvrSeqId(self):
		del self._SndrRcvrSeqId
		self._SndrRcvrSeqId = None

	@property
	def LkFileHash(self):
		return self._LkFileHash

	@LkFileHash.setter
	def LkFileHash(self, value):
		self._LkFileHash = value if type(value) != auto else self.make_default("LkFileHash")

	@LkFileHash.deleter
	def LkFileHash(self):
		del self._LkFileHash
		self._LkFileHash = None

	@property
	def AttchdBinryFile(self):
		return self._AttchdBinryFile

	@AttchdBinryFile.setter
	def AttchdBinryFile(self, value):
		self._AttchdBinryFile = value if type(value) != auto else self.make_default("AttchdBinryFile")

	@AttchdBinryFile.deleter
	def AttchdBinryFile(self):
		del self._AttchdBinryFile
		self._AttchdBinryFile = None

	@property
	def DocNm(self):
		return self._DocNm

	@DocNm.setter
	def DocNm(self, value):
		self._DocNm = value if type(value) != auto else self.make_default("DocNm")

	@DocNm.deleter
	def DocNm(self):
		del self._DocNm
		self._DocNm = None

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if type(value) != auto else self.make_default("URL")

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrRcvrSeqId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkFileHash', type=SignatureEnvelopeReference, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttchdBinryFile', type=BinaryFile1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=ExternalDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
	))

