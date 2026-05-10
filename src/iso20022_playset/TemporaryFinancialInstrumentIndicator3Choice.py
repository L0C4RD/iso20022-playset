import base_types
import GenericIdentification30
import YesNoIndicator

class TemporaryFinancialInstrumentIndicator3Choice(base_types._BaseFieldType):

	__slots__ = ["_TempInd", "_Prtry"]
	@property
	def TempInd(self):
		return self._TempInd

	@TempInd.setter
	def TempInd(self, value):
		self._TempInd = value if type(value) != auto else self.make_default("TempInd")

	@TempInd.deleter
	def TempInd(self):
		del self._TempInd
		self._TempInd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TempInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))

