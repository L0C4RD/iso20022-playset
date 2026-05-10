import base_types
import ContentInformationType39
import Max1025Text
import Max100KBinary

class ExternallyDefinedData5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Id", "_PrtctdVal", "_Val"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def PrtctdVal(self):
		return self._PrtctdVal

	@PrtctdVal.setter
	def PrtctdVal(self, value):
		self._PrtctdVal = value if type(value) != auto else self.make_default("PrtctdVal")

	@PrtctdVal.deleter
	def PrtctdVal(self):
		del self._PrtctdVal
		self._PrtctdVal = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max1025Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdVal', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))

