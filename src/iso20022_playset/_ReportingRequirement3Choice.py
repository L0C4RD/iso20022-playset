from . import base_types
from .ReconciliationCategory5 import ReconciliationCategory5
from .ReconciliationCategory4 import ReconciliationCategory4

class ReportingRequirement3Choice(base_types._BaseFieldType):

	__slots__ = ["_RptgRqrmnt", "_NoRptgRqrmnt"]
	@property
	def RptgRqrmnt(self):
		return self._RptgRqrmnt

	@RptgRqrmnt.setter
	def RptgRqrmnt(self, value):
		self._RptgRqrmnt = value if type(value) != base_types.auto else self.make_default("RptgRqrmnt")

	@RptgRqrmnt.deleter
	def RptgRqrmnt(self):
		del self._RptgRqrmnt
		self._RptgRqrmnt = None

	@property
	def NoRptgRqrmnt(self):
		return self._NoRptgRqrmnt

	@NoRptgRqrmnt.setter
	def NoRptgRqrmnt(self, value):
		self._NoRptgRqrmnt = value if type(value) != base_types.auto else self.make_default("NoRptgRqrmnt")

	@NoRptgRqrmnt.deleter
	def NoRptgRqrmnt(self):
		del self._NoRptgRqrmnt
		self._NoRptgRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgRqrmnt', type=ReconciliationCategory5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoRptgRqrmnt', type=ReconciliationCategory4, min=0, max=1, mutex_group=1, array=False),
	))

