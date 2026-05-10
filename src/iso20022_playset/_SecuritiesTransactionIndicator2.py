from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ReportingWaiverType1Code import ReportingWaiverType1Code
from ._ReportingWaiverType3Code import ReportingWaiverType3Code
from ._Side5Code import Side5Code

class SecuritiesTransactionIndicator2(base_types._BaseFieldType):

	__slots__ = ["_ShrtSellgInd", "_SctiesFincgTxInd", "_WvrInd", "_OTCPstTradInd", "_RskRdcgTx"]
	@property
	def OTCPstTradInd(self):
		return self._OTCPstTradInd

	@OTCPstTradInd.setter
	def OTCPstTradInd(self, value):
		self._OTCPstTradInd = value if type(value) != base_types.auto else self.make_default("OTCPstTradInd")

	@OTCPstTradInd.deleter
	def OTCPstTradInd(self):
		del self._OTCPstTradInd
		self._OTCPstTradInd = None

	@property
	def RskRdcgTx(self):
		return self._RskRdcgTx

	@RskRdcgTx.setter
	def RskRdcgTx(self, value):
		self._RskRdcgTx = value if type(value) != base_types.auto else self.make_default("RskRdcgTx")

	@RskRdcgTx.deleter
	def RskRdcgTx(self):
		del self._RskRdcgTx
		self._RskRdcgTx = None

	@property
	def SctiesFincgTxInd(self):
		return self._SctiesFincgTxInd

	@SctiesFincgTxInd.setter
	def SctiesFincgTxInd(self, value):
		self._SctiesFincgTxInd = value if type(value) != base_types.auto else self.make_default("SctiesFincgTxInd")

	@SctiesFincgTxInd.deleter
	def SctiesFincgTxInd(self):
		del self._SctiesFincgTxInd
		self._SctiesFincgTxInd = None

	@property
	def ShrtSellgInd(self):
		return self._ShrtSellgInd

	@ShrtSellgInd.setter
	def ShrtSellgInd(self, value):
		self._ShrtSellgInd = value if type(value) != base_types.auto else self.make_default("ShrtSellgInd")

	@ShrtSellgInd.deleter
	def ShrtSellgInd(self):
		del self._ShrtSellgInd
		self._ShrtSellgInd = None

	@property
	def WvrInd(self):
		return self._WvrInd

	@WvrInd.setter
	def WvrInd(self, value):
		self._WvrInd = value if type(value) != base_types.auto else self.make_default("WvrInd")

	@WvrInd.deleter
	def WvrInd(self):
		del self._WvrInd
		self._WvrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OTCPstTradInd', type=ReportingWaiverType3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RskRdcgTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtSellgInd', type=Side5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WvrInd', type=ReportingWaiverType1Code, min=0, max=None, mutex_group=None, array=True),
	))

