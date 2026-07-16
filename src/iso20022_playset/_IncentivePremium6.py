# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat3Choice
from . import IncentivePremiumType2Choice
from . import Max350Text
from . import PriceRateOrAmount8Choice

class IncentivePremium6(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Desc", "_PmtDt", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', PriceRateOrAmount8Choice, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', PriceRateOrAmount8Choice, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDt', DateFormat3Choice, False)

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = base_types.UninitialisedField(self, 'PmtDt', DateFormat3Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', IncentivePremiumType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', IncentivePremiumType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=PriceRateOrAmount8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IncentivePremiumType2Choice, min=1, max=1, mutex_group=None, array=False),
	))