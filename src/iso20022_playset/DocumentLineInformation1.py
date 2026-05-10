from . import base_types
from .DocumentLineIdentification1 import DocumentLineIdentification1
from .RemittanceAmount3 import RemittanceAmount3
from .Max2048Text import Max2048Text

class DocumentLineInformation1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Amt", "_Desc"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=DocumentLineIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=RemittanceAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))

