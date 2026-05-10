from . import base_types
from .ServiceStatus1Choice import ServiceStatus1Choice
from .CreditorEnrolmentStatusReason3 import CreditorEnrolmentStatusReason3
from .OriginalBusinessInstruction1 import OriginalBusinessInstruction1
from .SupplementaryData1 import SupplementaryData1
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .OriginalEnrolment3Choice import OriginalEnrolment3Choice

class EnrolmentStatus3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlBizInstr", "_SplmtryData", "_FctvEnrlmntDt", "_Sts", "_StsRsn", "_OrgnlEnrlmntRef"]
	@property
	def OrgnlBizInstr(self):
		return self._OrgnlBizInstr

	@OrgnlBizInstr.setter
	def OrgnlBizInstr(self, value):
		self._OrgnlBizInstr = value if type(value) != base_types.auto else self.make_default("OrgnlBizInstr")

	@OrgnlBizInstr.deleter
	def OrgnlBizInstr(self):
		del self._OrgnlBizInstr
		self._OrgnlBizInstr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FctvEnrlmntDt(self):
		return self._FctvEnrlmntDt

	@FctvEnrlmntDt.setter
	def FctvEnrlmntDt(self, value):
		self._FctvEnrlmntDt = value if type(value) != base_types.auto else self.make_default("FctvEnrlmntDt")

	@FctvEnrlmntDt.deleter
	def FctvEnrlmntDt(self):
		del self._FctvEnrlmntDt
		self._FctvEnrlmntDt = None

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
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def OrgnlEnrlmntRef(self):
		return self._OrgnlEnrlmntRef

	@OrgnlEnrlmntRef.setter
	def OrgnlEnrlmntRef(self, value):
		self._OrgnlEnrlmntRef = value if type(value) != base_types.auto else self.make_default("OrgnlEnrlmntRef")

	@OrgnlEnrlmntRef.deleter
	def OrgnlEnrlmntRef(self):
		del self._OrgnlEnrlmntRef
		self._OrgnlEnrlmntRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FctvEnrlmntDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ServiceStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=CreditorEnrolmentStatusReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmntRef', type=OriginalEnrolment3Choice, min=0, max=1, mutex_group=None, array=False),
	))

