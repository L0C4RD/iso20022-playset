from . import base_types
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .Max2000Text import Max2000Text
from .AutoExtension1 import AutoExtension1
from .YesNoIndicator import YesNoIndicator

class ExpiryTerms2(base_types._BaseFieldType):

	__slots__ = ["_Cond", "_AutoXtnsn", "_OpnEnddInd", "_DtTm"]
	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def AutoXtnsn(self):
		return self._AutoXtnsn

	@AutoXtnsn.setter
	def AutoXtnsn(self, value):
		self._AutoXtnsn = value if type(value) != auto else self.make_default("AutoXtnsn")

	@AutoXtnsn.deleter
	def AutoXtnsn(self):
		del self._AutoXtnsn
		self._AutoXtnsn = None

	@property
	def OpnEnddInd(self):
		return self._OpnEnddInd

	@OpnEnddInd.setter
	def OpnEnddInd(self, value):
		self._OpnEnddInd = value if type(value) != auto else self.make_default("OpnEnddInd")

	@OpnEnddInd.deleter
	def OpnEnddInd(self):
		del self._OpnEnddInd
		self._OpnEnddInd = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cond', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutoXtnsn', type=AutoExtension1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnEnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))

