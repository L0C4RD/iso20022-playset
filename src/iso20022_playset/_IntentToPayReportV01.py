# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import ReportLine1

class IntentToPayReportV01(base_types._BaseFieldType):

	__slots__ = ["_RptId", "_RptdItms"]
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

	@property
	def RptdItms(self):
		return self._RptdItms

	@RptdItms.setter
	def RptdItms(self, value):
		self._RptdItms = value if value is not None else base_types.UninitialisedField(self, 'RptdItms', ReportLine1, True)

	@RptdItms.deleter
	def RptdItms(self):
		del self._RptdItms
		self._RptdItms = base_types.UninitialisedField(self, 'RptdItms', ReportLine1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdItms', type=ReportLine1, min=0, max=None, mutex_group=None, array=True),
	))