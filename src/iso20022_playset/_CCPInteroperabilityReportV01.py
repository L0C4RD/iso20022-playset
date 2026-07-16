# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InteroperabilityCCP1
from . import SupplementaryData1

class CCPInteroperabilityReportV01(base_types._BaseFieldType):

	__slots__ = ["_IntrprbltyCCP", "_SplmtryData"]
	@property
	def IntrprbltyCCP(self):
		return self._IntrprbltyCCP

	@IntrprbltyCCP.setter
	def IntrprbltyCCP(self, value):
		self._IntrprbltyCCP = value if value is not None else base_types.UninitialisedField(self, 'IntrprbltyCCP', InteroperabilityCCP1, True)

	@IntrprbltyCCP.deleter
	def IntrprbltyCCP(self):
		del self._IntrprbltyCCP
		self._IntrprbltyCCP = base_types.UninitialisedField(self, 'IntrprbltyCCP', InteroperabilityCCP1, True)

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
		base_types.FieldEntry(name='IntrprbltyCCP', type=InteroperabilityCCP1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))