from . import base_types
from .OriginalBusinessInstruction1 import OriginalBusinessInstruction1
from .SupplementaryData1 import SupplementaryData1
from .OriginalEnrolment3Choice import OriginalEnrolment3Choice
from .CreditorEnrolmentCancellationReason3 import CreditorEnrolmentCancellationReason3

class CreditorEnrolmentCancellation3(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_OrgnlBizInstr", "_OrgnlEnrlmnt", "_CxlRsn"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def OrgnlBizInstr(self):
		return self._OrgnlBizInstr

	@OrgnlBizInstr.setter
	def OrgnlBizInstr(self, value):
		self._OrgnlBizInstr = value if type(value) != auto else self.make_default("OrgnlBizInstr")

	@OrgnlBizInstr.deleter
	def OrgnlBizInstr(self):
		del self._OrgnlBizInstr
		self._OrgnlBizInstr = None

	@property
	def OrgnlEnrlmnt(self):
		return self._OrgnlEnrlmnt

	@OrgnlEnrlmnt.setter
	def OrgnlEnrlmnt(self, value):
		self._OrgnlEnrlmnt = value if type(value) != auto else self.make_default("OrgnlEnrlmnt")

	@OrgnlEnrlmnt.deleter
	def OrgnlEnrlmnt(self):
		del self._OrgnlEnrlmnt
		self._OrgnlEnrlmnt = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlBizInstr', type=OriginalBusinessInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmnt', type=OriginalEnrolment3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CreditorEnrolmentCancellationReason3, min=0, max=1, mutex_group=None, array=False),
	))

