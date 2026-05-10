from . import base_types
from .SecurityInstrumentDescription23 import SecurityInstrumentDescription23
from .DerivativeInstrument6 import DerivativeInstrument6
from .DebtInstrument4 import DebtInstrument4

class SecurityInstrumentDescription22(base_types._BaseFieldType):

	__slots__ = ["_DebtInstrmAttrbts", "_DerivInstrmAttrbts", "_FinInstrmGnlAttrbts"]
	@property
	def DebtInstrmAttrbts(self):
		return self._DebtInstrmAttrbts

	@DebtInstrmAttrbts.setter
	def DebtInstrmAttrbts(self, value):
		self._DebtInstrmAttrbts = value if type(value) != auto else self.make_default("DebtInstrmAttrbts")

	@DebtInstrmAttrbts.deleter
	def DebtInstrmAttrbts(self):
		del self._DebtInstrmAttrbts
		self._DebtInstrmAttrbts = None

	@property
	def DerivInstrmAttrbts(self):
		return self._DerivInstrmAttrbts

	@DerivInstrmAttrbts.setter
	def DerivInstrmAttrbts(self, value):
		self._DerivInstrmAttrbts = value if type(value) != auto else self.make_default("DerivInstrmAttrbts")

	@DerivInstrmAttrbts.deleter
	def DerivInstrmAttrbts(self):
		del self._DerivInstrmAttrbts
		self._DerivInstrmAttrbts = None

	@property
	def FinInstrmGnlAttrbts(self):
		return self._FinInstrmGnlAttrbts

	@FinInstrmGnlAttrbts.setter
	def FinInstrmGnlAttrbts(self, value):
		self._FinInstrmGnlAttrbts = value if type(value) != auto else self.make_default("FinInstrmGnlAttrbts")

	@FinInstrmGnlAttrbts.deleter
	def FinInstrmGnlAttrbts(self):
		del self._FinInstrmGnlAttrbts
		self._FinInstrmGnlAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtInstrmAttrbts', type=DebtInstrument4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivInstrmAttrbts', type=DerivativeInstrument6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmGnlAttrbts', type=SecurityInstrumentDescription23, min=1, max=1, mutex_group=None, array=False),
	))

