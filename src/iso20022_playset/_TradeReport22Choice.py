# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeError9
from . import TradeNewTransaction13
from . import TradeTransactionCollateralUpdate8
from . import TradeTransactionCorrection13
from . import TradeTransactionPositionComponent8
from . import TradeValuationUpdate9

class TradeReport22Choice(base_types._BaseFieldType):

	__slots__ = ["_CollUpd", "_Crrctn", "_EarlyTermntn", "_Err", "_Mod", "_New", "_PosCmpnt", "_ValtnUpd"]
	@property
	def CollUpd(self):
		return self._CollUpd

	@CollUpd.setter
	def CollUpd(self, value):
		self._CollUpd = value if value is not None else base_types.UninitialisedField(self, 'CollUpd', TradeTransactionCollateralUpdate8, False)

	@CollUpd.deleter
	def CollUpd(self):
		del self._CollUpd
		self._CollUpd = base_types.UninitialisedField(self, 'CollUpd', TradeTransactionCollateralUpdate8, False)

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', TradeTransactionCorrection13, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', TradeTransactionCorrection13, False)

	@property
	def EarlyTermntn(self):
		return self._EarlyTermntn

	@EarlyTermntn.setter
	def EarlyTermntn(self, value):
		self._EarlyTermntn = value if value is not None else base_types.UninitialisedField(self, 'EarlyTermntn', TradeError9, False)

	@EarlyTermntn.deleter
	def EarlyTermntn(self):
		del self._EarlyTermntn
		self._EarlyTermntn = base_types.UninitialisedField(self, 'EarlyTermntn', TradeError9, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', TradeError9, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', TradeError9, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', TradeTransactionCorrection13, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', TradeTransactionCorrection13, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', TradeNewTransaction13, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', TradeNewTransaction13, False)

	@property
	def PosCmpnt(self):
		return self._PosCmpnt

	@PosCmpnt.setter
	def PosCmpnt(self, value):
		self._PosCmpnt = value if value is not None else base_types.UninitialisedField(self, 'PosCmpnt', TradeTransactionPositionComponent8, False)

	@PosCmpnt.deleter
	def PosCmpnt(self):
		del self._PosCmpnt
		self._PosCmpnt = base_types.UninitialisedField(self, 'PosCmpnt', TradeTransactionPositionComponent8, False)

	@property
	def ValtnUpd(self):
		return self._ValtnUpd

	@ValtnUpd.setter
	def ValtnUpd(self, value):
		self._ValtnUpd = value if value is not None else base_types.UninitialisedField(self, 'ValtnUpd', TradeValuationUpdate9, False)

	@ValtnUpd.deleter
	def ValtnUpd(self):
		del self._ValtnUpd
		self._ValtnUpd = base_types.UninitialisedField(self, 'ValtnUpd', TradeValuationUpdate9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollUpd', type=TradeTransactionCollateralUpdate8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=TradeTransactionCorrection13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EarlyTermntn', type=TradeError9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=TradeError9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=TradeTransactionCorrection13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=TradeNewTransaction13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PosCmpnt', type=TradeTransactionPositionComponent8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ValtnUpd', type=TradeValuationUpdate9, min=0, max=1, mutex_group=1, array=False),
	))