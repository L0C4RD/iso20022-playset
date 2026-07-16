# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActivityReportItems3
from . import MessageIdentification1

class ActivityReportV04(base_types._BaseFieldType):

	__slots__ = ["_RltdMsgRef", "_Rpt", "_RptId"]
	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if value is not None else base_types.UninitialisedField(self, 'RltdMsgRef', MessageIdentification1, False)

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = base_types.UninitialisedField(self, 'RltdMsgRef', MessageIdentification1, False)

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if value is not None else base_types.UninitialisedField(self, 'Rpt', ActivityReportItems3, True)

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = base_types.UninitialisedField(self, 'Rpt', ActivityReportItems3, True)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=ActivityReportItems3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))