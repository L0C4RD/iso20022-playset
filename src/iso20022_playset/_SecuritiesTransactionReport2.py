# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import Max52Text
from . import RecordTechnicalData2
from . import SupplementaryData1

class SecuritiesTransactionReport2(base_types._BaseFieldType):

	__slots__ = ["_ExctgPty", "_SplmtryData", "_SubmitgPty", "_TechAttrbts", "_TxId"]
	@property
	def ExctgPty(self):
		return self._ExctgPty

	@ExctgPty.setter
	def ExctgPty(self, value):
		self._ExctgPty = value if value is not None else base_types.UninitialisedField(self, 'ExctgPty', LEIIdentifier, False)

	@ExctgPty.deleter
	def ExctgPty(self):
		del self._ExctgPty
		self._ExctgPty = base_types.UninitialisedField(self, 'ExctgPty', LEIIdentifier, False)

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
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgPty', LEIIdentifier, False)

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = base_types.UninitialisedField(self, 'SubmitgPty', LEIIdentifier, False)

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData2, False)

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = base_types.UninitialisedField(self, 'TechAttrbts', RecordTechnicalData2, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
	))