from . import base_types
from .ISODateTime import ISODateTime
from .CollateralPortfolioCode6Choice import CollateralPortfolioCode6Choice
from .CollateralisationType3Code import CollateralisationType3Code

class MarginCollateralReport5(base_types._BaseFieldType):

	__slots__ = ["_TmStmp", "_CollstnCtgy", "_CollPrtflCd"]
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
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if type(value) != base_types.auto else self.make_default("CollPrtflCd")

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnCtgy', type=CollateralisationType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode6Choice, min=1, max=1, mutex_group=None, array=False),
	))

