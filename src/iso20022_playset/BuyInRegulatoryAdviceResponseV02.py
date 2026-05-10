from . import base_types
from .BuyInAdviceDetails2 import BuyInAdviceDetails2
from .PartyIdentification144 import PartyIdentification144
from .Identification14 import Identification14
from .SupplementaryData1 import SupplementaryData1
from .ProcessingStatus79Choice import ProcessingStatus79Choice
from .SecuritiesAccount19 import SecuritiesAccount19

class BuyInRegulatoryAdviceResponseV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_BuyInAttrbts", "_AdvcRef", "_SfkpgAcct", "_AcctOwnr", "_PrcgSts"]
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
	def AdvcRef(self):
		return self._AdvcRef

	@AdvcRef.setter
	def AdvcRef(self, value):
		self._AdvcRef = value if type(value) != base_types.auto else self.make_default("AdvcRef")

	@AdvcRef.deleter
	def AdvcRef(self):
		del self._AdvcRef
		self._AdvcRef = None

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
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyInAttrbts', type=BuyInAdviceDetails2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvcRef', type=Identification14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus79Choice, min=1, max=1, mutex_group=None, array=False),
	))

