from . import base_types
from ._CashCompensation1 import CashCompensation1
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._Price4 import Price4
from ._SecuritiesCompensation1 import SecuritiesCompensation1

class BuyIn2(base_types._BaseFieldType):

	__slots__ = ["_BuyInId", "_BuyInNtfctnId", "_Dt", "_Pric", "_ReqrdCshCompstn", "_SctiesBuyIn"]
	@property
	def BuyInId(self):
		return self._BuyInId

	@BuyInId.setter
	def BuyInId(self, value):
		self._BuyInId = value if type(value) != base_types.auto else self.make_default("BuyInId")

	@BuyInId.deleter
	def BuyInId(self):
		del self._BuyInId
		self._BuyInId = None

	@property
	def BuyInNtfctnId(self):
		return self._BuyInNtfctnId

	@BuyInNtfctnId.setter
	def BuyInNtfctnId(self, value):
		self._BuyInNtfctnId = value if type(value) != base_types.auto else self.make_default("BuyInNtfctnId")

	@BuyInNtfctnId.deleter
	def BuyInNtfctnId(self):
		del self._BuyInNtfctnId
		self._BuyInNtfctnId = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def ReqrdCshCompstn(self):
		return self._ReqrdCshCompstn

	@ReqrdCshCompstn.setter
	def ReqrdCshCompstn(self, value):
		self._ReqrdCshCompstn = value if type(value) != base_types.auto else self.make_default("ReqrdCshCompstn")

	@ReqrdCshCompstn.deleter
	def ReqrdCshCompstn(self):
		del self._ReqrdCshCompstn
		self._ReqrdCshCompstn = None

	@property
	def SctiesBuyIn(self):
		return self._SctiesBuyIn

	@SctiesBuyIn.setter
	def SctiesBuyIn(self, value):
		self._SctiesBuyIn = value if type(value) != base_types.auto else self.make_default("SctiesBuyIn")

	@SctiesBuyIn.deleter
	def SctiesBuyIn(self):
		del self._SctiesBuyIn
		self._SctiesBuyIn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdCshCompstn', type=CashCompensation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBuyIn', type=SecuritiesCompensation1, min=0, max=1, mutex_group=None, array=False),
	))

