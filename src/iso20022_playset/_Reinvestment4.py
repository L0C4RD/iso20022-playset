# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._FinancialInstrument87 import FinancialInstrument87
from ._PercentageRate import PercentageRate

class Reinvestment4(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_ReqdNAVCcy", "_RinvstmtPctg"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if type(value) != base_types.auto else self.make_default("ReqdNAVCcy")

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = None

	@property
	def RinvstmtPctg(self):
		return self._RinvstmtPctg

	@RinvstmtPctg.setter
	def RinvstmtPctg(self, value):
		self._RinvstmtPctg = value if type(value) != base_types.auto else self.make_default("RinvstmtPctg")

	@RinvstmtPctg.deleter
	def RinvstmtPctg(self):
		del self._RinvstmtPctg
		self._RinvstmtPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument87, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))