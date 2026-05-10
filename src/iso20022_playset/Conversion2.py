from . import base_types
from .FinancialInstrumentIdentification1 import FinancialInstrumentIdentification1
from .AdditionalInformation15 import AdditionalInformation15
from .DecimalNumber import DecimalNumber
from .Unit13 import Unit13

class Conversion2(base_types._BaseFieldType):

	__slots__ = ["_TtlUnitsNb", "_AddtlInf", "_SrcScty", "_UnitsDtls"]
	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def SrcScty(self):
		return self._SrcScty

	@SrcScty.setter
	def SrcScty(self, value):
		self._SrcScty = value if type(value) != auto else self.make_default("SrcScty")

	@SrcScty.deleter
	def SrcScty(self):
		del self._SrcScty
		self._SrcScty = None

	@property
	def UnitsDtls(self):
		return self._UnitsDtls

	@UnitsDtls.setter
	def UnitsDtls(self, value):
		self._UnitsDtls = value if type(value) != auto else self.make_default("UnitsDtls")

	@UnitsDtls.deleter
	def UnitsDtls(self):
		del self._UnitsDtls
		self._UnitsDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SrcScty', type=FinancialInstrumentIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsDtls', type=Unit13, min=0, max=None, mutex_group=None, array=True),
	))

