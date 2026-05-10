import base_types
import CollateralManagementCancellationStatusV05

class COLR_006_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollMgmtCxlSts"]
		@property
		def CollMgmtCxlSts(self):
			return self._CollMgmtCxlSts

		@CollMgmtCxlSts.setter
		def CollMgmtCxlSts(self, value):
			self._CollMgmtCxlSts = value if type(value) != auto else self.make_default("CollMgmtCxlSts")

		@CollMgmtCxlSts.deleter
		def CollMgmtCxlSts(self):
			del self._CollMgmtCxlSts
			self._CollMgmtCxlSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollMgmtCxlSts', type=CollateralManagementCancellationStatusV05, min=1, max=1, mutex_group=None, array=False),
		))

