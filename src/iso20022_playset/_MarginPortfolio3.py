# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PortfolioCode5Choice

class MarginPortfolio3(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnPrtflCd", "_VartnMrgnPrtflCd"]
	@property
	def InitlMrgnPrtflCd(self):
		return self._InitlMrgnPrtflCd

	@InitlMrgnPrtflCd.setter
	def InitlMrgnPrtflCd(self, value):
		self._InitlMrgnPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnPrtflCd', PortfolioCode5Choice, False)

	@InitlMrgnPrtflCd.deleter
	def InitlMrgnPrtflCd(self):
		del self._InitlMrgnPrtflCd
		self._InitlMrgnPrtflCd = base_types.UninitialisedField(self, 'InitlMrgnPrtflCd', PortfolioCode5Choice, False)

	@property
	def VartnMrgnPrtflCd(self):
		return self._VartnMrgnPrtflCd

	@VartnMrgnPrtflCd.setter
	def VartnMrgnPrtflCd(self, value):
		self._VartnMrgnPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPrtflCd', PortfolioCode5Choice, False)

	@VartnMrgnPrtflCd.deleter
	def VartnMrgnPrtflCd(self):
		del self._VartnMrgnPrtflCd
		self._VartnMrgnPrtflCd = base_types.UninitialisedField(self, 'VartnMrgnPrtflCd', PortfolioCode5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnPrtflCd', type=PortfolioCode5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPrtflCd', type=PortfolioCode5Choice, min=0, max=1, mutex_group=None, array=False),
	))