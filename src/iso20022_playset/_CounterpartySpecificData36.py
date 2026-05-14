# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContractValuationData8 import ContractValuationData8
from ._ISODateTime import ISODateTime
from ._TradeCounterpartyReport20 import TradeCounterpartyReport20

class CounterpartySpecificData36(base_types._BaseFieldType):

	__slots__ = ["_CtrPty", "_RptgTmStmp", "_Valtn"]
	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != base_types.auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	@property
	def RptgTmStmp(self):
		return self._RptgTmStmp

	@RptgTmStmp.setter
	def RptgTmStmp(self, value):
		self._RptgTmStmp = value if type(value) != base_types.auto else self.make_default("RptgTmStmp")

	@RptgTmStmp.deleter
	def RptgTmStmp(self):
		del self._RptgTmStmp
		self._RptgTmStmp = None

	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if type(value) != base_types.auto else self.make_default("Valtn")

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPty', type=TradeCounterpartyReport20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Valtn', type=ContractValuationData8, min=0, max=1, mutex_group=None, array=False),
	))