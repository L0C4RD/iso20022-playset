from . import base_types
from ._DateTimePeriod2 import DateTimePeriod2
from ._YesNoIndicator import YesNoIndicator
from ._PercentageRate import PercentageRate

class MarketMakerProfile2(base_types._BaseFieldType):

	__slots__ = ["_MaxSprd", "_Dscnt", "_CtrctPrd", "_Cmplc"]
	@property
	def MaxSprd(self):
		return self._MaxSprd

	@MaxSprd.setter
	def MaxSprd(self, value):
		self._MaxSprd = value if type(value) != base_types.auto else self.make_default("MaxSprd")

	@MaxSprd.deleter
	def MaxSprd(self):
		del self._MaxSprd
		self._MaxSprd = None

	@property
	def Dscnt(self):
		return self._Dscnt

	@Dscnt.setter
	def Dscnt(self, value):
		self._Dscnt = value if type(value) != base_types.auto else self.make_default("Dscnt")

	@Dscnt.deleter
	def Dscnt(self):
		del self._Dscnt
		self._Dscnt = None

	@property
	def CtrctPrd(self):
		return self._CtrctPrd

	@CtrctPrd.setter
	def CtrctPrd(self, value):
		self._CtrctPrd = value if type(value) != base_types.auto else self.make_default("CtrctPrd")

	@CtrctPrd.deleter
	def CtrctPrd(self):
		del self._CtrctPrd
		self._CtrctPrd = None

	@property
	def Cmplc(self):
		return self._Cmplc

	@Cmplc.setter
	def Cmplc(self, value):
		self._Cmplc = value if type(value) != base_types.auto else self.make_default("Cmplc")

	@Cmplc.deleter
	def Cmplc(self):
		del self._Cmplc
		self._Cmplc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxSprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscnt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctPrd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmplc', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

