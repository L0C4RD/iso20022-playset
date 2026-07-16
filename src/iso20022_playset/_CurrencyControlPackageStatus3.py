# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlRecordStatus3
from . import ISODateTime
from . import Max35Text
from . import StatisticalReportingStatus1Code
from . import ValidationStatusReason3

class CurrencyControlPackageStatus3(base_types._BaseFieldType):

	__slots__ = ["_PackgId", "_RcrdSts", "_Sts", "_StsDtTm", "_StsRsn"]
	@property
	def PackgId(self):
		return self._PackgId

	@PackgId.setter
	def PackgId(self, value):
		self._PackgId = value if value is not None else base_types.UninitialisedField(self, 'PackgId', Max35Text, False)

	@PackgId.deleter
	def PackgId(self):
		del self._PackgId
		self._PackgId = base_types.UninitialisedField(self, 'PackgId', Max35Text, False)

	@property
	def RcrdSts(self):
		return self._RcrdSts

	@RcrdSts.setter
	def RcrdSts(self, value):
		self._RcrdSts = value if value is not None else base_types.UninitialisedField(self, 'RcrdSts', CurrencyControlRecordStatus3, True)

	@RcrdSts.deleter
	def RcrdSts(self):
		del self._RcrdSts
		self._RcrdSts = base_types.UninitialisedField(self, 'RcrdSts', CurrencyControlRecordStatus3, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', StatisticalReportingStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', StatisticalReportingStatus1Code, False)

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if value is not None else base_types.UninitialisedField(self, 'StsDtTm', ISODateTime, False)

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = base_types.UninitialisedField(self, 'StsDtTm', ISODateTime, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', ValidationStatusReason3, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', ValidationStatusReason3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PackgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdSts', type=CurrencyControlRecordStatus3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=StatisticalReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=ValidationStatusReason3, min=0, max=None, mutex_group=None, array=True),
	))