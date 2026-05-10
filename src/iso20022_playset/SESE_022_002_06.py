from . import base_types
import SecuritiesStatusOrStatementQueryStatusAdvice002V06

class SESE_022_002_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesStsOrStmtQryStsAdvc"]
		@property
		def SctiesStsOrStmtQryStsAdvc(self):
			return self._SctiesStsOrStmtQryStsAdvc

		@SctiesStsOrStmtQryStsAdvc.setter
		def SctiesStsOrStmtQryStsAdvc(self, value):
			self._SctiesStsOrStmtQryStsAdvc = value if type(value) != auto else self.make_default("SctiesStsOrStmtQryStsAdvc")

		@SctiesStsOrStmtQryStsAdvc.deleter
		def SctiesStsOrStmtQryStsAdvc(self):
			del self._SctiesStsOrStmtQryStsAdvc
			self._SctiesStsOrStmtQryStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesStsOrStmtQryStsAdvc', type=SecuritiesStatusOrStatementQueryStatusAdvice002V06, min=1, max=1, mutex_group=None, array=False),
		))

