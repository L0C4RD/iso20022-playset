# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeRepositoryReportingType1Code
from . import TrueFalseIndicator

class ReconciliationFlag2(base_types._BaseFieldType):

	__slots__ = ["_BothCtrPtiesRptg", "_CollRcncltnSts", "_LnRcncltnSts", "_ModSts", "_PairdSts", "_RptTp"]
	@property
	def BothCtrPtiesRptg(self):
		return self._BothCtrPtiesRptg

	@BothCtrPtiesRptg.setter
	def BothCtrPtiesRptg(self, value):
		self._BothCtrPtiesRptg = value if value is not None else base_types.UninitialisedField(self, 'BothCtrPtiesRptg', TrueFalseIndicator, False)

	@BothCtrPtiesRptg.deleter
	def BothCtrPtiesRptg(self):
		del self._BothCtrPtiesRptg
		self._BothCtrPtiesRptg = base_types.UninitialisedField(self, 'BothCtrPtiesRptg', TrueFalseIndicator, False)

	@property
	def CollRcncltnSts(self):
		return self._CollRcncltnSts

	@CollRcncltnSts.setter
	def CollRcncltnSts(self, value):
		self._CollRcncltnSts = value if value is not None else base_types.UninitialisedField(self, 'CollRcncltnSts', TrueFalseIndicator, False)

	@CollRcncltnSts.deleter
	def CollRcncltnSts(self):
		del self._CollRcncltnSts
		self._CollRcncltnSts = base_types.UninitialisedField(self, 'CollRcncltnSts', TrueFalseIndicator, False)

	@property
	def LnRcncltnSts(self):
		return self._LnRcncltnSts

	@LnRcncltnSts.setter
	def LnRcncltnSts(self, value):
		self._LnRcncltnSts = value if value is not None else base_types.UninitialisedField(self, 'LnRcncltnSts', TrueFalseIndicator, False)

	@LnRcncltnSts.deleter
	def LnRcncltnSts(self):
		del self._LnRcncltnSts
		self._LnRcncltnSts = base_types.UninitialisedField(self, 'LnRcncltnSts', TrueFalseIndicator, False)

	@property
	def ModSts(self):
		return self._ModSts

	@ModSts.setter
	def ModSts(self, value):
		self._ModSts = value if value is not None else base_types.UninitialisedField(self, 'ModSts', TrueFalseIndicator, False)

	@ModSts.deleter
	def ModSts(self):
		del self._ModSts
		self._ModSts = base_types.UninitialisedField(self, 'ModSts', TrueFalseIndicator, False)

	@property
	def PairdSts(self):
		return self._PairdSts

	@PairdSts.setter
	def PairdSts(self, value):
		self._PairdSts = value if value is not None else base_types.UninitialisedField(self, 'PairdSts', TrueFalseIndicator, False)

	@PairdSts.deleter
	def PairdSts(self):
		del self._PairdSts
		self._PairdSts = base_types.UninitialisedField(self, 'PairdSts', TrueFalseIndicator, False)

	@property
	def RptTp(self):
		return self._RptTp

	@RptTp.setter
	def RptTp(self, value):
		self._RptTp = value if value is not None else base_types.UninitialisedField(self, 'RptTp', TradeRepositoryReportingType1Code, False)

	@RptTp.deleter
	def RptTp(self):
		del self._RptTp
		self._RptTp = base_types.UninitialisedField(self, 'RptTp', TradeRepositoryReportingType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BothCtrPtiesRptg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollRcncltnSts', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnRcncltnSts', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModSts', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PairdSts', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTp', type=TradeRepositoryReportingType1Code, min=0, max=1, mutex_group=None, array=False),
	))