import base_types
import MarginCollateralReport4
import TradeCounterpartyReport20
import ActiveOrHistoricCurrencyCode

class PositionSetCollateralDimensions3(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnPstdCcy", "_CtrPtyId", "_XcssCollPstdCcy", "_InitlMrgnRcvdCcy", "_XcssCollRcvdCcy", "_VartnMrgnPstdCcy", "_VartnMrgnRcvdCcy", "_Coll"]
	@property
	def InitlMrgnPstdCcy(self):
		return self._InitlMrgnPstdCcy

	@InitlMrgnPstdCcy.setter
	def InitlMrgnPstdCcy(self, value):
		self._InitlMrgnPstdCcy = value if type(value) != auto else self.make_default("InitlMrgnPstdCcy")

	@InitlMrgnPstdCcy.deleter
	def InitlMrgnPstdCcy(self):
		del self._InitlMrgnPstdCcy
		self._InitlMrgnPstdCcy = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def XcssCollPstdCcy(self):
		return self._XcssCollPstdCcy

	@XcssCollPstdCcy.setter
	def XcssCollPstdCcy(self, value):
		self._XcssCollPstdCcy = value if type(value) != auto else self.make_default("XcssCollPstdCcy")

	@XcssCollPstdCcy.deleter
	def XcssCollPstdCcy(self):
		del self._XcssCollPstdCcy
		self._XcssCollPstdCcy = None

	@property
	def InitlMrgnRcvdCcy(self):
		return self._InitlMrgnRcvdCcy

	@InitlMrgnRcvdCcy.setter
	def InitlMrgnRcvdCcy(self, value):
		self._InitlMrgnRcvdCcy = value if type(value) != auto else self.make_default("InitlMrgnRcvdCcy")

	@InitlMrgnRcvdCcy.deleter
	def InitlMrgnRcvdCcy(self):
		del self._InitlMrgnRcvdCcy
		self._InitlMrgnRcvdCcy = None

	@property
	def XcssCollRcvdCcy(self):
		return self._XcssCollRcvdCcy

	@XcssCollRcvdCcy.setter
	def XcssCollRcvdCcy(self, value):
		self._XcssCollRcvdCcy = value if type(value) != auto else self.make_default("XcssCollRcvdCcy")

	@XcssCollRcvdCcy.deleter
	def XcssCollRcvdCcy(self):
		del self._XcssCollRcvdCcy
		self._XcssCollRcvdCcy = None

	@property
	def VartnMrgnPstdCcy(self):
		return self._VartnMrgnPstdCcy

	@VartnMrgnPstdCcy.setter
	def VartnMrgnPstdCcy(self, value):
		self._VartnMrgnPstdCcy = value if type(value) != auto else self.make_default("VartnMrgnPstdCcy")

	@VartnMrgnPstdCcy.deleter
	def VartnMrgnPstdCcy(self):
		del self._VartnMrgnPstdCcy
		self._VartnMrgnPstdCcy = None

	@property
	def VartnMrgnRcvdCcy(self):
		return self._VartnMrgnRcvdCcy

	@VartnMrgnRcvdCcy.setter
	def VartnMrgnRcvdCcy(self, value):
		self._VartnMrgnRcvdCcy = value if type(value) != auto else self.make_default("VartnMrgnRcvdCcy")

	@VartnMrgnRcvdCcy.deleter
	def VartnMrgnRcvdCcy(self):
		del self._VartnMrgnRcvdCcy
		self._VartnMrgnRcvdCcy = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=TradeCounterpartyReport20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=MarginCollateralReport4, min=0, max=1, mutex_group=None, array=False),
	))

