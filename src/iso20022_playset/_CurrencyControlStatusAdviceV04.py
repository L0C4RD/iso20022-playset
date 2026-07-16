# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlGroupStatus3
from . import CurrencyControlHeader7
from . import CurrencyControlPackageStatus3
from . import SupplementaryData1

class CurrencyControlStatusAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_GrpSts", "_PackgSts", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader7, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader7, False)

	@property
	def GrpSts(self):
		return self._GrpSts

	@GrpSts.setter
	def GrpSts(self, value):
		self._GrpSts = value if value is not None else base_types.UninitialisedField(self, 'GrpSts', CurrencyControlGroupStatus3, True)

	@GrpSts.deleter
	def GrpSts(self):
		del self._GrpSts
		self._GrpSts = base_types.UninitialisedField(self, 'GrpSts', CurrencyControlGroupStatus3, True)

	@property
	def PackgSts(self):
		return self._PackgSts

	@PackgSts.setter
	def PackgSts(self, value):
		self._PackgSts = value if value is not None else base_types.UninitialisedField(self, 'PackgSts', CurrencyControlPackageStatus3, True)

	@PackgSts.deleter
	def PackgSts(self):
		del self._PackgSts
		self._PackgSts = base_types.UninitialisedField(self, 'PackgSts', CurrencyControlPackageStatus3, True)

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
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpSts', type=CurrencyControlGroupStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PackgSts', type=CurrencyControlPackageStatus3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))