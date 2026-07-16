# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection106
from . import BaseOneRate
from . import LongFraction19DecimalNumber
from . import PercentageRate
from . import SecuritiesTransactionPrice5

class SecuritiesTransactionPrice23Choice(base_types._BaseFieldType):

	__slots__ = ["_Dcml", "_MntryVal", "_Othr", "_Pctg", "_Unit", "_Yld"]
	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if value is not None else base_types.UninitialisedField(self, 'Dcml', BaseOneRate, False)

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = base_types.UninitialisedField(self, 'Dcml', BaseOneRate, False)

	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if value is not None else base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection106, False)

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection106, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', SecuritiesTransactionPrice5, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', SecuritiesTransactionPrice5, False)

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if value is not None else base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', LongFraction19DecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', LongFraction19DecimalNumber, False)

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if value is not None else base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dcml', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection106, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=SecuritiesTransactionPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))