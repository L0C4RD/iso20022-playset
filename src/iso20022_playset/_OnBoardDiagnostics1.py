# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10NumberFraction2
from . import Max12NumericText
from . import Max35Text
from . import Max3NumericText
from . import Max4NumericText
from . import Max5NumericText
from . import Max6NumberFraction2

class OnBoardDiagnostics1(base_types._BaseFieldType):

	__slots__ = ["_BttryVltg", "_ChckNgnWrngSts", "_CoolntTmprtr", "_FuelEcnmy", "_FuelGaugeLvl", "_FuelTankLvlStart", "_HardAcclrtn", "_HardBrakg", "_NgnHrs", "_NgnIdleTm", "_NgnLd", "_NgnOilLifeRmng", "_NgnOilPrssr", "_NgnOilTmprtr", "_NgnRPM", "_NgnTtlIdleTm", "_NgnTtlTm", "_RfrgrtnHrs", "_RfrgrtnTmprtr"]
	@property
	def BttryVltg(self):
		return self._BttryVltg

	@BttryVltg.setter
	def BttryVltg(self, value):
		self._BttryVltg = value if value is not None else base_types.UninitialisedField(self, 'BttryVltg', Max4NumericText, False)

	@BttryVltg.deleter
	def BttryVltg(self):
		del self._BttryVltg
		self._BttryVltg = base_types.UninitialisedField(self, 'BttryVltg', Max4NumericText, False)

	@property
	def ChckNgnWrngSts(self):
		return self._ChckNgnWrngSts

	@ChckNgnWrngSts.setter
	def ChckNgnWrngSts(self, value):
		self._ChckNgnWrngSts = value if value is not None else base_types.UninitialisedField(self, 'ChckNgnWrngSts', Max35Text, False)

	@ChckNgnWrngSts.deleter
	def ChckNgnWrngSts(self):
		del self._ChckNgnWrngSts
		self._ChckNgnWrngSts = base_types.UninitialisedField(self, 'ChckNgnWrngSts', Max35Text, False)

	@property
	def CoolntTmprtr(self):
		return self._CoolntTmprtr

	@CoolntTmprtr.setter
	def CoolntTmprtr(self, value):
		self._CoolntTmprtr = value if value is not None else base_types.UninitialisedField(self, 'CoolntTmprtr', Max6NumberFraction2, False)

	@CoolntTmprtr.deleter
	def CoolntTmprtr(self):
		del self._CoolntTmprtr
		self._CoolntTmprtr = base_types.UninitialisedField(self, 'CoolntTmprtr', Max6NumberFraction2, False)

	@property
	def FuelEcnmy(self):
		return self._FuelEcnmy

	@FuelEcnmy.setter
	def FuelEcnmy(self, value):
		self._FuelEcnmy = value if value is not None else base_types.UninitialisedField(self, 'FuelEcnmy', Max6NumberFraction2, False)

	@FuelEcnmy.deleter
	def FuelEcnmy(self):
		del self._FuelEcnmy
		self._FuelEcnmy = base_types.UninitialisedField(self, 'FuelEcnmy', Max6NumberFraction2, False)

	@property
	def FuelGaugeLvl(self):
		return self._FuelGaugeLvl

	@FuelGaugeLvl.setter
	def FuelGaugeLvl(self, value):
		self._FuelGaugeLvl = value if value is not None else base_types.UninitialisedField(self, 'FuelGaugeLvl', Max4NumericText, False)

	@FuelGaugeLvl.deleter
	def FuelGaugeLvl(self):
		del self._FuelGaugeLvl
		self._FuelGaugeLvl = base_types.UninitialisedField(self, 'FuelGaugeLvl', Max4NumericText, False)

	@property
	def FuelTankLvlStart(self):
		return self._FuelTankLvlStart

	@FuelTankLvlStart.setter
	def FuelTankLvlStart(self, value):
		self._FuelTankLvlStart = value if value is not None else base_types.UninitialisedField(self, 'FuelTankLvlStart', Max4NumericText, False)

	@FuelTankLvlStart.deleter
	def FuelTankLvlStart(self):
		del self._FuelTankLvlStart
		self._FuelTankLvlStart = base_types.UninitialisedField(self, 'FuelTankLvlStart', Max4NumericText, False)

	@property
	def HardAcclrtn(self):
		return self._HardAcclrtn

	@HardAcclrtn.setter
	def HardAcclrtn(self, value):
		self._HardAcclrtn = value if value is not None else base_types.UninitialisedField(self, 'HardAcclrtn', Max4NumericText, False)

	@HardAcclrtn.deleter
	def HardAcclrtn(self):
		del self._HardAcclrtn
		self._HardAcclrtn = base_types.UninitialisedField(self, 'HardAcclrtn', Max4NumericText, False)

	@property
	def HardBrakg(self):
		return self._HardBrakg

	@HardBrakg.setter
	def HardBrakg(self, value):
		self._HardBrakg = value if value is not None else base_types.UninitialisedField(self, 'HardBrakg', Max4NumericText, False)

	@HardBrakg.deleter
	def HardBrakg(self):
		del self._HardBrakg
		self._HardBrakg = base_types.UninitialisedField(self, 'HardBrakg', Max4NumericText, False)

	@property
	def NgnHrs(self):
		return self._NgnHrs

	@NgnHrs.setter
	def NgnHrs(self, value):
		self._NgnHrs = value if value is not None else base_types.UninitialisedField(self, 'NgnHrs', Max10NumberFraction2, False)

	@NgnHrs.deleter
	def NgnHrs(self):
		del self._NgnHrs
		self._NgnHrs = base_types.UninitialisedField(self, 'NgnHrs', Max10NumberFraction2, False)

	@property
	def NgnIdleTm(self):
		return self._NgnIdleTm

	@NgnIdleTm.setter
	def NgnIdleTm(self, value):
		self._NgnIdleTm = value if value is not None else base_types.UninitialisedField(self, 'NgnIdleTm', Max10NumberFraction2, False)

	@NgnIdleTm.deleter
	def NgnIdleTm(self):
		del self._NgnIdleTm
		self._NgnIdleTm = base_types.UninitialisedField(self, 'NgnIdleTm', Max10NumberFraction2, False)

	@property
	def NgnLd(self):
		return self._NgnLd

	@NgnLd.setter
	def NgnLd(self, value):
		self._NgnLd = value if value is not None else base_types.UninitialisedField(self, 'NgnLd', Max12NumericText, False)

	@NgnLd.deleter
	def NgnLd(self):
		del self._NgnLd
		self._NgnLd = base_types.UninitialisedField(self, 'NgnLd', Max12NumericText, False)

	@property
	def NgnOilLifeRmng(self):
		return self._NgnOilLifeRmng

	@NgnOilLifeRmng.setter
	def NgnOilLifeRmng(self, value):
		self._NgnOilLifeRmng = value if value is not None else base_types.UninitialisedField(self, 'NgnOilLifeRmng', Max3NumericText, False)

	@NgnOilLifeRmng.deleter
	def NgnOilLifeRmng(self):
		del self._NgnOilLifeRmng
		self._NgnOilLifeRmng = base_types.UninitialisedField(self, 'NgnOilLifeRmng', Max3NumericText, False)

	@property
	def NgnOilPrssr(self):
		return self._NgnOilPrssr

	@NgnOilPrssr.setter
	def NgnOilPrssr(self, value):
		self._NgnOilPrssr = value if value is not None else base_types.UninitialisedField(self, 'NgnOilPrssr', Max3NumericText, False)

	@NgnOilPrssr.deleter
	def NgnOilPrssr(self):
		del self._NgnOilPrssr
		self._NgnOilPrssr = base_types.UninitialisedField(self, 'NgnOilPrssr', Max3NumericText, False)

	@property
	def NgnOilTmprtr(self):
		return self._NgnOilTmprtr

	@NgnOilTmprtr.setter
	def NgnOilTmprtr(self, value):
		self._NgnOilTmprtr = value if value is not None else base_types.UninitialisedField(self, 'NgnOilTmprtr', Max6NumberFraction2, False)

	@NgnOilTmprtr.deleter
	def NgnOilTmprtr(self):
		del self._NgnOilTmprtr
		self._NgnOilTmprtr = base_types.UninitialisedField(self, 'NgnOilTmprtr', Max6NumberFraction2, False)

	@property
	def NgnRPM(self):
		return self._NgnRPM

	@NgnRPM.setter
	def NgnRPM(self, value):
		self._NgnRPM = value if value is not None else base_types.UninitialisedField(self, 'NgnRPM', Max5NumericText, False)

	@NgnRPM.deleter
	def NgnRPM(self):
		del self._NgnRPM
		self._NgnRPM = base_types.UninitialisedField(self, 'NgnRPM', Max5NumericText, False)

	@property
	def NgnTtlIdleTm(self):
		return self._NgnTtlIdleTm

	@NgnTtlIdleTm.setter
	def NgnTtlIdleTm(self, value):
		self._NgnTtlIdleTm = value if value is not None else base_types.UninitialisedField(self, 'NgnTtlIdleTm', Max10NumberFraction2, False)

	@NgnTtlIdleTm.deleter
	def NgnTtlIdleTm(self):
		del self._NgnTtlIdleTm
		self._NgnTtlIdleTm = base_types.UninitialisedField(self, 'NgnTtlIdleTm', Max10NumberFraction2, False)

	@property
	def NgnTtlTm(self):
		return self._NgnTtlTm

	@NgnTtlTm.setter
	def NgnTtlTm(self, value):
		self._NgnTtlTm = value if value is not None else base_types.UninitialisedField(self, 'NgnTtlTm', Max6NumberFraction2, False)

	@NgnTtlTm.deleter
	def NgnTtlTm(self):
		del self._NgnTtlTm
		self._NgnTtlTm = base_types.UninitialisedField(self, 'NgnTtlTm', Max6NumberFraction2, False)

	@property
	def RfrgrtnHrs(self):
		return self._RfrgrtnHrs

	@RfrgrtnHrs.setter
	def RfrgrtnHrs(self, value):
		self._RfrgrtnHrs = value if value is not None else base_types.UninitialisedField(self, 'RfrgrtnHrs', Max10NumberFraction2, False)

	@RfrgrtnHrs.deleter
	def RfrgrtnHrs(self):
		del self._RfrgrtnHrs
		self._RfrgrtnHrs = base_types.UninitialisedField(self, 'RfrgrtnHrs', Max10NumberFraction2, False)

	@property
	def RfrgrtnTmprtr(self):
		return self._RfrgrtnTmprtr

	@RfrgrtnTmprtr.setter
	def RfrgrtnTmprtr(self, value):
		self._RfrgrtnTmprtr = value if value is not None else base_types.UninitialisedField(self, 'RfrgrtnTmprtr', Max6NumberFraction2, False)

	@RfrgrtnTmprtr.deleter
	def RfrgrtnTmprtr(self):
		del self._RfrgrtnTmprtr
		self._RfrgrtnTmprtr = base_types.UninitialisedField(self, 'RfrgrtnTmprtr', Max6NumberFraction2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BttryVltg', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckNgnWrngSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoolntTmprtr', type=Max6NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelEcnmy', type=Max6NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelGaugeLvl', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FuelTankLvlStart', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HardAcclrtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HardBrakg', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnHrs', type=Max10NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnIdleTm', type=Max10NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnLd', type=Max12NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnOilLifeRmng', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnOilPrssr', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnOilTmprtr', type=Max6NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnRPM', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnTtlIdleTm', type=Max10NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgnTtlTm', type=Max6NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrgrtnHrs', type=Max10NumberFraction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrgrtnTmprtr', type=Max6NumberFraction2, min=0, max=1, mutex_group=None, array=False),
	))