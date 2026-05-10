import base_types
import UndertakingAmendmentResponseV01

class TSRV_008_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAmdmntRspn"]
		@property
		def UdrtkgAmdmntRspn(self):
			return self._UdrtkgAmdmntRspn

		@UdrtkgAmdmntRspn.setter
		def UdrtkgAmdmntRspn(self, value):
			self._UdrtkgAmdmntRspn = value if type(value) != auto else self.make_default("UdrtkgAmdmntRspn")

		@UdrtkgAmdmntRspn.deleter
		def UdrtkgAmdmntRspn(self):
			del self._UdrtkgAmdmntRspn
			self._UdrtkgAmdmntRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntRspn', type=UndertakingAmendmentResponseV01, min=1, max=1, mutex_group=None, array=False),
		))

