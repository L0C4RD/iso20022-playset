import base_types
import Max35Text
import Max3NumericText
import BICIdentification1
import Number

class DocumentIdentification4(base_types._BaseFieldType):

	__slots__ = ["_Vrsn", "_Id", "_DocIndx", "_Submitr"]
	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

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
	def DocIndx(self):
		return self._DocIndx

	@DocIndx.setter
	def DocIndx(self, value):
		self._DocIndx = value if type(value) != auto else self.make_default("DocIndx")

	@DocIndx.deleter
	def DocIndx(self):
		del self._DocIndx
		self._DocIndx = None

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if type(value) != auto else self.make_default("Submitr")

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vrsn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocIndx', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

