# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MICIdentifier
from . import Max350Text
from . import PercentageRate

class TradingUnderWaiversPercentage1(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_TradgUdrWvrPctg", "_TradgVn"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if value is not None else base_types.UninitialisedField(self, 'Dsclmr', Max350Text, False)

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = base_types.UninitialisedField(self, 'Dsclmr', Max350Text, False)

	@property
	def TradgUdrWvrPctg(self):
		return self._TradgUdrWvrPctg

	@TradgUdrWvrPctg.setter
	def TradgUdrWvrPctg(self, value):
		self._TradgUdrWvrPctg = value if value is not None else base_types.UninitialisedField(self, 'TradgUdrWvrPctg', PercentageRate, False)

	@TradgUdrWvrPctg.deleter
	def TradgUdrWvrPctg(self):
		del self._TradgUdrWvrPctg
		self._TradgUdrWvrPctg = base_types.UninitialisedField(self, 'TradgUdrWvrPctg', PercentageRate, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgUdrWvrPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))