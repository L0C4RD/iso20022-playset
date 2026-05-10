from . import base_types
from .SecurityCSDLinkMaintenanceRequestV01 import SecurityCSDLinkMaintenanceRequestV01

class REDA_046_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctyCSDLkMntncReq"]
		@property
		def SctyCSDLkMntncReq(self):
			return self._SctyCSDLkMntncReq

		@SctyCSDLkMntncReq.setter
		def SctyCSDLkMntncReq(self, value):
			self._SctyCSDLkMntncReq = value if type(value) != auto else self.make_default("SctyCSDLkMntncReq")

		@SctyCSDLkMntncReq.deleter
		def SctyCSDLkMntncReq(self):
			del self._SctyCSDLkMntncReq
			self._SctyCSDLkMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyCSDLkMntncReq', type=SecurityCSDLinkMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

