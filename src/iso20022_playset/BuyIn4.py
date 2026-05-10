from . import base_types
import ISODate
import YesNoIndicator
import DateFormat15Choice

class BuyIn4(base_types._BaseFieldType):

	__slots__ = ["_WrngInd", "_XpctdBuyInDt", "_BuyInRvrsnDt", "_CxlLmtDt"]
	@property
	def WrngInd(self):
		return self._WrngInd

	@WrngInd.setter
	def WrngInd(self, value):
		self._WrngInd = value if type(value) != auto else self.make_default("WrngInd")

	@WrngInd.deleter
	def WrngInd(self):
		del self._WrngInd
		self._WrngInd = None

	@property
	def XpctdBuyInDt(self):
		return self._XpctdBuyInDt

	@XpctdBuyInDt.setter
	def XpctdBuyInDt(self, value):
		self._XpctdBuyInDt = value if type(value) != auto else self.make_default("XpctdBuyInDt")

	@XpctdBuyInDt.deleter
	def XpctdBuyInDt(self):
		del self._XpctdBuyInDt
		self._XpctdBuyInDt = None

	@property
	def BuyInRvrsnDt(self):
		return self._BuyInRvrsnDt

	@BuyInRvrsnDt.setter
	def BuyInRvrsnDt(self, value):
		self._BuyInRvrsnDt = value if type(value) != auto else self.make_default("BuyInRvrsnDt")

	@BuyInRvrsnDt.deleter
	def BuyInRvrsnDt(self):
		del self._BuyInRvrsnDt
		self._BuyInRvrsnDt = None

	@property
	def CxlLmtDt(self):
		return self._CxlLmtDt

	@CxlLmtDt.setter
	def CxlLmtDt(self, value):
		self._CxlLmtDt = value if type(value) != auto else self.make_default("CxlLmtDt")

	@CxlLmtDt.deleter
	def CxlLmtDt(self):
		del self._CxlLmtDt
		self._CxlLmtDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='WrngInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdBuyInDt', type=DateFormat15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInRvrsnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlLmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

