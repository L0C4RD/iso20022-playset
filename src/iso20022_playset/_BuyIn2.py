# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashCompensation1
from . import ISODate
from . import Max35Text
from . import Price4
from . import SecuritiesCompensation1

class BuyIn2(base_types._BaseFieldType):

	__slots__ = ["_BuyInId", "_BuyInNtfctnId", "_Dt", "_Pric", "_ReqrdCshCompstn", "_SctiesBuyIn"]
	@property
	def BuyInId(self):
		return self._BuyInId

	@BuyInId.setter
	def BuyInId(self, value):
		self._BuyInId = value if value is not None else base_types.UninitialisedField(self, 'BuyInId', Max35Text, False)

	@BuyInId.deleter
	def BuyInId(self):
		del self._BuyInId
		self._BuyInId = base_types.UninitialisedField(self, 'BuyInId', Max35Text, False)

	@property
	def BuyInNtfctnId(self):
		return self._BuyInNtfctnId

	@BuyInNtfctnId.setter
	def BuyInNtfctnId(self, value):
		self._BuyInNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'BuyInNtfctnId', Max35Text, False)

	@BuyInNtfctnId.deleter
	def BuyInNtfctnId(self):
		del self._BuyInNtfctnId
		self._BuyInNtfctnId = base_types.UninitialisedField(self, 'BuyInNtfctnId', Max35Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', Price4, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', Price4, False)

	@property
	def ReqrdCshCompstn(self):
		return self._ReqrdCshCompstn

	@ReqrdCshCompstn.setter
	def ReqrdCshCompstn(self, value):
		self._ReqrdCshCompstn = value if value is not None else base_types.UninitialisedField(self, 'ReqrdCshCompstn', CashCompensation1, False)

	@ReqrdCshCompstn.deleter
	def ReqrdCshCompstn(self):
		del self._ReqrdCshCompstn
		self._ReqrdCshCompstn = base_types.UninitialisedField(self, 'ReqrdCshCompstn', CashCompensation1, False)

	@property
	def SctiesBuyIn(self):
		return self._SctiesBuyIn

	@SctiesBuyIn.setter
	def SctiesBuyIn(self, value):
		self._SctiesBuyIn = value if value is not None else base_types.UninitialisedField(self, 'SctiesBuyIn', SecuritiesCompensation1, False)

	@SctiesBuyIn.deleter
	def SctiesBuyIn(self):
		del self._SctiesBuyIn
		self._SctiesBuyIn = base_types.UninitialisedField(self, 'SctiesBuyIn', SecuritiesCompensation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdCshCompstn', type=CashCompensation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBuyIn', type=SecuritiesCompensation1, min=0, max=1, mutex_group=None, array=False),
	))