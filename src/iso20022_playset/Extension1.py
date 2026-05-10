from . import base_types
import Max350Text

class Extension1(base_types._BaseFieldType):

	__slots__ = ["_Txt", "_PlcAndNm"]
	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	@property
	def PlcAndNm(self):
		return self._PlcAndNm

	@PlcAndNm.setter
	def PlcAndNm(self, value):
		self._PlcAndNm = value if type(value) != auto else self.make_default("PlcAndNm")

	@PlcAndNm.deleter
	def PlcAndNm(self):
		del self._PlcAndNm
		self._PlcAndNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Txt', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcAndNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

