# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import MarginCollateralReport4
from . import TradeCounterpartyReport20

class PositionSetCollateralDimensions3(base_types._BaseFieldType):

	__slots__ = ["_Coll", "_CtrPtyId", "_InitlMrgnPstdCcy", "_InitlMrgnRcvdCcy", "_VartnMrgnPstdCcy", "_VartnMrgnRcvdCcy", "_XcssCollPstdCcy", "_XcssCollRcvdCcy"]
	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', MarginCollateralReport4, False)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', MarginCollateralReport4, False)

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', TradeCounterpartyReport20, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', TradeCounterpartyReport20, False)

	@property
	def InitlMrgnPstdCcy(self):
		return self._InitlMrgnPstdCcy

	@InitlMrgnPstdCcy.setter
	def InitlMrgnPstdCcy(self, value):
		self._InitlMrgnPstdCcy = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@InitlMrgnPstdCcy.deleter
	def InitlMrgnPstdCcy(self):
		del self._InitlMrgnPstdCcy
		self._InitlMrgnPstdCcy = base_types.UninitialisedField(self, 'InitlMrgnPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def InitlMrgnRcvdCcy(self):
		return self._InitlMrgnRcvdCcy

	@InitlMrgnRcvdCcy.setter
	def InitlMrgnRcvdCcy(self, value):
		self._InitlMrgnRcvdCcy = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	@InitlMrgnRcvdCcy.deleter
	def InitlMrgnRcvdCcy(self):
		del self._InitlMrgnRcvdCcy
		self._InitlMrgnRcvdCcy = base_types.UninitialisedField(self, 'InitlMrgnRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def VartnMrgnPstdCcy(self):
		return self._VartnMrgnPstdCcy

	@VartnMrgnPstdCcy.setter
	def VartnMrgnPstdCcy(self, value):
		self._VartnMrgnPstdCcy = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@VartnMrgnPstdCcy.deleter
	def VartnMrgnPstdCcy(self):
		del self._VartnMrgnPstdCcy
		self._VartnMrgnPstdCcy = base_types.UninitialisedField(self, 'VartnMrgnPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def VartnMrgnRcvdCcy(self):
		return self._VartnMrgnRcvdCcy

	@VartnMrgnRcvdCcy.setter
	def VartnMrgnRcvdCcy(self, value):
		self._VartnMrgnRcvdCcy = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	@VartnMrgnRcvdCcy.deleter
	def VartnMrgnRcvdCcy(self):
		del self._VartnMrgnRcvdCcy
		self._VartnMrgnRcvdCcy = base_types.UninitialisedField(self, 'VartnMrgnRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def XcssCollPstdCcy(self):
		return self._XcssCollPstdCcy

	@XcssCollPstdCcy.setter
	def XcssCollPstdCcy(self, value):
		self._XcssCollPstdCcy = value if value is not None else base_types.UninitialisedField(self, 'XcssCollPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@XcssCollPstdCcy.deleter
	def XcssCollPstdCcy(self):
		del self._XcssCollPstdCcy
		self._XcssCollPstdCcy = base_types.UninitialisedField(self, 'XcssCollPstdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def XcssCollRcvdCcy(self):
		return self._XcssCollRcvdCcy

	@XcssCollRcvdCcy.setter
	def XcssCollRcvdCcy(self, value):
		self._XcssCollRcvdCcy = value if value is not None else base_types.UninitialisedField(self, 'XcssCollRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	@XcssCollRcvdCcy.deleter
	def XcssCollRcvdCcy(self):
		del self._XcssCollRcvdCcy
		self._XcssCollRcvdCcy = base_types.UninitialisedField(self, 'XcssCollRcvdCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coll', type=MarginCollateralReport4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=TradeCounterpartyReport20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))