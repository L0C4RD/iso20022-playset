from . import base_types
from .UndertakingDocumentType2Choice import UndertakingDocumentType2Choice
from .Channel1Choice import Channel1Choice
from .DocumentFormat1Choice import DocumentFormat1Choice
from .YesNoIndicator import YesNoIndicator

class Document10(base_types._BaseFieldType):

	__slots__ = ["_DocTp", "_PresntnChanl", "_SgndInd", "_CpyInd", "_DocFrmt"]
	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	@property
	def PresntnChanl(self):
		return self._PresntnChanl

	@PresntnChanl.setter
	def PresntnChanl(self, value):
		self._PresntnChanl = value if type(value) != auto else self.make_default("PresntnChanl")

	@PresntnChanl.deleter
	def PresntnChanl(self):
		del self._PresntnChanl
		self._PresntnChanl = None

	@property
	def SgndInd(self):
		return self._SgndInd

	@SgndInd.setter
	def SgndInd(self, value):
		self._SgndInd = value if type(value) != auto else self.make_default("SgndInd")

	@SgndInd.deleter
	def SgndInd(self):
		del self._SgndInd
		self._SgndInd = None

	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if type(value) != auto else self.make_default("CpyInd")

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = None

	@property
	def DocFrmt(self):
		return self._DocFrmt

	@DocFrmt.setter
	def DocFrmt(self, value):
		self._DocFrmt = value if type(value) != auto else self.make_default("DocFrmt")

	@DocFrmt.deleter
	def DocFrmt(self):
		del self._DocFrmt
		self._DocFrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocTp', type=UndertakingDocumentType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnChanl', type=Channel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocFrmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
	))

