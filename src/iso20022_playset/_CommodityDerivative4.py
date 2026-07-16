# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CommodityDerivative2Choice

class CommodityDerivative4(base_types._BaseFieldType):

	__slots__ = ["_ClssSpcfc", "_NtnlCcy"]
	@property
	def ClssSpcfc(self):
		return self._ClssSpcfc

	@ClssSpcfc.setter
	def ClssSpcfc(self, value):
		self._ClssSpcfc = value if value is not None else base_types.UninitialisedField(self, 'ClssSpcfc', CommodityDerivative2Choice, False)

	@ClssSpcfc.deleter
	def ClssSpcfc(self):
		del self._ClssSpcfc
		self._ClssSpcfc = base_types.UninitialisedField(self, 'ClssSpcfc', CommodityDerivative2Choice, False)

	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssSpcfc', type=CommodityDerivative2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))