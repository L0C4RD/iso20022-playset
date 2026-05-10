from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._TransactionReportItems3 import TransactionReportItems3

class TransactionReportV03(base_types._BaseFieldType):

	__slots__ = ["_RltdMsgRef", "_RptId", "_RptdItms"]
	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if type(value) != base_types.auto else self.make_default("RltdMsgRef")

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def RptdItms(self):
		return self._RptdItms

	@RptdItms.setter
	def RptdItms(self, value):
		self._RptdItms = value if type(value) != base_types.auto else self.make_default("RptdItms")

	@RptdItms.deleter
	def RptdItms(self):
		del self._RptdItms
		self._RptdItms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdItms', type=TransactionReportItems3, min=0, max=None, mutex_group=None, array=True),
	))

