# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentType4Code
from . import ISODate
from . import Max140Text
from . import Max256Text
from . import Max35Text

class DocumentGeneralInformation1(base_types._BaseFieldType):

	__slots__ = ["_DocNb", "_DocTp", "_IsseDt", "_SndrRcvrSeqId", "_URL"]
	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if value is not None else base_types.UninitialisedField(self, 'DocTp', DocumentType4Code, False)

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = base_types.UninitialisedField(self, 'DocTp', DocumentType4Code, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def SndrRcvrSeqId(self):
		return self._SndrRcvrSeqId

	@SndrRcvrSeqId.setter
	def SndrRcvrSeqId(self, value):
		self._SndrRcvrSeqId = value if value is not None else base_types.UninitialisedField(self, 'SndrRcvrSeqId', Max140Text, False)

	@SndrRcvrSeqId.deleter
	def SndrRcvrSeqId(self):
		del self._SndrRcvrSeqId
		self._SndrRcvrSeqId = base_types.UninitialisedField(self, 'SndrRcvrSeqId', Max140Text, False)

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if value is not None else base_types.UninitialisedField(self, 'URL', Max256Text, False)

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = base_types.UninitialisedField(self, 'URL', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=DocumentType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrRcvrSeqId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))