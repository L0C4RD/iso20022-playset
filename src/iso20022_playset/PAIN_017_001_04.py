from . import base_types
from .MandateCopyRequestV04 import MandateCopyRequestV04

class PAIN_017_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MndtCpyReq"]
		@property
		def MndtCpyReq(self):
			return self._MndtCpyReq

		@MndtCpyReq.setter
		def MndtCpyReq(self, value):
			self._MndtCpyReq = value if type(value) != auto else self.make_default("MndtCpyReq")

		@MndtCpyReq.deleter
		def MndtCpyReq(self):
			del self._MndtCpyReq
			self._MndtCpyReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtCpyReq', type=MandateCopyRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

