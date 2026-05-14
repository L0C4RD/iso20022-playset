# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._AmountAndDirection106 import AmountAndDirection106
from ._Schedule11 import Schedule11

class NotionalAmount6(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_SchdlPrd"]
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
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if type(value) != base_types.auto else self.make_default("SchdlPrd")

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdlPrd', type=Schedule11, min=0, max=None, mutex_group=None, array=True),
	))