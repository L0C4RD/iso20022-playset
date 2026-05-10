from . import base_types
from ._DateTimePeriodDetails1 import DateTimePeriodDetails1
from ._MessageIdentification1 import MessageIdentification1
from ._BICIdentification1 import BICIdentification1

class ActivityReportRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_NttiesToBeRptd", "_RptPrd"]
	@property
	def NttiesToBeRptd(self):
		return self._NttiesToBeRptd

	@NttiesToBeRptd.setter
	def NttiesToBeRptd(self, value):
		self._NttiesToBeRptd = value if type(value) != base_types.auto else self.make_default("NttiesToBeRptd")

	@NttiesToBeRptd.deleter
	def NttiesToBeRptd(self):
		del self._NttiesToBeRptd
		self._NttiesToBeRptd = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != base_types.auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if type(value) != base_types.auto else self.make_default("RptPrd")

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NttiesToBeRptd', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=DateTimePeriodDetails1, min=1, max=1, mutex_group=None, array=False),
	))

