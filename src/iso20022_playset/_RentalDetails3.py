# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO3NumericCurrencyCode
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import Max4NumericText
from . import Max70Text
from . import PeriodUnit2Code
from . import ServiceStartEnd3

class RentalDetails3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_DtTm", "_Id", "_Rtr", "_Start", "_TmPrd", "_TmPrdRate", "_TmPrdUnit"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@property
	def Rtr(self):
		return self._Rtr

	@Rtr.setter
	def Rtr(self, value):
		self._Rtr = value if value is not None else base_types.UninitialisedField(self, 'Rtr', ServiceStartEnd3, False)

	@Rtr.deleter
	def Rtr(self):
		del self._Rtr
		self._Rtr = base_types.UninitialisedField(self, 'Rtr', ServiceStartEnd3, False)

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if value is not None else base_types.UninitialisedField(self, 'Start', ServiceStartEnd3, False)

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = base_types.UninitialisedField(self, 'Start', ServiceStartEnd3, False)

	@property
	def TmPrd(self):
		return self._TmPrd

	@TmPrd.setter
	def TmPrd(self, value):
		self._TmPrd = value if value is not None else base_types.UninitialisedField(self, 'TmPrd', PeriodUnit2Code, True)

	@TmPrd.deleter
	def TmPrd(self):
		del self._TmPrd
		self._TmPrd = base_types.UninitialisedField(self, 'TmPrd', PeriodUnit2Code, True)

	@property
	def TmPrdRate(self):
		return self._TmPrdRate

	@TmPrdRate.setter
	def TmPrdRate(self, value):
		self._TmPrdRate = value if value is not None else base_types.UninitialisedField(self, 'TmPrdRate', ImpliedCurrencyAndAmount, False)

	@TmPrdRate.deleter
	def TmPrdRate(self):
		del self._TmPrdRate
		self._TmPrdRate = base_types.UninitialisedField(self, 'TmPrdRate', ImpliedCurrencyAndAmount, False)

	@property
	def TmPrdUnit(self):
		return self._TmPrdUnit

	@TmPrdUnit.setter
	def TmPrdUnit(self, value):
		self._TmPrdUnit = value if value is not None else base_types.UninitialisedField(self, 'TmPrdUnit', Max4NumericText, False)

	@TmPrdUnit.deleter
	def TmPrdUnit(self):
		del self._TmPrdUnit
		self._TmPrdUnit = base_types.UninitialisedField(self, 'TmPrdUnit', Max4NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtr', type=ServiceStartEnd3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Start', type=ServiceStartEnd3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmPrd', type=PeriodUnit2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TmPrdRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmPrdUnit', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
	))