# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BasketIdentificationAndEligibilitySetProfile1
from . import CollateralAmount16
from . import CollateralParties11
from . import CollateralStatus1Code
from . import OptionType6Choice
from . import PercentageRate
from . import RepoTerminationOption1Code

class CounterpartyAggregation3(base_types._BaseFieldType):

	__slots__ = ["_BsktIdAndElgbltySetPrfl", "_CollPties", "_GblCtrPtySts", "_MrgnRate", "_OptnTp", "_TermntnOptn", "_ValtnAmts"]
	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties11, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties11, False)

	@property
	def GblCtrPtySts(self):
		return self._GblCtrPtySts

	@GblCtrPtySts.setter
	def GblCtrPtySts(self, value):
		self._GblCtrPtySts = value if value is not None else base_types.UninitialisedField(self, 'GblCtrPtySts', CollateralStatus1Code, False)

	@GblCtrPtySts.deleter
	def GblCtrPtySts(self):
		del self._GblCtrPtySts
		self._GblCtrPtySts = base_types.UninitialisedField(self, 'GblCtrPtySts', CollateralStatus1Code, False)

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if value is not None else base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if value is not None else base_types.UninitialisedField(self, 'TermntnOptn', RepoTerminationOption1Code, False)

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = base_types.UninitialisedField(self, 'TermntnOptn', RepoTerminationOption1Code, False)

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount16, True)

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount16, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCtrPtySts', type=CollateralStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount16, min=1, max=None, mutex_group=None, array=True),
	))