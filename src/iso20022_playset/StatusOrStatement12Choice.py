from . import base_types
import DocumentNumber19
import DocumentNumber14

class StatusOrStatement12Choice(base_types._BaseFieldType):

	__slots__ = ["_Stmt", "_StsAdvc"]
	@property
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if type(value) != auto else self.make_default("Stmt")

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = None

	@property
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if type(value) != auto else self.make_default("StsAdvc")

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Stmt', type=DocumentNumber14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StsAdvc', type=DocumentNumber19, min=0, max=1, mutex_group=1, array=False),
	))

