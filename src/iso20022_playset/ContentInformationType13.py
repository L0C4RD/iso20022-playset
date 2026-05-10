import base_types
import ContentType2Code
import SignedData4
import AuthenticatedData4

class ContentInformationType13(base_types._BaseFieldType):

	__slots__ = ["_SgndData", "_AuthntcdData", "_CnttTp"]
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

	@property
	def AuthntcdData(self):
		return self._AuthntcdData

	@AuthntcdData.setter
	def AuthntcdData(self, value):
		self._AuthntcdData = value if type(value) != auto else self.make_default("AuthntcdData")

	@AuthntcdData.deleter
	def AuthntcdData(self):
		del self._AuthntcdData
		self._AuthntcdData = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgndData', type=SignedData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcdData', type=AuthenticatedData4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
	))

