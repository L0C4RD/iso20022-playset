# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionReport2
from . import SecuritiesTransactionReport7
from . import SupplementaryData1

class ReportingTransactionType3Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxl", "_New", "_SplmtryData"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', SecuritiesTransactionReport2, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', SecuritiesTransactionReport2, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', SecuritiesTransactionReport7, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', SecuritiesTransactionReport7, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=SecuritiesTransactionReport2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=SecuritiesTransactionReport7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=1, array=True),
	))