# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Counterparty39
from . import ISODateTime
from . import Max140Text
from . import Max52Text
from . import SupplementaryData1

class CollateralMarginError4(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflId", "_CtrPty", "_RptgDtTm", "_SplmtryData", "_TechRcrdId"]
	@property
	def CollPrtflId(self):
		return self._CollPrtflId

	@CollPrtflId.setter
	def CollPrtflId(self, value):
		self._CollPrtflId = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflId', Max52Text, False)

	@CollPrtflId.deleter
	def CollPrtflId(self):
		del self._CollPrtflId
		self._CollPrtflId = base_types.UninitialisedField(self, 'CollPrtflId', Max52Text, False)

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', Counterparty39, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', Counterparty39, False)

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrtflId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=Counterparty39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))