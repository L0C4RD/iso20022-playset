from . import base_types
from ._DocumentNumber13 import DocumentNumber13
from ._DocumentNumber21 import DocumentNumber21

class StatusOrStatement13Choice(base_types._BaseFieldType):

	__slots__ = ["_Stmt", "_StsAdvc"]
	@property
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if type(value) != base_types.auto else self.make_default("Stmt")

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = None

	@property
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if type(value) != base_types.auto else self.make_default("StsAdvc")

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Stmt', type=DocumentNumber13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StsAdvc', type=DocumentNumber21, min=0, max=1, mutex_group=1, array=False),
	))

