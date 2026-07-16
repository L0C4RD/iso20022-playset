# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReconciliationCategory4
from . import ReconciliationCategory5

class ReportingRequirement3Choice(base_types._BaseFieldType):

	__slots__ = ["_NoRptgRqrmnt", "_RptgRqrmnt"]
	@property
	def NoRptgRqrmnt(self):
		return self._NoRptgRqrmnt

	@NoRptgRqrmnt.setter
	def NoRptgRqrmnt(self, value):
		self._NoRptgRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'NoRptgRqrmnt', ReconciliationCategory4, False)

	@NoRptgRqrmnt.deleter
	def NoRptgRqrmnt(self):
		del self._NoRptgRqrmnt
		self._NoRptgRqrmnt = base_types.UninitialisedField(self, 'NoRptgRqrmnt', ReconciliationCategory4, False)

	@property
	def RptgRqrmnt(self):
		return self._RptgRqrmnt

	@RptgRqrmnt.setter
	def RptgRqrmnt(self, value):
		self._RptgRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'RptgRqrmnt', ReconciliationCategory5, False)

	@RptgRqrmnt.deleter
	def RptgRqrmnt(self):
		del self._RptgRqrmnt
		self._RptgRqrmnt = base_types.UninitialisedField(self, 'RptgRqrmnt', ReconciliationCategory5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoRptgRqrmnt', type=ReconciliationCategory4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RptgRqrmnt', type=ReconciliationCategory5, min=0, max=1, mutex_group=1, array=False),
	))