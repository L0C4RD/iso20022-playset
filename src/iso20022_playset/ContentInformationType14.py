from . import base_types
import SignedData4
import ContentType2Code

class ContentInformationType14(base_types._BaseFieldType):

	__slots__ = ["_CnttTp", "_SgndData"]
	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if type(value) != auto else self.make_default("CnttTp")

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = None

	@property
	def SgndData(self):
		return self._SgndData

	@SgndData.setter
	def SgndData(self, value):
		self._SgndData = value if type(value) != auto else self.make_default("SgndData")

	@SgndData.deleter
	def SgndData(self):
		del self._SgndData
		self._SgndData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndData', type=SignedData4, min=1, max=1, mutex_group=None, array=False),
	))

