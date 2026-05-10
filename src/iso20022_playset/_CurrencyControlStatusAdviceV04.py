from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._CurrencyControlHeader7 import CurrencyControlHeader7
from ._CurrencyControlGroupStatus3 import CurrencyControlGroupStatus3
from ._CurrencyControlPackageStatus3 import CurrencyControlPackageStatus3

class CurrencyControlStatusAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_GrpSts", "_SplmtryData", "_PackgSts"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def GrpSts(self):
		return self._GrpSts

	@GrpSts.setter
	def GrpSts(self, value):
		self._GrpSts = value if type(value) != base_types.auto else self.make_default("GrpSts")

	@GrpSts.deleter
	def GrpSts(self):
		del self._GrpSts
		self._GrpSts = None

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

	@property
	def PackgSts(self):
		return self._PackgSts

	@PackgSts.setter
	def PackgSts(self, value):
		self._PackgSts = value if type(value) != base_types.auto else self.make_default("PackgSts")

	@PackgSts.deleter
	def PackgSts(self):
		del self._PackgSts
		self._PackgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpSts', type=CurrencyControlGroupStatus3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PackgSts', type=CurrencyControlPackageStatus3, min=0, max=None, mutex_group=None, array=True),
	))

