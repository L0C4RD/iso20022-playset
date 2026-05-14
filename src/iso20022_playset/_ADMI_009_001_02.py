from . import base_types
from ._StaticDataRequestV02 import StaticDataRequestV02

class ADMI_009_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StatcDataReq"]
		@property
		def StatcDataReq(self):
			return self._StatcDataReq

		@StatcDataReq.setter
		def StatcDataReq(self, value):
			self._StatcDataReq = value if type(value) != base_types.auto else self.make_default("StatcDataReq")

		@StatcDataReq.deleter
		def StatcDataReq(self):
			del self._StatcDataReq
			self._StatcDataReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StatcDataReq', type=StaticDataRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

