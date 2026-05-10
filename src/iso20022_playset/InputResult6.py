import base_types
import InputResultData6
import SaleCapabilities2Code
import InformationQualify1Code

class InputResult6(base_types._BaseFieldType):

	__slots__ = ["_DvcTp", "_InptRsltData", "_InfQlfr"]
	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if type(value) != auto else self.make_default("DvcTp")

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = None

	@property
	def InptRsltData(self):
		return self._InptRsltData

	@InptRsltData.setter
	def InptRsltData(self, value):
		self._InptRsltData = value if type(value) != auto else self.make_default("InptRsltData")

	@InptRsltData.deleter
	def InptRsltData(self):
		del self._InptRsltData
		self._InptRsltData = None

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if type(value) != auto else self.make_default("InfQlfr")

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcTp', type=SaleCapabilities2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptRsltData', type=InputResultData6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
	))

