# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._ShortLong1Code import ShortLong1Code

class SignedQuantityFormat13(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_ShrtLngPos"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if type(value) != base_types.auto else self.make_default("ShrtLngPos")

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))