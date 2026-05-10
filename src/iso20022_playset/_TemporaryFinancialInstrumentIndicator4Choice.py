from . import base_types
from ._GenericIdentification47 import GenericIdentification47
from ._YesNoIndicator import YesNoIndicator

class TemporaryFinancialInstrumentIndicator4Choice(base_types._BaseFieldType):

	__slots__ = ["_TempInd", "_Prtry"]
	@property
	def TempInd(self):
		return self._TempInd

	@TempInd.setter
	def TempInd(self, value):
		self._TempInd = value if type(value) != base_types.auto else self.make_default("TempInd")

	@TempInd.deleter
	def TempInd(self):
		del self._TempInd
		self._TempInd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TempInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
	))

