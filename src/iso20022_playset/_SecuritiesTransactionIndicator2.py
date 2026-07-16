# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportingWaiverType1Code
from . import ReportingWaiverType3Code
from . import Side5Code
from . import TrueFalseIndicator

class SecuritiesTransactionIndicator2(base_types._BaseFieldType):

	__slots__ = ["_OTCPstTradInd", "_RskRdcgTx", "_SctiesFincgTxInd", "_ShrtSellgInd", "_WvrInd"]
	@property
	def OTCPstTradInd(self):
		return self._OTCPstTradInd

	@OTCPstTradInd.setter
	def OTCPstTradInd(self, value):
		self._OTCPstTradInd = value if value is not None else base_types.UninitialisedField(self, 'OTCPstTradInd', ReportingWaiverType3Code, True)

	@OTCPstTradInd.deleter
	def OTCPstTradInd(self):
		del self._OTCPstTradInd
		self._OTCPstTradInd = base_types.UninitialisedField(self, 'OTCPstTradInd', ReportingWaiverType3Code, True)

	@property
	def RskRdcgTx(self):
		return self._RskRdcgTx

	@RskRdcgTx.setter
	def RskRdcgTx(self, value):
		self._RskRdcgTx = value if value is not None else base_types.UninitialisedField(self, 'RskRdcgTx', TrueFalseIndicator, False)

	@RskRdcgTx.deleter
	def RskRdcgTx(self):
		del self._RskRdcgTx
		self._RskRdcgTx = base_types.UninitialisedField(self, 'RskRdcgTx', TrueFalseIndicator, False)

	@property
	def SctiesFincgTxInd(self):
		return self._SctiesFincgTxInd

	@SctiesFincgTxInd.setter
	def SctiesFincgTxInd(self, value):
		self._SctiesFincgTxInd = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTxInd', TrueFalseIndicator, False)

	@SctiesFincgTxInd.deleter
	def SctiesFincgTxInd(self):
		del self._SctiesFincgTxInd
		self._SctiesFincgTxInd = base_types.UninitialisedField(self, 'SctiesFincgTxInd', TrueFalseIndicator, False)

	@property
	def ShrtSellgInd(self):
		return self._ShrtSellgInd

	@ShrtSellgInd.setter
	def ShrtSellgInd(self, value):
		self._ShrtSellgInd = value if value is not None else base_types.UninitialisedField(self, 'ShrtSellgInd', Side5Code, False)

	@ShrtSellgInd.deleter
	def ShrtSellgInd(self):
		del self._ShrtSellgInd
		self._ShrtSellgInd = base_types.UninitialisedField(self, 'ShrtSellgInd', Side5Code, False)

	@property
	def WvrInd(self):
		return self._WvrInd

	@WvrInd.setter
	def WvrInd(self, value):
		self._WvrInd = value if value is not None else base_types.UninitialisedField(self, 'WvrInd', ReportingWaiverType1Code, True)

	@WvrInd.deleter
	def WvrInd(self):
		del self._WvrInd
		self._WvrInd = base_types.UninitialisedField(self, 'WvrInd', ReportingWaiverType1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OTCPstTradInd', type=ReportingWaiverType3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RskRdcgTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtSellgInd', type=Side5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WvrInd', type=ReportingWaiverType1Code, min=0, max=None, mutex_group=None, array=True),
	))