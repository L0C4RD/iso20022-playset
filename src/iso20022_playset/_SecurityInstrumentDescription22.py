# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtInstrument4
from . import DerivativeInstrument6
from . import SecurityInstrumentDescription23

class SecurityInstrumentDescription22(base_types._BaseFieldType):

	__slots__ = ["_DebtInstrmAttrbts", "_DerivInstrmAttrbts", "_FinInstrmGnlAttrbts"]
	@property
	def DebtInstrmAttrbts(self):
		return self._DebtInstrmAttrbts

	@DebtInstrmAttrbts.setter
	def DebtInstrmAttrbts(self, value):
		self._DebtInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'DebtInstrmAttrbts', DebtInstrument4, False)

	@DebtInstrmAttrbts.deleter
	def DebtInstrmAttrbts(self):
		del self._DebtInstrmAttrbts
		self._DebtInstrmAttrbts = base_types.UninitialisedField(self, 'DebtInstrmAttrbts', DebtInstrument4, False)

	@property
	def DerivInstrmAttrbts(self):
		return self._DerivInstrmAttrbts

	@DerivInstrmAttrbts.setter
	def DerivInstrmAttrbts(self, value):
		self._DerivInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'DerivInstrmAttrbts', DerivativeInstrument6, False)

	@DerivInstrmAttrbts.deleter
	def DerivInstrmAttrbts(self):
		del self._DerivInstrmAttrbts
		self._DerivInstrmAttrbts = base_types.UninitialisedField(self, 'DerivInstrmAttrbts', DerivativeInstrument6, False)

	@property
	def FinInstrmGnlAttrbts(self):
		return self._FinInstrmGnlAttrbts

	@FinInstrmGnlAttrbts.setter
	def FinInstrmGnlAttrbts(self, value):
		self._FinInstrmGnlAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmGnlAttrbts', SecurityInstrumentDescription23, False)

	@FinInstrmGnlAttrbts.deleter
	def FinInstrmGnlAttrbts(self):
		del self._FinInstrmGnlAttrbts
		self._FinInstrmGnlAttrbts = base_types.UninitialisedField(self, 'FinInstrmGnlAttrbts', SecurityInstrumentDescription23, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtInstrmAttrbts', type=DebtInstrument4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivInstrmAttrbts', type=DerivativeInstrument6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmGnlAttrbts', type=SecurityInstrumentDescription23, min=1, max=1, mutex_group=None, array=False),
	))