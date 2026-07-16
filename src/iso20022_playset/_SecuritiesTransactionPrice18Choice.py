# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection107
from . import BaseOneRate
from . import DecimalNumber
from . import PercentageRate

class SecuritiesTransactionPrice18Choice(base_types._BaseFieldType):

	__slots__ = ["_BsisPts", "_Dcml", "_MntryVal", "_Pctg"]
	@property
	def BsisPts(self):
		return self._BsisPts

	@BsisPts.setter
	def BsisPts(self, value):
		self._BsisPts = value if value is not None else base_types.UninitialisedField(self, 'BsisPts', DecimalNumber, False)

	@BsisPts.deleter
	def BsisPts(self):
		del self._BsisPts
		self._BsisPts = base_types.UninitialisedField(self, 'BsisPts', DecimalNumber, False)

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
		self._MntryVal = value if value is not None else base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection107, False)

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = base_types.UninitialisedField(self, 'MntryVal', AmountAndDirection107, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dcml', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection107, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))