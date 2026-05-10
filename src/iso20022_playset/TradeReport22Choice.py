from . import base_types
from .TradeTransactionCollateralUpdate8 import TradeTransactionCollateralUpdate8
from .TradeTransactionCorrection13 import TradeTransactionCorrection13
from .TradeNewTransaction13 import TradeNewTransaction13
from .TradeTransactionPositionComponent8 import TradeTransactionPositionComponent8
from .TradeValuationUpdate9 import TradeValuationUpdate9
from .TradeError9 import TradeError9

class TradeReport22Choice(base_types._BaseFieldType):

	__slots__ = ["_EarlyTermntn", "_CollUpd", "_Crrctn", "_Err", "_Mod", "_PosCmpnt", "_ValtnUpd", "_New"]
	@property
	def EarlyTermntn(self):
		return self._EarlyTermntn

	@EarlyTermntn.setter
	def EarlyTermntn(self, value):
		self._EarlyTermntn = value if type(value) != base_types.auto else self.make_default("EarlyTermntn")

	@EarlyTermntn.deleter
	def EarlyTermntn(self):
		del self._EarlyTermntn
		self._EarlyTermntn = None

	@property
	def CollUpd(self):
		return self._CollUpd

	@CollUpd.setter
	def CollUpd(self, value):
		self._CollUpd = value if type(value) != base_types.auto else self.make_default("CollUpd")

	@CollUpd.deleter
	def CollUpd(self):
		del self._CollUpd
		self._CollUpd = None

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if type(value) != base_types.auto else self.make_default("Crrctn")

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = None

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != base_types.auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def PosCmpnt(self):
		return self._PosCmpnt

	@PosCmpnt.setter
	def PosCmpnt(self, value):
		self._PosCmpnt = value if type(value) != base_types.auto else self.make_default("PosCmpnt")

	@PosCmpnt.deleter
	def PosCmpnt(self):
		del self._PosCmpnt
		self._PosCmpnt = None

	@property
	def ValtnUpd(self):
		return self._ValtnUpd

	@ValtnUpd.setter
	def ValtnUpd(self, value):
		self._ValtnUpd = value if type(value) != base_types.auto else self.make_default("ValtnUpd")

	@ValtnUpd.deleter
	def ValtnUpd(self):
		del self._ValtnUpd
		self._ValtnUpd = None

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != base_types.auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EarlyTermntn', type=TradeError9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollUpd', type=TradeTransactionCollateralUpdate8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=TradeTransactionCorrection13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=TradeError9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=TradeTransactionCorrection13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PosCmpnt', type=TradeTransactionPositionComponent8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValtnUpd', type=TradeValuationUpdate9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=TradeNewTransaction13, min=0, max=1, mutex_group=1, array=False),
	))

