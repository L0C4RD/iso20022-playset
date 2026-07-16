# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Channel1Choice
from . import DocumentFormat1Choice
from . import UndertakingDocumentType2Choice
from . import YesNoIndicator

class Document10(base_types._BaseFieldType):

	__slots__ = ["_CpyInd", "_DocFrmt", "_DocTp", "_PresntnChanl", "_SgndInd"]
	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if value is not None else base_types.UninitialisedField(self, 'CpyInd', YesNoIndicator, False)

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = base_types.UninitialisedField(self, 'CpyInd', YesNoIndicator, False)

	@property
	def DocFrmt(self):
		return self._DocFrmt

	@DocFrmt.setter
	def DocFrmt(self, value):
		self._DocFrmt = value if value is not None else base_types.UninitialisedField(self, 'DocFrmt', DocumentFormat1Choice, False)

	@DocFrmt.deleter
	def DocFrmt(self):
		del self._DocFrmt
		self._DocFrmt = base_types.UninitialisedField(self, 'DocFrmt', DocumentFormat1Choice, False)

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if value is not None else base_types.UninitialisedField(self, 'DocTp', UndertakingDocumentType2Choice, False)

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = base_types.UninitialisedField(self, 'DocTp', UndertakingDocumentType2Choice, False)

	@property
	def PresntnChanl(self):
		return self._PresntnChanl

	@PresntnChanl.setter
	def PresntnChanl(self, value):
		self._PresntnChanl = value if value is not None else base_types.UninitialisedField(self, 'PresntnChanl', Channel1Choice, False)

	@PresntnChanl.deleter
	def PresntnChanl(self):
		del self._PresntnChanl
		self._PresntnChanl = base_types.UninitialisedField(self, 'PresntnChanl', Channel1Choice, False)

	@property
	def SgndInd(self):
		return self._SgndInd

	@SgndInd.setter
	def SgndInd(self, value):
		self._SgndInd = value if value is not None else base_types.UninitialisedField(self, 'SgndInd', YesNoIndicator, False)

	@SgndInd.deleter
	def SgndInd(self):
		del self._SgndInd
		self._SgndInd = base_types.UninitialisedField(self, 'SgndInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocFrmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=UndertakingDocumentType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnChanl', type=Channel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))