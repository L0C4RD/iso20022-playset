# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISINOct2015Identifier
from . import ISODate
from . import Max350Text
from . import PercentageRate
from . import Period4Choice
from . import TradingUnderWaiversPercentage1

class VolumeCapResult1(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_Id", "_LastUpdDt", "_RptgPrd", "_TradgUdrWvrBrkdwn", "_TradgUdrWvrPctg", "_TtlTradgVol"]
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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def LastUpdDt(self):
		return self._LastUpdDt

	@LastUpdDt.setter
	def LastUpdDt(self, value):
		self._LastUpdDt = value if value is not None else base_types.UninitialisedField(self, 'LastUpdDt', ISODate, False)

	@LastUpdDt.deleter
	def LastUpdDt(self):
		del self._LastUpdDt
		self._LastUpdDt = base_types.UninitialisedField(self, 'LastUpdDt', ISODate, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@property
	def TradgUdrWvrBrkdwn(self):
		return self._TradgUdrWvrBrkdwn

	@TradgUdrWvrBrkdwn.setter
	def TradgUdrWvrBrkdwn(self, value):
		self._TradgUdrWvrBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'TradgUdrWvrBrkdwn', TradingUnderWaiversPercentage1, True)

	@TradgUdrWvrBrkdwn.deleter
	def TradgUdrWvrBrkdwn(self):
		del self._TradgUdrWvrBrkdwn
		self._TradgUdrWvrBrkdwn = base_types.UninitialisedField(self, 'TradgUdrWvrBrkdwn', TradingUnderWaiversPercentage1, True)

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
	def TtlTradgVol(self):
		return self._TtlTradgVol

	@TtlTradgVol.setter
	def TtlTradgVol(self, value):
		self._TtlTradgVol = value if value is not None else base_types.UninitialisedField(self, 'TtlTradgVol', ActiveCurrencyAndAmount, False)

	@TtlTradgVol.deleter
	def TtlTradgVol(self):
		del self._TtlTradgVol
		self._TtlTradgVol = base_types.UninitialisedField(self, 'TtlTradgVol', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgUdrWvrBrkdwn', type=TradingUnderWaiversPercentage1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgUdrWvrPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTradgVol', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))