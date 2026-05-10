from . import base_types
import Number
import YesNoIndicator

class TimeFrame7Choice(base_types._BaseFieldType):

	__slots__ = ["_TPlus", "_Prepmt"]
	@property
	def TPlus(self):
		return self._TPlus

	@TPlus.setter
	def TPlus(self, value):
		self._TPlus = value if type(value) != auto else self.make_default("TPlus")

	@TPlus.deleter
	def TPlus(self):
		del self._TPlus
		self._TPlus = None

	@property
	def Prepmt(self):
		return self._Prepmt

	@Prepmt.setter
	def Prepmt(self, value):
		self._Prepmt = value if type(value) != auto else self.make_default("Prepmt")

	@Prepmt.deleter
	def Prepmt(self):
		del self._Prepmt
		self._Prepmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prepmt', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))

