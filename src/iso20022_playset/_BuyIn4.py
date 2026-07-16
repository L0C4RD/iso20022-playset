# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat15Choice
from . import ISODate
from . import YesNoIndicator

class BuyIn4(base_types._BaseFieldType):

	__slots__ = ["_BuyInRvrsnDt", "_CxlLmtDt", "_WrngInd", "_XpctdBuyInDt"]
	@property
	def BuyInRvrsnDt(self):
		return self._BuyInRvrsnDt

	@BuyInRvrsnDt.setter
	def BuyInRvrsnDt(self, value):
		self._BuyInRvrsnDt = value if value is not None else base_types.UninitialisedField(self, 'BuyInRvrsnDt', ISODate, False)

	@BuyInRvrsnDt.deleter
	def BuyInRvrsnDt(self):
		del self._BuyInRvrsnDt
		self._BuyInRvrsnDt = base_types.UninitialisedField(self, 'BuyInRvrsnDt', ISODate, False)

	@property
	def CxlLmtDt(self):
		return self._CxlLmtDt

	@CxlLmtDt.setter
	def CxlLmtDt(self, value):
		self._CxlLmtDt = value if value is not None else base_types.UninitialisedField(self, 'CxlLmtDt', ISODate, False)

	@CxlLmtDt.deleter
	def CxlLmtDt(self):
		del self._CxlLmtDt
		self._CxlLmtDt = base_types.UninitialisedField(self, 'CxlLmtDt', ISODate, False)

	@property
	def WrngInd(self):
		return self._WrngInd

	@WrngInd.setter
	def WrngInd(self, value):
		self._WrngInd = value if value is not None else base_types.UninitialisedField(self, 'WrngInd', YesNoIndicator, False)

	@WrngInd.deleter
	def WrngInd(self):
		del self._WrngInd
		self._WrngInd = base_types.UninitialisedField(self, 'WrngInd', YesNoIndicator, False)

	@property
	def XpctdBuyInDt(self):
		return self._XpctdBuyInDt

	@XpctdBuyInDt.setter
	def XpctdBuyInDt(self, value):
		self._XpctdBuyInDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdBuyInDt', DateFormat15Choice, False)

	@XpctdBuyInDt.deleter
	def XpctdBuyInDt(self):
		del self._XpctdBuyInDt
		self._XpctdBuyInDt = base_types.UninitialisedField(self, 'XpctdBuyInDt', DateFormat15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInRvrsnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlLmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WrngInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdBuyInDt', type=DateFormat15Choice, min=1, max=1, mutex_group=None, array=False),
	))