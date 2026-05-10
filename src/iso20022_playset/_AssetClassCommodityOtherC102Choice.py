from . import base_types
from ._OtherC10CommodityNonDeliverable2 import OtherC10CommodityNonDeliverable2
from ._OtherC10CommodityDeliverable2 import OtherC10CommodityDeliverable2

class AssetClassCommodityOtherC102Choice(base_types._BaseFieldType):

	__slots__ = ["_Dlvrbl", "_NonDlvrbl"]
	@property
	def Dlvrbl(self):
		return self._Dlvrbl

	@Dlvrbl.setter
	def Dlvrbl(self, value):
		self._Dlvrbl = value if type(value) != base_types.auto else self.make_default("Dlvrbl")

	@Dlvrbl.deleter
	def Dlvrbl(self):
		del self._Dlvrbl
		self._Dlvrbl = None

	@property
	def NonDlvrbl(self):
		return self._NonDlvrbl

	@NonDlvrbl.setter
	def NonDlvrbl(self, value):
		self._NonDlvrbl = value if type(value) != base_types.auto else self.make_default("NonDlvrbl")

	@NonDlvrbl.deleter
	def NonDlvrbl(self):
		del self._NonDlvrbl
		self._NonDlvrbl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dlvrbl', type=OtherC10CommodityDeliverable2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonDlvrbl', type=OtherC10CommodityNonDeliverable2, min=0, max=1, mutex_group=1, array=False),
	))

