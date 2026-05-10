from . import base_types
import PortfolioCode5Choice

class MarginPortfolio3(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnPrtflCd", "_VartnMrgnPrtflCd"]
	@property
	def InitlMrgnPrtflCd(self):
		return self._InitlMrgnPrtflCd

	@InitlMrgnPrtflCd.setter
	def InitlMrgnPrtflCd(self, value):
		self._InitlMrgnPrtflCd = value if type(value) != auto else self.make_default("InitlMrgnPrtflCd")

	@InitlMrgnPrtflCd.deleter
	def InitlMrgnPrtflCd(self):
		del self._InitlMrgnPrtflCd
		self._InitlMrgnPrtflCd = None

	@property
	def VartnMrgnPrtflCd(self):
		return self._VartnMrgnPrtflCd

	@VartnMrgnPrtflCd.setter
	def VartnMrgnPrtflCd(self, value):
		self._VartnMrgnPrtflCd = value if type(value) != auto else self.make_default("VartnMrgnPrtflCd")

	@VartnMrgnPrtflCd.deleter
	def VartnMrgnPrtflCd(self):
		del self._VartnMrgnPrtflCd
		self._VartnMrgnPrtflCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnPrtflCd', type=PortfolioCode5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPrtflCd', type=PortfolioCode5Choice, min=0, max=1, mutex_group=None, array=False),
	))

