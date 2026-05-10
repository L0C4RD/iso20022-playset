import base_types
import NettingCutOffReferenceDataUpdateRequestV02

class REDA_060_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NetgCutOffRefDataUpdReq"]
		@property
		def NetgCutOffRefDataUpdReq(self):
			return self._NetgCutOffRefDataUpdReq

		@NetgCutOffRefDataUpdReq.setter
		def NetgCutOffRefDataUpdReq(self, value):
			self._NetgCutOffRefDataUpdReq = value if type(value) != auto else self.make_default("NetgCutOffRefDataUpdReq")

		@NetgCutOffRefDataUpdReq.deleter
		def NetgCutOffRefDataUpdReq(self):
			del self._NetgCutOffRefDataUpdReq
			self._NetgCutOffRefDataUpdReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetgCutOffRefDataUpdReq', type=NettingCutOffReferenceDataUpdateRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

