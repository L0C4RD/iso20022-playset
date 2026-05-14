# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CommodityDerivative2Choice import CommodityDerivative2Choice

class CommodityDerivative4(base_types._BaseFieldType):

	__slots__ = ["_ClssSpcfc", "_NtnlCcy"]
	@property
	def ClssSpcfc(self):
		return self._ClssSpcfc

	@ClssSpcfc.setter
	def ClssSpcfc(self, value):
		self._ClssSpcfc = value if type(value) != base_types.auto else self.make_default("ClssSpcfc")

	@ClssSpcfc.deleter
	def ClssSpcfc(self):
		del self._ClssSpcfc
		self._ClssSpcfc = None

	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if type(value) != base_types.auto else self.make_default("NtnlCcy")

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssSpcfc', type=CommodityDerivative2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))