from . import base_types
from .ReconciliationMatchedStatus9Choice import ReconciliationMatchedStatus9Choice
from .NoReasonCode import NoReasonCode

class ReconciliationStatus8Choice(base_types._BaseFieldType):

	__slots__ = ["_RptgData", "_NoRcncltnReqrd"]
	@property
	def RptgData(self):
		return self._RptgData

	@RptgData.setter
	def RptgData(self, value):
		self._RptgData = value if type(value) != base_types.auto else self.make_default("RptgData")

	@RptgData.deleter
	def RptgData(self):
		del self._RptgData
		self._RptgData = None

	@property
	def NoRcncltnReqrd(self):
		return self._NoRcncltnReqrd

	@NoRcncltnReqrd.setter
	def NoRcncltnReqrd(self, value):
		self._NoRcncltnReqrd = value if type(value) != base_types.auto else self.make_default("NoRcncltnReqrd")

	@NoRcncltnReqrd.deleter
	def NoRcncltnReqrd(self):
		del self._NoRcncltnReqrd
		self._NoRcncltnReqrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgData', type=ReconciliationMatchedStatus9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoRcncltnReqrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

