# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyReport1Choice
from . import SupplementaryData1

class FinancialSupervisedPartyIdentityReportV01(base_types._BaseFieldType):

	__slots__ = ["_PtyData", "_SplmtryData"]
	@property
	def PtyData(self):
		return self._PtyData

	@PtyData.setter
	def PtyData(self, value):
		self._PtyData = value if value is not None else base_types.UninitialisedField(self, 'PtyData', PartyReport1Choice, True)

	@PtyData.deleter
	def PtyData(self):
		del self._PtyData
		self._PtyData = base_types.UninitialisedField(self, 'PtyData', PartyReport1Choice, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyData', type=PartyReport1Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))