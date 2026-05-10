from . import base_types
import TerminalManagementRejectionV05

class CATM_004_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TermnlMgmtRjctn"]
		@property
		def TermnlMgmtRjctn(self):
			return self._TermnlMgmtRjctn

		@TermnlMgmtRjctn.setter
		def TermnlMgmtRjctn(self, value):
			self._TermnlMgmtRjctn = value if type(value) != auto else self.make_default("TermnlMgmtRjctn")

		@TermnlMgmtRjctn.deleter
		def TermnlMgmtRjctn(self):
			del self._TermnlMgmtRjctn
			self._TermnlMgmtRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TermnlMgmtRjctn', type=TerminalManagementRejectionV05, min=1, max=1, mutex_group=None, array=False),
		))

