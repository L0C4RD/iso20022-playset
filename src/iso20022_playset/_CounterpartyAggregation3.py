from . import base_types
from .BasketIdentificationAndEligibilitySetProfile1 import BasketIdentificationAndEligibilitySetProfile1
from .CollateralAmount16 import CollateralAmount16
from .RepoTerminationOption1Code import RepoTerminationOption1Code
from .CollateralStatus1Code import CollateralStatus1Code
from .PercentageRate import PercentageRate
from .CollateralParties11 import CollateralParties11
from .OptionType6Choice import OptionType6Choice

class CounterpartyAggregation3(base_types._BaseFieldType):

	__slots__ = ["_ValtnAmts", "_CollPties", "_TermntnOptn", "_OptnTp", "_BsktIdAndElgbltySetPrfl", "_MrgnRate", "_GblCtrPtySts"]
	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if type(value) != base_types.auto else self.make_default("ValtnAmts")

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = None

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if type(value) != base_types.auto else self.make_default("CollPties")

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = None

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if type(value) != base_types.auto else self.make_default("TermntnOptn")

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("BsktIdAndElgbltySetPrfl")

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = None

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if type(value) != base_types.auto else self.make_default("MrgnRate")

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = None

	@property
	def GblCtrPtySts(self):
		return self._GblCtrPtySts

	@GblCtrPtySts.setter
	def GblCtrPtySts(self, value):
		self._GblCtrPtySts = value if type(value) != base_types.auto else self.make_default("GblCtrPtySts")

	@GblCtrPtySts.deleter
	def GblCtrPtySts(self):
		del self._GblCtrPtySts
		self._GblCtrPtySts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollPties', type=CollateralParties11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCtrPtySts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))

