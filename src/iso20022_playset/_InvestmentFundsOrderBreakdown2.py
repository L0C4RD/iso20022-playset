# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import OrderBreakdownType1Choice

class InvestmentFundsOrderBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_OrdrBrkdwnTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def OrdrBrkdwnTp(self):
		return self._OrdrBrkdwnTp

	@OrdrBrkdwnTp.setter
	def OrdrBrkdwnTp(self, value):
		self._OrdrBrkdwnTp = value if value is not None else base_types.UninitialisedField(self, 'OrdrBrkdwnTp', OrderBreakdownType1Choice, False)

	@OrdrBrkdwnTp.deleter
	def OrdrBrkdwnTp(self):
		del self._OrdrBrkdwnTp
		self._OrdrBrkdwnTp = base_types.UninitialisedField(self, 'OrdrBrkdwnTp', OrderBreakdownType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBrkdwnTp', type=OrderBreakdownType1Choice, min=1, max=1, mutex_group=None, array=False),
	))