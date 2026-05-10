import base_types
import CrystallisationDay1
import BenchmarkCurveName13Choice
import ActiveOrHistoricCurrencyCode
import Max3NumericText
import InterestRateIndexTenor2Code

class RateTypeAndLookback2(base_types._BaseFieldType):

	__slots__ = ["_LookBckDays", "_Tnr", "_Ccy", "_CrstllstnDt", "_Tp"]
	@property
	def LookBckDays(self):
		return self._LookBckDays

	@LookBckDays.setter
	def LookBckDays(self, value):
		self._LookBckDays = value if type(value) != auto else self.make_default("LookBckDays")

	@LookBckDays.deleter
	def LookBckDays(self):
		del self._LookBckDays
		self._LookBckDays = None

	@property
	def Tnr(self):
		return self._Tnr

	@Tnr.setter
	def Tnr(self, value):
		self._Tnr = value if type(value) != auto else self.make_default("Tnr")

	@Tnr.deleter
	def Tnr(self):
		del self._Tnr
		self._Tnr = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CrstllstnDt(self):
		return self._CrstllstnDt

	@CrstllstnDt.setter
	def CrstllstnDt(self, value):
		self._CrstllstnDt = value if type(value) != auto else self.make_default("CrstllstnDt")

	@CrstllstnDt.deleter
	def CrstllstnDt(self):
		del self._CrstllstnDt
		self._CrstllstnDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LookBckDays', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tnr', type=InterestRateIndexTenor2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnDt', type=CrystallisationDay1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BenchmarkCurveName13Choice, min=1, max=1, mutex_group=None, array=False),
	))

