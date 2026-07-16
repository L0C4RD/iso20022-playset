# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentNumber14
from . import DocumentNumber19

class StatusOrStatement12Choice(base_types._BaseFieldType):

	__slots__ = ["_Stmt", "_StsAdvc"]
	@property
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if value is not None else base_types.UninitialisedField(self, 'Stmt', DocumentNumber14, False)

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = base_types.UninitialisedField(self, 'Stmt', DocumentNumber14, False)

	@property
	def StsAdvc(self):
		return self._StsAdvc

	@StsAdvc.setter
	def StsAdvc(self, value):
		self._StsAdvc = value if value is not None else base_types.UninitialisedField(self, 'StsAdvc', DocumentNumber19, False)

	@StsAdvc.deleter
	def StsAdvc(self):
		del self._StsAdvc
		self._StsAdvc = base_types.UninitialisedField(self, 'StsAdvc', DocumentNumber19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Stmt', type=DocumentNumber14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StsAdvc', type=DocumentNumber19, min=0, max=1, mutex_group=1, array=False),
	))