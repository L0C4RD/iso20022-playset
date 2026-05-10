import base_types
import AutoExtension1
import DateAndDateTimeChoice
import YesNoIndicator
import Max2000Text

class ExpiryTerms1(base_types._BaseFieldType):

	__slots__ = ["_AutoXtnsn", "_DtTm", "_Cond", "_OpnEnddInd"]
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
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

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
	def OpnEnddInd(self):
		return self._OpnEnddInd

	@OpnEnddInd.setter
	def OpnEnddInd(self, value):
		self._OpnEnddInd = value if type(value) != auto else self.make_default("OpnEnddInd")

	@OpnEnddInd.deleter
	def OpnEnddInd(self):
		del self._OpnEnddInd
		self._OpnEnddInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutoXtnsn', type=AutoExtension1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnEnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

