# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import ISODate
from . import MICIdentifier
from . import Max35Text
from . import NumberAndVolume2
from . import TrueFalseIndicator

class TransparencyDataReport13(base_types._BaseFieldType):

	__slots__ = ["_Id", "_RptgDt", "_Sspnsn", "_TechRcrdId", "_TradgVn", "_TxsExctd", "_TxsExctdExclgPreTradWvr", "_TxsExctdExclgPstTradLrgInScaleWvr"]
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
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if value is not None else base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = base_types.UninitialisedField(self, 'RptgDt', ISODate, False)

	@property
	def Sspnsn(self):
		return self._Sspnsn

	@Sspnsn.setter
	def Sspnsn(self, value):
		self._Sspnsn = value if value is not None else base_types.UninitialisedField(self, 'Sspnsn', TrueFalseIndicator, False)

	@Sspnsn.deleter
	def Sspnsn(self):
		del self._Sspnsn
		self._Sspnsn = base_types.UninitialisedField(self, 'Sspnsn', TrueFalseIndicator, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

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

	@property
	def TxsExctd(self):
		return self._TxsExctd

	@TxsExctd.setter
	def TxsExctd(self, value):
		self._TxsExctd = value if value is not None else base_types.UninitialisedField(self, 'TxsExctd', NumberAndVolume2, False)

	@TxsExctd.deleter
	def TxsExctd(self):
		del self._TxsExctd
		self._TxsExctd = base_types.UninitialisedField(self, 'TxsExctd', NumberAndVolume2, False)

	@property
	def TxsExctdExclgPreTradWvr(self):
		return self._TxsExctdExclgPreTradWvr

	@TxsExctdExclgPreTradWvr.setter
	def TxsExctdExclgPreTradWvr(self, value):
		self._TxsExctdExclgPreTradWvr = value if value is not None else base_types.UninitialisedField(self, 'TxsExctdExclgPreTradWvr', NumberAndVolume2, False)

	@TxsExctdExclgPreTradWvr.deleter
	def TxsExctdExclgPreTradWvr(self):
		del self._TxsExctdExclgPreTradWvr
		self._TxsExctdExclgPreTradWvr = base_types.UninitialisedField(self, 'TxsExctdExclgPreTradWvr', NumberAndVolume2, False)

	@property
	def TxsExctdExclgPstTradLrgInScaleWvr(self):
		return self._TxsExctdExclgPstTradLrgInScaleWvr

	@TxsExctdExclgPstTradLrgInScaleWvr.setter
	def TxsExctdExclgPstTradLrgInScaleWvr(self, value):
		self._TxsExctdExclgPstTradLrgInScaleWvr = value if value is not None else base_types.UninitialisedField(self, 'TxsExctdExclgPstTradLrgInScaleWvr', NumberAndVolume2, False)

	@TxsExctdExclgPstTradLrgInScaleWvr.deleter
	def TxsExctdExclgPstTradLrgInScaleWvr(self):
		del self._TxsExctdExclgPstTradLrgInScaleWvr
		self._TxsExctdExclgPstTradLrgInScaleWvr = base_types.UninitialisedField(self, 'TxsExctdExclgPstTradLrgInScaleWvr', NumberAndVolume2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sspnsn', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctd', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctdExclgPreTradWvr', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsExctdExclgPstTradLrgInScaleWvr', type=NumberAndVolume2, min=1, max=1, mutex_group=None, array=False),
	))