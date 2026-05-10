import base_types
import SupplementaryDataEnvelope1
import Max350Text

class SupplementaryData1(base_types._BaseFieldType):

	__slots__ = ["_Envlp", "_PlcAndNm"]
	@property
	def Envlp(self):
		return self._Envlp

	@Envlp.setter
	def Envlp(self, value):
		self._Envlp = value if type(value) != auto else self.make_default("Envlp")

	@Envlp.deleter
	def Envlp(self):
		del self._Envlp
		self._Envlp = None

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
		base_types.FieldEntry(name='Envlp', type=SupplementaryDataEnvelope1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcAndNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

