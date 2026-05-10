from . import base_types
import Party50Choice
import YesNoIndicator
import Max35Text

class Case6(base_types._BaseFieldType):

	__slots__ = ["_ReopCaseIndctn", "_Cretr", "_Id"]
	@property
	def ReopCaseIndctn(self):
		return self._ReopCaseIndctn

	@ReopCaseIndctn.setter
	def ReopCaseIndctn(self, value):
		self._ReopCaseIndctn = value if type(value) != auto else self.make_default("ReopCaseIndctn")

	@ReopCaseIndctn.deleter
	def ReopCaseIndctn(self):
		del self._ReopCaseIndctn
		self._ReopCaseIndctn = None

	@property
	def Cretr(self):
		return self._Cretr

	@Cretr.setter
	def Cretr(self, value):
		self._Cretr = value if type(value) != auto else self.make_default("Cretr")

	@Cretr.deleter
	def Cretr(self):
		del self._Cretr
		self._Cretr = None

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
		base_types.FieldEntry(name='ReopCaseIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cretr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

