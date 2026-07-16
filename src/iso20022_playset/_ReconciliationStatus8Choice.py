# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import ReconciliationMatchedStatus9Choice

class ReconciliationStatus8Choice(base_types._BaseFieldType):

	__slots__ = ["_NoRcncltnReqrd", "_RptgData"]
	@property
	def NoRcncltnReqrd(self):
		return self._NoRcncltnReqrd

	@NoRcncltnReqrd.setter
	def NoRcncltnReqrd(self, value):
		self._NoRcncltnReqrd = value if value is not None else base_types.UninitialisedField(self, 'NoRcncltnReqrd', NoReasonCode, False)

	@NoRcncltnReqrd.deleter
	def NoRcncltnReqrd(self):
		del self._NoRcncltnReqrd
		self._NoRcncltnReqrd = base_types.UninitialisedField(self, 'NoRcncltnReqrd', NoReasonCode, False)

	@property
	def RptgData(self):
		return self._RptgData

	@RptgData.setter
	def RptgData(self, value):
		self._RptgData = value if value is not None else base_types.UninitialisedField(self, 'RptgData', ReconciliationMatchedStatus9Choice, False)

	@RptgData.deleter
	def RptgData(self):
		del self._RptgData
		self._RptgData = base_types.UninitialisedField(self, 'RptgData', ReconciliationMatchedStatus9Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoRcncltnReqrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RptgData', type=ReconciliationMatchedStatus9Choice, min=0, max=1, mutex_group=1, array=False),
	))