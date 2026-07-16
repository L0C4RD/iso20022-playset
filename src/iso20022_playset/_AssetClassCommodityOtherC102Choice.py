# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OtherC10CommodityDeliverable2
from . import OtherC10CommodityNonDeliverable2

class AssetClassCommodityOtherC102Choice(base_types._BaseFieldType):

	__slots__ = ["_Dlvrbl", "_NonDlvrbl"]
	@property
	def Dlvrbl(self):
		return self._Dlvrbl

	@Dlvrbl.setter
	def Dlvrbl(self, value):
		self._Dlvrbl = value if value is not None else base_types.UninitialisedField(self, 'Dlvrbl', OtherC10CommodityDeliverable2, False)

	@Dlvrbl.deleter
	def Dlvrbl(self):
		del self._Dlvrbl
		self._Dlvrbl = base_types.UninitialisedField(self, 'Dlvrbl', OtherC10CommodityDeliverable2, False)

	@property
	def NonDlvrbl(self):
		return self._NonDlvrbl

	@NonDlvrbl.setter
	def NonDlvrbl(self, value):
		self._NonDlvrbl = value if value is not None else base_types.UninitialisedField(self, 'NonDlvrbl', OtherC10CommodityNonDeliverable2, False)

	@NonDlvrbl.deleter
	def NonDlvrbl(self):
		del self._NonDlvrbl
		self._NonDlvrbl = base_types.UninitialisedField(self, 'NonDlvrbl', OtherC10CommodityNonDeliverable2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dlvrbl', type=OtherC10CommodityDeliverable2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonDlvrbl', type=OtherC10CommodityNonDeliverable2, min=0, max=1, mutex_group=1, array=False),
	))