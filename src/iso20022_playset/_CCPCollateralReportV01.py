# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralAccount4
from . import SupplementaryData1

class CCPCollateralReportV01(base_types._BaseFieldType):

	__slots__ = ["_CollAcctOwnr", "_SplmtryData"]
	@property
	def CollAcctOwnr(self):
		return self._CollAcctOwnr

	@CollAcctOwnr.setter
	def CollAcctOwnr(self, value):
		self._CollAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CollAcctOwnr', CollateralAccount4, True)

	@CollAcctOwnr.deleter
	def CollAcctOwnr(self):
		del self._CollAcctOwnr
		self._CollAcctOwnr = base_types.UninitialisedField(self, 'CollAcctOwnr', CollateralAccount4, True)

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
		base_types.FieldEntry(name='CollAcctOwnr', type=CollateralAccount4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))