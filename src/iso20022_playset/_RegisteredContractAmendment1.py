# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification28
from . import ISODate
from . import Max1025Text
from . import Max35Text

class RegisteredContractAmendment1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AmdmntDt", "_AmdmntRsn", "_Doc", "_StartDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def AmdmntDt(self):
		return self._AmdmntDt

	@AmdmntDt.setter
	def AmdmntDt(self, value):
		self._AmdmntDt = value if value is not None else base_types.UninitialisedField(self, 'AmdmntDt', ISODate, False)

	@AmdmntDt.deleter
	def AmdmntDt(self):
		del self._AmdmntDt
		self._AmdmntDt = base_types.UninitialisedField(self, 'AmdmntDt', ISODate, False)

	@property
	def AmdmntRsn(self):
		return self._AmdmntRsn

	@AmdmntRsn.setter
	def AmdmntRsn(self, value):
		self._AmdmntRsn = value if value is not None else base_types.UninitialisedField(self, 'AmdmntRsn', Max35Text, False)

	@AmdmntRsn.deleter
	def AmdmntRsn(self):
		del self._AmdmntRsn
		self._AmdmntRsn = base_types.UninitialisedField(self, 'AmdmntRsn', Max35Text, False)

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if value is not None else base_types.UninitialisedField(self, 'Doc', DocumentIdentification28, False)

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = base_types.UninitialisedField(self, 'Doc', DocumentIdentification28, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Doc', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))