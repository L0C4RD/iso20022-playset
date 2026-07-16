# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import DecimalNumber
from . import FinancialInstrumentIdentification7
from . import Unit15

class Conversion4(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_SrcScty", "_TtlUnitsNb", "_UnitsDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def SrcScty(self):
		return self._SrcScty

	@SrcScty.setter
	def SrcScty(self, value):
		self._SrcScty = value if value is not None else base_types.UninitialisedField(self, 'SrcScty', FinancialInstrumentIdentification7, False)

	@SrcScty.deleter
	def SrcScty(self):
		del self._SrcScty
		self._SrcScty = base_types.UninitialisedField(self, 'SrcScty', FinancialInstrumentIdentification7, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', DecimalNumber, False)

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if value is not None else base_types.UninitialisedField(self, 'UnitsDtls', Unit15, True)

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = base_types.UninitialisedField(self, 'UnitsDtls', Unit15, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SrcScty', type=FinancialInstrumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit15, min=0, max=None, mutex_group=None, array=True),
	))