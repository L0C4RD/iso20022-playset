from . import base_types
from ._HighFrequencyTradingProfile1 import HighFrequencyTradingProfile1
from ._InvestorProfileStatus1Choice import InvestorProfileStatus1Choice
from ._MarketMakerProfile2 import MarketMakerProfile2
from ._ProfileType1Choice import ProfileType1Choice
from ._TreasuryProfile1 import TreasuryProfile1

class InvestorProfile2(base_types._BaseFieldType):

	__slots__ = ["_HghFrqcyTradg", "_MktMakr", "_Sts", "_Tp", "_Trsr"]
	@property
	def HghFrqcyTradg(self):
		return self._HghFrqcyTradg

	@HghFrqcyTradg.setter
	def HghFrqcyTradg(self, value):
		self._HghFrqcyTradg = value if type(value) != base_types.auto else self.make_default("HghFrqcyTradg")

	@HghFrqcyTradg.deleter
	def HghFrqcyTradg(self):
		del self._HghFrqcyTradg
		self._HghFrqcyTradg = None

	@property
	def MktMakr(self):
		return self._MktMakr

	@MktMakr.setter
	def MktMakr(self, value):
		self._MktMakr = value if type(value) != base_types.auto else self.make_default("MktMakr")

	@MktMakr.deleter
	def MktMakr(self):
		del self._MktMakr
		self._MktMakr = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Trsr(self):
		return self._Trsr

	@Trsr.setter
	def Trsr(self, value):
		self._Trsr = value if type(value) != base_types.auto else self.make_default("Trsr")

	@Trsr.deleter
	def Trsr(self):
		del self._Trsr
		self._Trsr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghFrqcyTradg', type=HighFrequencyTradingProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktMakr', type=MarketMakerProfile2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=InvestorProfileStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProfileType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trsr', type=TreasuryProfile1, min=0, max=1, mutex_group=None, array=False),
	))

