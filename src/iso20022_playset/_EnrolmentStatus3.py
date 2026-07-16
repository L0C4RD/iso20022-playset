# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorEnrolmentStatusReason3
from . import DateAndDateTime2Choice
from . import OriginalBusinessInstruction1
from . import OriginalEnrolment3Choice
from . import ServiceStatus1Choice
from . import SupplementaryData1

class EnrolmentStatus3(base_types._BaseFieldType):

	__slots__ = ["_FctvEnrlmntDt", "_OrgnlBizInstr", "_OrgnlEnrlmntRef", "_SplmtryData", "_Sts", "_StsRsn"]
	@property
	def FctvEnrlmntDt(self):
		return self._FctvEnrlmntDt

	@FctvEnrlmntDt.setter
	def FctvEnrlmntDt(self, value):
		self._FctvEnrlmntDt = value if value is not None else base_types.UninitialisedField(self, 'FctvEnrlmntDt', DateAndDateTime2Choice, False)

	@FctvEnrlmntDt.deleter
	def FctvEnrlmntDt(self):
		del self._FctvEnrlmntDt
		self._FctvEnrlmntDt = base_types.UninitialisedField(self, 'FctvEnrlmntDt', DateAndDateTime2Choice, False)

	@property
	def OrgnlBizInstr(self):
		return self._OrgnlBizInstr

	@OrgnlBizInstr.setter
	def OrgnlBizInstr(self, value):
		self._OrgnlBizInstr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBizInstr', OriginalBusinessInstruction1, False)

	@OrgnlBizInstr.deleter
	def OrgnlBizInstr(self):
		del self._OrgnlBizInstr
		self._OrgnlBizInstr = base_types.UninitialisedField(self, 'OrgnlBizInstr', OriginalBusinessInstruction1, False)

	@property
	def OrgnlEnrlmntRef(self):
		return self._OrgnlEnrlmntRef

	@OrgnlEnrlmntRef.setter
	def OrgnlEnrlmntRef(self, value):
		self._OrgnlEnrlmntRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEnrlmntRef', OriginalEnrolment3Choice, False)

	@OrgnlEnrlmntRef.deleter
	def OrgnlEnrlmntRef(self):
		del self._OrgnlEnrlmntRef
		self._OrgnlEnrlmntRef = base_types.UninitialisedField(self, 'OrgnlEnrlmntRef', OriginalEnrolment3Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ServiceStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ServiceStatus1Choice, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', CreditorEnrolmentStatusReason3, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', CreditorEnrolmentStatusReason3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvEnrlmntDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmntRef', type=OriginalEnrolment3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ServiceStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=CreditorEnrolmentStatusReason3, min=0, max=1, mutex_group=None, array=False),
	))