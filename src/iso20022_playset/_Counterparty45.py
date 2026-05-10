from . import base_types
from ._PartyIdentification248Choice import PartyIdentification248Choice
from ._Direction4Choice import Direction4Choice
from ._ReportingExemption1 import ReportingExemption1
from ._CountryCode import CountryCode
from ._TradingCapacity7Code import TradingCapacity7Code
from ._CounterpartyTradeNature15Choice import CounterpartyTradeNature15Choice

class Counterparty45(base_types._BaseFieldType):

	__slots__ = ["_Id", "_DrctnOrSd", "_TradrLctn", "_BookgLctn", "_Ntr", "_TradgCpcty", "_RptgXmptn"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def DrctnOrSd(self):
		return self._DrctnOrSd

	@DrctnOrSd.setter
	def DrctnOrSd(self, value):
		self._DrctnOrSd = value if type(value) != base_types.auto else self.make_default("DrctnOrSd")

	@DrctnOrSd.deleter
	def DrctnOrSd(self):
		del self._DrctnOrSd
		self._DrctnOrSd = None

	@property
	def TradrLctn(self):
		return self._TradrLctn

	@TradrLctn.setter
	def TradrLctn(self, value):
		self._TradrLctn = value if type(value) != base_types.auto else self.make_default("TradrLctn")

	@TradrLctn.deleter
	def TradrLctn(self):
		del self._TradrLctn
		self._TradrLctn = None

	@property
	def BookgLctn(self):
		return self._BookgLctn

	@BookgLctn.setter
	def BookgLctn(self, value):
		self._BookgLctn = value if type(value) != base_types.auto else self.make_default("BookgLctn")

	@BookgLctn.deleter
	def BookgLctn(self):
		del self._BookgLctn
		self._BookgLctn = None

	@property
	def Ntr(self):
		return self._Ntr

	@Ntr.setter
	def Ntr(self, value):
		self._Ntr = value if type(value) != base_types.auto else self.make_default("Ntr")

	@Ntr.deleter
	def Ntr(self):
		del self._Ntr
		self._Ntr = None

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != base_types.auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	@property
	def RptgXmptn(self):
		return self._RptgXmptn

	@RptgXmptn.setter
	def RptgXmptn(self, value):
		self._RptgXmptn = value if type(value) != base_types.auto else self.make_default("RptgXmptn")

	@RptgXmptn.deleter
	def RptgXmptn(self):
		del self._RptgXmptn
		self._RptgXmptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification248Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctnOrSd', type=Direction4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradrLctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookgLctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntr', type=CounterpartyTradeNature15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgXmptn', type=ReportingExemption1, min=0, max=1, mutex_group=None, array=False),
	))

