from . import base_types
import Max35Text
import Number
import Max3NumericText

class DocumentIdentification6(base_types._BaseFieldType):

	__slots__ = ["_AmdmntSeqNb", "_Vrsn", "_Id"]
	@property
	def AmdmntSeqNb(self):
		return self._AmdmntSeqNb

	@AmdmntSeqNb.setter
	def AmdmntSeqNb(self, value):
		self._AmdmntSeqNb = value if type(value) != auto else self.make_default("AmdmntSeqNb")

	@AmdmntSeqNb.deleter
	def AmdmntSeqNb(self):
		del self._AmdmntSeqNb
		self._AmdmntSeqNb = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntSeqNb', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

