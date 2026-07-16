# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralPortfolioCode5Choice
from . import CollateralisationType3Code
from . import ISODateTime

class MarginCollateralReport4(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflCd", "_CollstnCtgy", "_TmStmp"]
	@property
	def CollPrtflCd(self):
		return self._CollPrtflCd

	@CollPrtflCd.setter
	def CollPrtflCd(self, value):
		self._CollPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode5Choice, False)

	@CollPrtflCd.deleter
	def CollPrtflCd(self):
		del self._CollPrtflCd
		self._CollPrtflCd = base_types.UninitialisedField(self, 'CollPrtflCd', CollateralPortfolioCode5Choice, False)

	@property
	def CollstnCtgy(self):
		return self._CollstnCtgy

	@CollstnCtgy.setter
	def CollstnCtgy(self, value):
		self._CollstnCtgy = value if value is not None else base_types.UninitialisedField(self, 'CollstnCtgy', CollateralisationType3Code, False)

	@CollstnCtgy.deleter
	def CollstnCtgy(self):
		del self._CollstnCtgy
		self._CollstnCtgy = base_types.UninitialisedField(self, 'CollstnCtgy', CollateralisationType3Code, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrtflCd', type=CollateralPortfolioCode5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollstnCtgy', type=CollateralisationType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))