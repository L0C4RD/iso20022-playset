from . import base_types
from ._StatisticalReportingStatus1Code import StatisticalReportingStatus1Code
from ._ValidationStatusReason3 import ValidationStatusReason3
from ._DocumentIdentification28 import DocumentIdentification28
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime

class CurrencyControlRecordStatus3(base_types._BaseFieldType):

	__slots__ = ["_RcrdId", "_DocId", "_StsRsn", "_StsDtTm", "_Sts"]
	@property
	def DocId(self):
		return self._DocId

	@DocId.setter
	def DocId(self, value):
		self._DocId = value if type(value) != base_types.auto else self.make_default("DocId")

	@DocId.deleter
	def DocId(self):
		del self._DocId
		self._DocId = None

	@property
	def RcrdId(self):
		return self._RcrdId

	@RcrdId.setter
	def RcrdId(self, value):
		self._RcrdId = value if type(value) != base_types.auto else self.make_default("RcrdId")

	@RcrdId.deleter
	def RcrdId(self):
		del self._RcrdId
		self._RcrdId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if type(value) != base_types.auto else self.make_default("StsDtTm")

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocId', type=DocumentIdentification28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=StatisticalReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=ValidationStatusReason3, min=0, max=None, mutex_group=None, array=True),
	))

