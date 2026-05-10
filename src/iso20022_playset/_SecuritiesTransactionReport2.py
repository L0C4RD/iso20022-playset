from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._Max52Text import Max52Text
from ._RecordTechnicalData2 import RecordTechnicalData2
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesTransactionReport2(base_types._BaseFieldType):

	__slots__ = ["_ExctgPty", "_SplmtryData", "_SubmitgPty", "_TechAttrbts", "_TxId"]
	@property
	def ExctgPty(self):
		return self._ExctgPty

	@ExctgPty.setter
	def ExctgPty(self, value):
		self._ExctgPty = value if type(value) != base_types.auto else self.make_default("ExctgPty")

	@ExctgPty.deleter
	def ExctgPty(self):
		del self._ExctgPty
		self._ExctgPty = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if type(value) != base_types.auto else self.make_default("SubmitgPty")

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = None

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if type(value) != base_types.auto else self.make_default("TechAttrbts")

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=RecordTechnicalData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
	))

