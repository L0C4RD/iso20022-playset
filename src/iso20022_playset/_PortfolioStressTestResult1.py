# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102
from . import GenericIdentification165
from . import TrueFalseIndicator

class PortfolioStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_Cover1Flg", "_Cover2Flg", "_PrtflId", "_RawStrssLoss", "_StrssLoss"]
	@property
	def Cover1Flg(self):
		return self._Cover1Flg

	@Cover1Flg.setter
	def Cover1Flg(self, value):
		self._Cover1Flg = value if value is not None else base_types.UninitialisedField(self, 'Cover1Flg', TrueFalseIndicator, False)

	@Cover1Flg.deleter
	def Cover1Flg(self):
		del self._Cover1Flg
		self._Cover1Flg = base_types.UninitialisedField(self, 'Cover1Flg', TrueFalseIndicator, False)

	@property
	def Cover2Flg(self):
		return self._Cover2Flg

	@Cover2Flg.setter
	def Cover2Flg(self, value):
		self._Cover2Flg = value if value is not None else base_types.UninitialisedField(self, 'Cover2Flg', TrueFalseIndicator, False)

	@Cover2Flg.deleter
	def Cover2Flg(self):
		del self._Cover2Flg
		self._Cover2Flg = base_types.UninitialisedField(self, 'Cover2Flg', TrueFalseIndicator, False)

	@property
	def PrtflId(self):
		return self._PrtflId

	@PrtflId.setter
	def PrtflId(self, value):
		self._PrtflId = value if value is not None else base_types.UninitialisedField(self, 'PrtflId', GenericIdentification165, False)

	@PrtflId.deleter
	def PrtflId(self):
		del self._PrtflId
		self._PrtflId = base_types.UninitialisedField(self, 'PrtflId', GenericIdentification165, False)

	@property
	def RawStrssLoss(self):
		return self._RawStrssLoss

	@RawStrssLoss.setter
	def RawStrssLoss(self, value):
		self._RawStrssLoss = value if value is not None else base_types.UninitialisedField(self, 'RawStrssLoss', AmountAndDirection102, False)

	@RawStrssLoss.deleter
	def RawStrssLoss(self):
		del self._RawStrssLoss
		self._RawStrssLoss = base_types.UninitialisedField(self, 'RawStrssLoss', AmountAndDirection102, False)

	@property
	def StrssLoss(self):
		return self._StrssLoss

	@StrssLoss.setter
	def StrssLoss(self, value):
		self._StrssLoss = value if value is not None else base_types.UninitialisedField(self, 'StrssLoss', AmountAndDirection102, False)

	@StrssLoss.deleter
	def StrssLoss(self):
		del self._StrssLoss
		self._StrssLoss = base_types.UninitialisedField(self, 'StrssLoss', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cover1Flg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cover2Flg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RawStrssLoss', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))