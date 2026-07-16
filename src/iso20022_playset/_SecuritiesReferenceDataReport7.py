# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtInstrument2
from . import DerivativeInstrument5
from . import LEIIdentifier
from . import Max35Text
from . import RecordTechnicalData4
from . import SecurityInstrumentDescription17
from . import TradingVenueAttributes2

class SecuritiesReferenceDataReport7(base_types._BaseFieldType):

	__slots__ = ["_DebtInstrmAttrbts", "_DerivInstrmAttrbts", "_FinInstrmGnlAttrbts", "_Issr", "_TechAttrbts", "_TechRcrdId", "_TradgVnRltdAttrbts"]
	@property
	def DebtInstrmAttrbts(self):
		return self._DebtInstrmAttrbts

	@DebtInstrmAttrbts.setter
	def DebtInstrmAttrbts(self, value):
		self._DebtInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'DebtInstrmAttrbts', DebtInstrument2, False)

	@DebtInstrmAttrbts.deleter
	def DebtInstrmAttrbts(self):
		del self._DebtInstrmAttrbts
		self._DebtInstrmAttrbts = base_types.UninitialisedField(self, 'DebtInstrmAttrbts', DebtInstrument2, False)

	@property
	def DerivInstrmAttrbts(self):
		return self._DerivInstrmAttrbts

	@DerivInstrmAttrbts.setter
	def DerivInstrmAttrbts(self, value):
		self._DerivInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'DerivInstrmAttrbts', DerivativeInstrument5, False)

	@DerivInstrmAttrbts.deleter
	def DerivInstrmAttrbts(self):
		del self._DerivInstrmAttrbts
		self._DerivInstrmAttrbts = base_types.UninitialisedField(self, 'DerivInstrmAttrbts', DerivativeInstrument5, False)

	@property
	def FinInstrmGnlAttrbts(self):
		return self._FinInstrmGnlAttrbts

	@FinInstrmGnlAttrbts.setter
	def FinInstrmGnlAttrbts(self, value):
		self._FinInstrmGnlAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmGnlAttrbts', SecurityInstrumentDescription17, False)

	@FinInstrmGnlAttrbts.deleter
	def FinInstrmGnlAttrbts(self):
		del self._FinInstrmGnlAttrbts
		self._FinInstrmGnlAttrbts = base_types.UninitialisedField(self, 'FinInstrmGnlAttrbts', SecurityInstrumentDescription17, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', LEIIdentifier, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', LEIIdentifier, False)

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData4, False)

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData4, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def TradgVnRltdAttrbts(self):
		return self._TradgVnRltdAttrbts

	@TradgVnRltdAttrbts.setter
	def TradgVnRltdAttrbts(self, value):
		self._TradgVnRltdAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TradgVnRltdAttrbts', TradingVenueAttributes2, True)

	@TradgVnRltdAttrbts.deleter
	def TradgVnRltdAttrbts(self):
		del self._TradgVnRltdAttrbts
		self._TradgVnRltdAttrbts = base_types.UninitialisedField(self, 'TradgVnRltdAttrbts', TradingVenueAttributes2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtInstrmAttrbts', type=DebtInstrument2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivInstrmAttrbts', type=DerivativeInstrument5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmGnlAttrbts', type=SecurityInstrumentDescription17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVnRltdAttrbts', type=TradingVenueAttributes2, min=1, max=None, mutex_group=None, array=True),
	))