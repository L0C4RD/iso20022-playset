from . import base_types
from ._CreditorEnrolmentAmendment6 import CreditorEnrolmentAmendment6
from ._CreditorEnrolmentAmendmentReason3 import CreditorEnrolmentAmendmentReason3
from ._OriginalBusinessInstruction1 import OriginalBusinessInstruction1
from ._OriginalEnrolment3Choice import OriginalEnrolment3Choice
from ._SupplementaryData1 import SupplementaryData1

class CreditorEnrolmentAmendment5(base_types._BaseFieldType):

	__slots__ = ["_Amdmnt", "_AmdmntRsn", "_OrgnlBizInstr", "_OrgnlEnrlmnt", "_SplmtryData"]
	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != base_types.auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

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
	def OrgnlEnrlmnt(self):
		return self._OrgnlEnrlmnt

	@OrgnlEnrlmnt.setter
	def OrgnlEnrlmnt(self, value):
		self._OrgnlEnrlmnt = value if type(value) != base_types.auto else self.make_default("OrgnlEnrlmnt")

	@OrgnlEnrlmnt.deleter
	def OrgnlEnrlmnt(self):
		del self._OrgnlEnrlmnt
		self._OrgnlEnrlmnt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amdmnt', type=CreditorEnrolmentAmendment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntRsn', type=CreditorEnrolmentAmendmentReason3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmnt', type=OriginalEnrolment3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

