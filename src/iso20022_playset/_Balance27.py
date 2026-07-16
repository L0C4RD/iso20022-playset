# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShortLong1Code
from . import SubBalanceQuantity9Choice

class Balance27(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_ShrtLngInd"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity9Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity9Choice, False)

	@property
	def ShrtLngInd(self):
		return self._ShrtLngInd

	@ShrtLngInd.setter
	def ShrtLngInd(self, value):
		self._ShrtLngInd = value if value is not None else base_types.UninitialisedField(self, 'ShrtLngInd', ShortLong1Code, False)

	@ShrtLngInd.deleter
	def ShrtLngInd(self):
		del self._ShrtLngInd
		self._ShrtLngInd = base_types.UninitialisedField(self, 'ShrtLngInd', ShortLong1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
	))