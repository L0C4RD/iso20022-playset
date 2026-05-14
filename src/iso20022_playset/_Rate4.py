# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmountRange2 import ActiveOrHistoricCurrencyAndAmountRange2
from ._RateType4Choice import RateType4Choice

class Rate4(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_VldtyRg"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def VldtyRg(self):
		return self._VldtyRg

	@VldtyRg.setter
	def VldtyRg(self, value):
		self._VldtyRg = value if type(value) != base_types.auto else self.make_default("VldtyRg")

	@VldtyRg.deleter
	def VldtyRg(self):
		del self._VldtyRg
		self._VldtyRg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=RateType4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyRg', type=ActiveOrHistoricCurrencyAndAmountRange2, min=0, max=1, mutex_group=None, array=False),
	))