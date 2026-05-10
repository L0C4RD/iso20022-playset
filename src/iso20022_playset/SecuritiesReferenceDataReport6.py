from . import base_types
from .TradingVenueAttributes1 import TradingVenueAttributes1
from .LEIIdentifier import LEIIdentifier
from .SecurityInstrumentDescription9 import SecurityInstrumentDescription9
from .DebtInstrument2 import DebtInstrument2
from .DerivativeInstrument5 import DerivativeInstrument5
from .RecordTechnicalData4 import RecordTechnicalData4
from .Max35Text import Max35Text

class SecuritiesReferenceDataReport6(base_types._BaseFieldType):

	__slots__ = ["_TradgVnRltdAttrbts", "_DerivInstrmAttrbts", "_TechAttrbts", "_TechRcrdId", "_FinInstrmGnlAttrbts", "_Issr", "_DebtInstrmAttrbts"]
	@property
	def TradgVnRltdAttrbts(self):
		return self._TradgVnRltdAttrbts

	@TradgVnRltdAttrbts.setter
	def TradgVnRltdAttrbts(self, value):
		self._TradgVnRltdAttrbts = value if type(value) != base_types.auto else self.make_default("TradgVnRltdAttrbts")

	@TradgVnRltdAttrbts.deleter
	def TradgVnRltdAttrbts(self):
		del self._TradgVnRltdAttrbts
		self._TradgVnRltdAttrbts = None

	@property
	def DerivInstrmAttrbts(self):
		return self._DerivInstrmAttrbts

	@DerivInstrmAttrbts.setter
	def DerivInstrmAttrbts(self, value):
		self._DerivInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("DerivInstrmAttrbts")

	@DerivInstrmAttrbts.deleter
	def DerivInstrmAttrbts(self):
		del self._DerivInstrmAttrbts
		self._DerivInstrmAttrbts = None

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if type(value) != base_types.auto else self.make_default("TechAttrbts")

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def FinInstrmGnlAttrbts(self):
		return self._FinInstrmGnlAttrbts

	@FinInstrmGnlAttrbts.setter
	def FinInstrmGnlAttrbts(self, value):
		self._FinInstrmGnlAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmGnlAttrbts")

	@FinInstrmGnlAttrbts.deleter
	def FinInstrmGnlAttrbts(self):
		del self._FinInstrmGnlAttrbts
		self._FinInstrmGnlAttrbts = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def DebtInstrmAttrbts(self):
		return self._DebtInstrmAttrbts

	@DebtInstrmAttrbts.setter
	def DebtInstrmAttrbts(self, value):
		self._DebtInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("DebtInstrmAttrbts")

	@DebtInstrmAttrbts.deleter
	def DebtInstrmAttrbts(self):
		del self._DebtInstrmAttrbts
		self._DebtInstrmAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgVnRltdAttrbts', type=TradingVenueAttributes1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DerivInstrmAttrbts', type=DerivativeInstrument5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmGnlAttrbts', type=SecurityInstrumentDescription9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DebtInstrmAttrbts', type=DebtInstrument2, min=0, max=1, mutex_group=None, array=False),
	))

