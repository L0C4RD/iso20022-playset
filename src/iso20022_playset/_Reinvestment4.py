# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import FinancialInstrument87
from . import PercentageRate

class Reinvestment4(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_ReqdNAVCcy", "_RinvstmtPctg"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument87, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument87, False)

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if value is not None else base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveCurrencyCode, False)

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = base_types.UninitialisedField(self, 'ReqdNAVCcy', ActiveCurrencyCode, False)

	@property
	def RinvstmtPctg(self):
		return self._RinvstmtPctg

	@RinvstmtPctg.setter
	def RinvstmtPctg(self, value):
		self._RinvstmtPctg = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtPctg', PercentageRate, False)

	@RinvstmtPctg.deleter
	def RinvstmtPctg(self):
		del self._RinvstmtPctg
		self._RinvstmtPctg = base_types.UninitialisedField(self, 'RinvstmtPctg', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument87, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))