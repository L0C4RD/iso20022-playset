from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._CollateralAccount4 import CollateralAccount4

class CCPCollateralReportV01(base_types._BaseFieldType):

	__slots__ = ["_CollAcctOwnr", "_SplmtryData"]
	@property
	def CollAcctOwnr(self):
		return self._CollAcctOwnr

	@CollAcctOwnr.setter
	def CollAcctOwnr(self, value):
		self._CollAcctOwnr = value if type(value) != base_types.auto else self.make_default("CollAcctOwnr")

	@CollAcctOwnr.deleter
	def CollAcctOwnr(self):
		del self._CollAcctOwnr
		self._CollAcctOwnr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollAcctOwnr', type=CollateralAccount4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

