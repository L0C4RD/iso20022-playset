import base_types
import MessageIdentification1
import ActivityReportItems3

class ActivityReportV04(base_types._BaseFieldType):

	__slots__ = ["_RltdMsgRef", "_Rpt", "_RptId"]
	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if type(value) != auto else self.make_default("RltdMsgRef")

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = None

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=ActivityReportItems3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

