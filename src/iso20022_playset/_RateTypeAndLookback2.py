# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BenchmarkCurveName13Choice
from . import CrystallisationDay1
from . import InterestRateIndexTenor2Code
from . import Max3NumericText

class RateTypeAndLookback2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CrstllstnDt", "_LookBckDays", "_Tnr", "_Tp"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def CrstllstnDt(self):
		return self._CrstllstnDt

	@CrstllstnDt.setter
	def CrstllstnDt(self, value):
		self._CrstllstnDt = value if value is not None else base_types.UninitialisedField(self, 'CrstllstnDt', CrystallisationDay1, False)

	@CrstllstnDt.deleter
	def CrstllstnDt(self):
		del self._CrstllstnDt
		self._CrstllstnDt = base_types.UninitialisedField(self, 'CrstllstnDt', CrystallisationDay1, False)

	@property
	def LookBckDays(self):
		return self._LookBckDays

	@LookBckDays.setter
	def LookBckDays(self, value):
		self._LookBckDays = value if value is not None else base_types.UninitialisedField(self, 'LookBckDays', Max3NumericText, False)

	@LookBckDays.deleter
	def LookBckDays(self):
		del self._LookBckDays
		self._LookBckDays = base_types.UninitialisedField(self, 'LookBckDays', Max3NumericText, False)

	@property
	def Tnr(self):
		return self._Tnr

	@Tnr.setter
	def Tnr(self, value):
		self._Tnr = value if value is not None else base_types.UninitialisedField(self, 'Tnr', InterestRateIndexTenor2Code, False)

	@Tnr.deleter
	def Tnr(self):
		del self._Tnr
		self._Tnr = base_types.UninitialisedField(self, 'Tnr', InterestRateIndexTenor2Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BenchmarkCurveName13Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BenchmarkCurveName13Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnDt', type=CrystallisationDay1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LookBckDays', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tnr', type=InterestRateIndexTenor2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BenchmarkCurveName13Choice, min=1, max=1, mutex_group=None, array=False),
	))