from . import base_types
from ._Max15NumericText import Max15NumericText
from ._ReportItemStatus1Code import ReportItemStatus1Code

class NumberOfItemsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_NbOfItms"]
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

	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if type(value) != base_types.auto else self.make_default("NbOfItms")

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=ReportItemStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

