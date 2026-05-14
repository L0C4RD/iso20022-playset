# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AdjustmentDirection1Code import AdjustmentDirection1Code

class Adjustment5(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Drctn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if type(value) != base_types.auto else self.make_default("Drctn")

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drctn', type=AdjustmentDirection1Code, min=1, max=1, mutex_group=None, array=False),
	))