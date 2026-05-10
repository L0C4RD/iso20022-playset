import base_types
import CollateralMarginMarginUpdate5
import CollateralMarginError4
import CollateralMarginCorrection6

class TradeReport21Choice(base_types._BaseFieldType):

	__slots__ = ["_New", "_Err", "_Crrctn", "_TradUpd"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if type(value) != auto else self.make_default("Crrctn")

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = None

	@property
	def TradUpd(self):
		return self._TradUpd

	@TradUpd.setter
	def TradUpd(self, value):
		self._TradUpd = value if type(value) != auto else self.make_default("TradUpd")

	@TradUpd.deleter
	def TradUpd(self):
		del self._TradUpd
		self._TradUpd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=CollateralMarginCorrection6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=CollateralMarginError4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=CollateralMarginCorrection6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradUpd', type=CollateralMarginMarginUpdate5, min=0, max=1, mutex_group=1, array=False),
	))

