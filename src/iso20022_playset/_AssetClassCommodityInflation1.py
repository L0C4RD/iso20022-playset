# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AssetClassProductType12Code import AssetClassProductType12Code

class AssetClassCommodityInflation1(base_types._BaseFieldType):

	__slots__ = ["_BasePdct"]
	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if type(value) != base_types.auto else self.make_default("BasePdct")

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BasePdct', type=AssetClassProductType12Code, min=1, max=1, mutex_group=None, array=False),
	))