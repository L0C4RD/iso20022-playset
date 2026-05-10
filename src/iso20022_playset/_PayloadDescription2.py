from . import base_types
from ._PayloadData2 import PayloadData2
from ._Max256Text import Max256Text
from ._ManifestData2 import ManifestData2
from ._ApplicationSpecifics1 import ApplicationSpecifics1

class PayloadDescription2(base_types._BaseFieldType):

	__slots__ = ["_PyldData", "_PyldTp", "_MnfstData", "_ApplSpcfcs"]
	@property
	def PyldData(self):
		return self._PyldData

	@PyldData.setter
	def PyldData(self, value):
		self._PyldData = value if type(value) != base_types.auto else self.make_default("PyldData")

	@PyldData.deleter
	def PyldData(self):
		del self._PyldData
		self._PyldData = None

	@property
	def PyldTp(self):
		return self._PyldTp

	@PyldTp.setter
	def PyldTp(self, value):
		self._PyldTp = value if type(value) != base_types.auto else self.make_default("PyldTp")

	@PyldTp.deleter
	def PyldTp(self):
		del self._PyldTp
		self._PyldTp = None

	@property
	def MnfstData(self):
		return self._MnfstData

	@MnfstData.setter
	def MnfstData(self, value):
		self._MnfstData = value if type(value) != base_types.auto else self.make_default("MnfstData")

	@MnfstData.deleter
	def MnfstData(self):
		del self._MnfstData
		self._MnfstData = None

	@property
	def ApplSpcfcs(self):
		return self._ApplSpcfcs

	@ApplSpcfcs.setter
	def ApplSpcfcs(self, value):
		self._ApplSpcfcs = value if type(value) != base_types.auto else self.make_default("ApplSpcfcs")

	@ApplSpcfcs.deleter
	def ApplSpcfcs(self):
		del self._ApplSpcfcs
		self._ApplSpcfcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyldData', type=PayloadData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyldTp', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnfstData', type=ManifestData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplSpcfcs', type=ApplicationSpecifics1, min=0, max=1, mutex_group=None, array=False),
	))

