from . import base_types
import MaintenanceDelegationResponseV08

class CATM_006_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MntncDlgtnRspn"]
		@property
		def MntncDlgtnRspn(self):
			return self._MntncDlgtnRspn

		@MntncDlgtnRspn.setter
		def MntncDlgtnRspn(self, value):
			self._MntncDlgtnRspn = value if type(value) != auto else self.make_default("MntncDlgtnRspn")

		@MntncDlgtnRspn.deleter
		def MntncDlgtnRspn(self):
			del self._MntncDlgtnRspn
			self._MntncDlgtnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MntncDlgtnRspn', type=MaintenanceDelegationResponseV08, min=1, max=1, mutex_group=None, array=False),
		))

