import base_types
import ApplicationSpecifics1
import ManifestData2
import Max256Text
import PayloadData2

class PayloadDescription2(base_types._BaseFieldType):

	__slots__ = ["_PyldTp", "_ApplSpcfcs", "_PyldData", "_MnfstData"]
	@property
	def PyldTp(self):
		return self._PyldTp

	@PyldTp.setter
	def PyldTp(self, value):
		self._PyldTp = value if type(value) != auto else self.make_default("PyldTp")

	@PyldTp.deleter
	def PyldTp(self):
		del self._PyldTp
		self._PyldTp = None

	@property
	def ApplSpcfcs(self):
		return self._ApplSpcfcs

	@ApplSpcfcs.setter
	def ApplSpcfcs(self, value):
		self._ApplSpcfcs = value if type(value) != auto else self.make_default("ApplSpcfcs")

	@ApplSpcfcs.deleter
	def ApplSpcfcs(self):
		del self._ApplSpcfcs
		self._ApplSpcfcs = None

	@property
	def PyldData(self):
		return self._PyldData

	@PyldData.setter
	def PyldData(self, value):
		self._PyldData = value if type(value) != auto else self.make_default("PyldData")

	@PyldData.deleter
	def PyldData(self):
		del self._PyldData
		self._PyldData = None

	@property
	def MnfstData(self):
		return self._MnfstData

	@MnfstData.setter
	def MnfstData(self, value):
		self._MnfstData = value if type(value) != auto else self.make_default("MnfstData")

	@MnfstData.deleter
	def MnfstData(self):
		del self._MnfstData
		self._MnfstData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyldTp', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplSpcfcs', type=ApplicationSpecifics1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyldData', type=PayloadData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnfstData', type=ManifestData2, min=0, max=None, mutex_group=None, array=True),
	))

