from . import base_types
from .DocumentIdentification28 import DocumentIdentification28
from .Max35Text import Max35Text
from .Max1025Text import Max1025Text
from .ISODate import ISODate

class RegisteredContractAmendment1(base_types._BaseFieldType):

	__slots__ = ["_AmdmntDt", "_AmdmntRsn", "_Doc", "_AddtlInf", "_StartDt"]
	@property
	def AmdmntDt(self):
		return self._AmdmntDt

	@AmdmntDt.setter
	def AmdmntDt(self, value):
		self._AmdmntDt = value if type(value) != base_types.auto else self.make_default("AmdmntDt")

	@AmdmntDt.deleter
	def AmdmntDt(self):
		del self._AmdmntDt
		self._AmdmntDt = None

	@property
	def AmdmntRsn(self):
		return self._AmdmntRsn

	@AmdmntRsn.setter
	def AmdmntRsn(self, value):
		self._AmdmntRsn = value if type(value) != base_types.auto else self.make_default("AmdmntRsn")

	@AmdmntRsn.deleter
	def AmdmntRsn(self):
		del self._AmdmntRsn
		self._AmdmntRsn = None

	@property
	def Doc(self):
		return self._Doc

	@Doc.setter
	def Doc(self, value):
		self._Doc = value if type(value) != base_types.auto else self.make_default("Doc")

	@Doc.deleter
	def Doc(self):
		del self._Doc
		self._Doc = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Doc', type=DocumentIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

