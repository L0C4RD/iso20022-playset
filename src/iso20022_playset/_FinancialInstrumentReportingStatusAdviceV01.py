# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageReportHeader4
from . import SupplementaryData1

class FinancialInstrumentReportingStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StsAdvc"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if value is not None else base_types.UninitialisedField(self, 'StsAdvc', MessageReportHeader4, True)

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = base_types.UninitialisedField(self, 'StsAdvc', MessageReportHeader4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAdvc', type=MessageReportHeader4, min=1, max=None, mutex_group=None, array=True),
	))