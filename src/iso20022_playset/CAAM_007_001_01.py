import base_types
import HostToATMRequestV01

class CAAM_007_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_HstToATMReq"]
		@property
		def HstToATMReq(self):
			return self._HstToATMReq

		@HstToATMReq.setter
		def HstToATMReq(self, value):
			self._HstToATMReq = value if type(value) != auto else self.make_default("HstToATMReq")

		@HstToATMReq.deleter
		def HstToATMReq(self):
			del self._HstToATMReq
			self._HstToATMReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='HstToATMReq', type=HostToATMRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

