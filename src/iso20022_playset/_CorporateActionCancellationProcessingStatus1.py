from . import base_types
from ._Max350Text import Max350Text
from ._ProcessedStatus5FormatChoice import ProcessedStatus5FormatChoice

class CorporateActionCancellationProcessingStatus1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Sts"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ProcessedStatus5FormatChoice, min=1, max=1, mutex_group=None, array=False),
	))

