# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginPortfolio3
from . import PortfolioCode3Choice

class CollateralPortfolioCode5Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnPrtflCd", "_Prtfl"]
	@property
	def MrgnPrtflCd(self):
		return self._MrgnPrtflCd

	@MrgnPrtflCd.setter
	def MrgnPrtflCd(self, value):
		self._MrgnPrtflCd = value if value is not None else base_types.UninitialisedField(self, 'MrgnPrtflCd', MarginPortfolio3, False)

	@MrgnPrtflCd.deleter
	def MrgnPrtflCd(self):
		del self._MrgnPrtflCd
		self._MrgnPrtflCd = base_types.UninitialisedField(self, 'MrgnPrtflCd', MarginPortfolio3, False)

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if value is not None else base_types.UninitialisedField(self, 'Prtfl', PortfolioCode3Choice, False)

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = base_types.UninitialisedField(self, 'Prtfl', PortfolioCode3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnPrtflCd', type=MarginPortfolio3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtfl', type=PortfolioCode3Choice, min=0, max=1, mutex_group=1, array=False),
	))