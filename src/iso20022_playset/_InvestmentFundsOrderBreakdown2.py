from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._OrderBreakdownType1Choice import OrderBreakdownType1Choice

class InvestmentFundsOrderBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_OrdrBrkdwnTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def OrdrBrkdwnTp(self):
		return self._OrdrBrkdwnTp

	@OrdrBrkdwnTp.setter
	def OrdrBrkdwnTp(self, value):
		self._OrdrBrkdwnTp = value if type(value) != base_types.auto else self.make_default("OrdrBrkdwnTp")

	@OrdrBrkdwnTp.deleter
	def OrdrBrkdwnTp(self):
		del self._OrdrBrkdwnTp
		self._OrdrBrkdwnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrBrkdwnTp', type=OrderBreakdownType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

