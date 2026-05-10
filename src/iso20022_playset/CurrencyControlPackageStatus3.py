import base_types
import ISODateTime
import ValidationStatusReason3
import StatisticalReportingStatus1Code
import CurrencyControlRecordStatus3
import Max35Text

class CurrencyControlPackageStatus3(base_types._BaseFieldType):

	__slots__ = ["_RcrdSts", "_StsRsn", "_Sts", "_StsDtTm", "_PackgId"]
	@property
	def RcrdSts(self):
		return self._RcrdSts

	@RcrdSts.setter
	def RcrdSts(self, value):
		self._RcrdSts = value if type(value) != auto else self.make_default("RcrdSts")

	@RcrdSts.deleter
	def RcrdSts(self):
		del self._RcrdSts
		self._RcrdSts = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if type(value) != auto else self.make_default("StsDtTm")

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = None

	@property
	def PackgId(self):
		return self._PackgId

	@PackgId.setter
	def PackgId(self, value):
		self._PackgId = value if type(value) != auto else self.make_default("PackgId")

	@PackgId.deleter
	def PackgId(self):
		del self._PackgId
		self._PackgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcrdSts', type=CurrencyControlRecordStatus3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsRsn', type=ValidationStatusReason3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=StatisticalReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

