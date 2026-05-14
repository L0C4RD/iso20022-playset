from . import base_types
from ._CollateralValueCreationRequestV01 import CollateralValueCreationRequestV01

class REDA_024_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollValCreReq"]
		@property
		def CollValCreReq(self):
			return self._CollValCreReq

		@CollValCreReq.setter
		def CollValCreReq(self, value):
			self._CollValCreReq = value if type(value) != base_types.auto else self.make_default("CollValCreReq")

		@CollValCreReq.deleter
		def CollValCreReq(self):
			del self._CollValCreReq
			self._CollValCreReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValCreReq', type=CollateralValueCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

