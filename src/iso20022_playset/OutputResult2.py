import base_types
import InformationQualify1Code
import ResponseType11
import UserInterface4Code

class OutputResult2(base_types._BaseFieldType):

	__slots__ = ["_Rspn", "_DvcTp", "_InfQlfr"]
	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

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
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTp', type=UserInterface4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
	))

