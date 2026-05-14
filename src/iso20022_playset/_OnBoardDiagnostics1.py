# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max10NumberFraction2 import Max10NumberFraction2
from ._Max12NumericText import Max12NumericText
from ._Max35Text import Max35Text
from ._Max3NumericText import Max3NumericText
from ._Max4NumericText import Max4NumericText
from ._Max5NumericText import Max5NumericText
from ._Max6NumberFraction2 import Max6NumberFraction2

class OnBoardDiagnostics1(base_types._BaseFieldType):

	__slots__ = ["_BttryVltg", "_ChckNgnWrngSts", "_CoolntTmprtr", "_FuelEcnmy", "_FuelGaugeLvl", "_FuelTankLvlStart", "_HardAcclrtn", "_HardBrakg", "_NgnHrs", "_NgnIdleTm", "_NgnLd", "_NgnOilLifeRmng", "_NgnOilPrssr", "_NgnOilTmprtr", "_NgnRPM", "_NgnTtlIdleTm", "_NgnTtlTm", "_RfrgrtnHrs", "_RfrgrtnTmprtr"]
	@property
	def BttryVltg(self):
		return self._BttryVltg

	@BttryVltg.setter
	def BttryVltg(self, value):
		self._BttryVltg = value if type(value) != base_types.auto else self.make_default("BttryVltg")

	@BttryVltg.deleter
	def BttryVltg(self):
		del self._BttryVltg
		self._BttryVltg = None

	@property
	def ChckNgnWrngSts(self):
		return self._ChckNgnWrngSts

	@ChckNgnWrngSts.setter
	def ChckNgnWrngSts(self, value):
		self._ChckNgnWrngSts = value if type(value) != base_types.auto else self.make_default("ChckNgnWrngSts")

	@ChckNgnWrngSts.deleter
	def ChckNgnWrngSts(self):
		del self._ChckNgnWrngSts
		self._ChckNgnWrngSts = None

	@property
	def CoolntTmprtr(self):
		return self._CoolntTmprtr

	@CoolntTmprtr.setter
	def CoolntTmprtr(self, value):
		self._CoolntTmprtr = value if type(value) != base_types.auto else self.make_default("CoolntTmprtr")

	@CoolntTmprtr.deleter
	def CoolntTmprtr(self):
		del self._CoolntTmprtr
		self._CoolntTmprtr = None

	@property
	def FuelEcnmy(self):
		return self._FuelEcnmy

	@FuelEcnmy.setter
	def FuelEcnmy(self, value):
		self._FuelEcnmy = value if type(value) != base_types.auto else self.make_default("FuelEcnmy")

	@FuelEcnmy.deleter
	def FuelEcnmy(self):
		del self._FuelEcnmy
		self._FuelEcnmy = None

	@property
	def FuelGaugeLvl(self):
		return self._FuelGaugeLvl

	@FuelGaugeLvl.setter
	def FuelGaugeLvl(self, value):
		self._FuelGaugeLvl = value if type(value) != base_types.auto else self.make_default("FuelGaugeLvl")

	@FuelGaugeLvl.deleter
	def FuelGaugeLvl(self):
		del self._FuelGaugeLvl
		self._FuelGaugeLvl = None

	@property
	def FuelTankLvlStart(self):
		return self._FuelTankLvlStart

	@FuelTankLvlStart.setter
	def FuelTankLvlStart(self, value):
		self._FuelTankLvlStart = value if type(value) != base_types.auto else self.make_default("FuelTankLvlStart")

	@FuelTankLvlStart.deleter
	def FuelTankLvlStart(self):
		del self._FuelTankLvlStart
		self._FuelTankLvlStart = None

	@property
	def HardAcclrtn(self):
		return self._HardAcclrtn

	@HardAcclrtn.setter
	def HardAcclrtn(self, value):
		self._HardAcclrtn = value if type(value) != base_types.auto else self.make_default("HardAcclrtn")

	@HardAcclrtn.deleter
	def HardAcclrtn(self):
		del self._HardAcclrtn
		self._HardAcclrtn = None

	@property
	def HardBrakg(self):
		return self._HardBrakg

	@HardBrakg.setter
	def HardBrakg(self, value):
		self._HardBrakg = value if type(value) != base_types.auto else self.make_default("HardBrakg")

	@HardBrakg.deleter
	def HardBrakg(self):
		del self._HardBrakg
		self._HardBrakg = None

	@property
	def NgnHrs(self):
		return self._NgnHrs

	@NgnHrs.setter
	def NgnHrs(self, value):
		self._NgnHrs = value if type(value) != base_types.auto else self.make_default("NgnHrs")

	@NgnHrs.deleter
	def NgnHrs(self):
		del self._NgnHrs
		self._NgnHrs = None

	@property
	def NgnIdleTm(self):
		return self._NgnIdleTm

	@NgnIdleTm.setter
	def NgnIdleTm(self, value):
		self._NgnIdleTm = value if type(value) != base_types.auto else self.make_default("NgnIdleTm")

	@NgnIdleTm.deleter
	def NgnIdleTm(self):
		del self._NgnIdleTm
		self._NgnIdleTm = None

	@property
	def NgnLd(self):
		return self._NgnLd

	@NgnLd.setter
	def NgnLd(self, value):
		self._NgnLd = value if type(value) != base_types.auto else self.make_default("NgnLd")

	@NgnLd.deleter
	def NgnLd(self):
		del self._NgnLd
		self._NgnLd = None

	@property
	def NgnOilLifeRmng(self):
		return self._NgnOilLifeRmng

	@NgnOilLifeRmng.setter
	def NgnOilLifeRmng(self, value):
		self._NgnOilLifeRmng = value if type(value) != base_types.auto else self.make_default("NgnOilLifeRmng")

	@NgnOilLifeRmng.deleter
	def NgnOilLifeRmng(self):
		del self._NgnOilLifeRmng
		self._NgnOilLifeRmng = None

	@property
	def NgnOilPrssr(self):
		return self._NgnOilPrssr

	@NgnOilPrssr.setter
	def NgnOilPrssr(self, value):
		self._NgnOilPrssr = value if type(value) != base_types.auto else self.make_default("NgnOilPrssr")

	@NgnOilPrssr.deleter
	def NgnOilPrssr(self):
		del self._NgnOilPrssr
		self._NgnOilPrssr = None

	@property
	def NgnOilTmprtr(self):
		return self._NgnOilTmprtr

	@NgnOilTmprtr.setter
	def NgnOilTmprtr(self, value):
		self._NgnOilTmprtr = value if type(value) != base_types.auto else self.make_default("NgnOilTmprtr")

	@NgnOilTmprtr.deleter
	def NgnOilTmprtr(self):
		del self._NgnOilTmprtr
		self._NgnOilTmprtr = None

	@property
	def NgnRPM(self):
		return self._NgnRPM

	@NgnRPM.setter
	def NgnRPM(self, value):
		self._NgnRPM = value if type(value) != base_types.auto else self.make_default("NgnRPM")

	@NgnRPM.deleter
	def NgnRPM(self):
		del self._NgnRPM
		self._NgnRPM = None

	@property
	def NgnTtlIdleTm(self):
		return self._NgnTtlIdleTm

	@NgnTtlIdleTm.setter
	def NgnTtlIdleTm(self, value):
		self._NgnTtlIdleTm = value if type(value) != base_types.auto else self.make_default("NgnTtlIdleTm")

	@NgnTtlIdleTm.deleter
	def NgnTtlIdleTm(self):
		del self._NgnTtlIdleTm
		self._NgnTtlIdleTm = None

	@property
	def NgnTtlTm(self):
		return self._NgnTtlTm

	@NgnTtlTm.setter
	def NgnTtlTm(self, value):
		self._NgnTtlTm = value if type(value) != base_types.auto else self.make_default("NgnTtlTm")

	@NgnTtlTm.deleter
	def NgnTtlTm(self):
		del self._NgnTtlTm
		self._NgnTtlTm = None

	@property
	def RfrgrtnHrs(self):
		return self._RfrgrtnHrs

	@RfrgrtnHrs.setter
	def RfrgrtnHrs(self, value):
		self._RfrgrtnHrs = value if type(value) != base_types.auto else self.make_default("RfrgrtnHrs")

	@RfrgrtnHrs.deleter
	def RfrgrtnHrs(self):
		del self._RfrgrtnHrs
		self._RfrgrtnHrs = None

	@property
	def RfrgrtnTmprtr(self):
		return self._RfrgrtnTmprtr

	@RfrgrtnTmprtr.setter
	def RfrgrtnTmprtr(self, value):
		self._RfrgrtnTmprtr = value if type(value) != base_types.auto else self.make_default("RfrgrtnTmprtr")

	@RfrgrtnTmprtr.deleter
	def RfrgrtnTmprtr(self):
		del self._RfrgrtnTmprtr
		self._RfrgrtnTmprtr = None

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