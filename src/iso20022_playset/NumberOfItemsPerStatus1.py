import base_types
import ReportItemStatus1Code
import Max15NumericText

class NumberOfItemsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_NbOfItms", "_Sts"]
	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if type(value) != auto else self.make_default("NbOfItms")

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ReportItemStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

