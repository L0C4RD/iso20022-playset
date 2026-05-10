from . import base_types
from .PortfolioCode3Choice import PortfolioCode3Choice
from .MarginPortfolio4 import MarginPortfolio4

class CollateralPortfolioCode6Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnPrtflCd", "_Prtfl"]
	@property
	def MrgnPrtflCd(self):
		return self._MrgnPrtflCd

	@MrgnPrtflCd.setter
	def MrgnPrtflCd(self, value):
		self._MrgnPrtflCd = value if type(value) != auto else self.make_default("MrgnPrtflCd")

	@MrgnPrtflCd.deleter
	def MrgnPrtflCd(self):
		del self._MrgnPrtflCd
		self._MrgnPrtflCd = None

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnPrtflCd', type=MarginPortfolio4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtfl', type=PortfolioCode3Choice, min=0, max=1, mutex_group=1, array=False),
	))

