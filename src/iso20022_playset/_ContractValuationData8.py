# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection109
from . import ISODateTime
from . import LongFraction19DecimalNumber
from . import ValuationType1Code

class ContractValuationData8(base_types._BaseFieldType):

	__slots__ = ["_CtrctVal", "_Dlta", "_TmStmp", "_Tp"]
	@property
	def CtrctVal(self):
		return self._CtrctVal

	@CtrctVal.setter
	def CtrctVal(self, value):
		self._CtrctVal = value if value is not None else base_types.UninitialisedField(self, 'CtrctVal', AmountAndDirection109, False)

	@CtrctVal.deleter
	def CtrctVal(self):
		del self._CtrctVal
		self._CtrctVal = base_types.UninitialisedField(self, 'CtrctVal', AmountAndDirection109, False)

	@property
	def Dlta(self):
		return self._Dlta

	@Dlta.setter
	def Dlta(self, value):
		self._Dlta = value if value is not None else base_types.UninitialisedField(self, 'Dlta', LongFraction19DecimalNumber, False)

	@Dlta.deleter
	def Dlta(self):
		del self._Dlta
		self._Dlta = base_types.UninitialisedField(self, 'Dlta', LongFraction19DecimalNumber, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ValuationType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ValuationType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctVal', type=AmountAndDirection109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dlta', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ValuationType1Code, min=0, max=1, mutex_group=None, array=False),
	))