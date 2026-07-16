# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractValuationData8
from . import ISODateTime
from . import TradeCounterpartyReport20

class CounterpartySpecificData36(base_types._BaseFieldType):

	__slots__ = ["_CtrPty", "_RptgTmStmp", "_Valtn"]
	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', TradeCounterpartyReport20, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', TradeCounterpartyReport20, False)

	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if value is not None else base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = base_types.UninitialisedField(self, 'RptgTmStmp', ISODateTime, False)

	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if value is not None else base_types.UninitialisedField(self, 'Valtn', ContractValuationData8, False)

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = base_types.UninitialisedField(self, 'Valtn', ContractValuationData8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPty', type=TradeCounterpartyReport20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Valtn', type=ContractValuationData8, min=0, max=1, mutex_group=None, array=False),
	))