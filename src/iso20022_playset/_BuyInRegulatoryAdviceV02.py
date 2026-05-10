from . import base_types
from ._BuyInAdviceDetails2 import BuyInAdviceDetails2
from ._PartyIdentification144 import PartyIdentification144
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SupplementaryData1 import SupplementaryData1

class BuyInRegulatoryAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BuyInAttrbts", "_SfkpgAcct", "_SplmtryData"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def BuyInAttrbts(self):
		return self._BuyInAttrbts

	@BuyInAttrbts.setter
	def BuyInAttrbts(self, value):
		self._BuyInAttrbts = value if type(value) != base_types.auto else self.make_default("BuyInAttrbts")

	@BuyInAttrbts.deleter
	def BuyInAttrbts(self):
		del self._BuyInAttrbts
		self._BuyInAttrbts = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInAttrbts', type=BuyInAdviceDetails2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

