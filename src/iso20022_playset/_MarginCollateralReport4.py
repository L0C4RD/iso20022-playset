from . import base_types
from ._CollateralPortfolioCode5Choice import CollateralPortfolioCode5Choice
from ._CollateralisationType3Code import CollateralisationType3Code
from ._ISODateTime import ISODateTime

class MarginCollateralReport4(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflCd", "_CollstnCtgy", "_TmStmp"]
	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if type(value) != base_types.auto else self.make_default("CollPrtflCd")

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = None

	@property
	def CollstnCtgy(self):
		return self._CollstnCtgy

	@CollstnCtgy.setter
	def CollstnCtgy(self, value):
		self._CollstnCtgy = value if type(value) != base_types.auto else self.make_default("CollstnCtgy")

	@CollstnCtgy.deleter
	def CollstnCtgy(self):
		del self._CollstnCtgy
		self._CollstnCtgy = None

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnCtgy', type=CollateralisationType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

