from . import base_types
from .DocumentType4Code import DocumentType4Code
from .Max140Text import Max140Text
from .Max256Text import Max256Text
from .ISODate import ISODate
from .Max35Text import Max35Text

class DocumentGeneralInformation1(base_types._BaseFieldType):

	__slots__ = ["_DocTp", "_IsseDt", "_DocNb", "_URL", "_SndrRcvrSeqId"]
	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != base_types.auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != base_types.auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if type(value) != base_types.auto else self.make_default("URL")

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = None

	@property
	def SndrRcvrSeqId(self):
		return self._SndrRcvrSeqId

	@SndrRcvrSeqId.setter
	def SndrRcvrSeqId(self, value):
		self._SndrRcvrSeqId = value if type(value) != base_types.auto else self.make_default("SndrRcvrSeqId")

	@SndrRcvrSeqId.deleter
	def SndrRcvrSeqId(self):
		del self._SndrRcvrSeqId
		self._SndrRcvrSeqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocTp', type=DocumentType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrRcvrSeqId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

