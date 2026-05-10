from . import base_types
from ._ResendRequestV01 import ResendRequestV01

class ADMI_006_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RsndReq"]
		@property
		def RsndReq(self):
			return self._RsndReq

		@RsndReq.setter
		def RsndReq(self, value):
			self._RsndReq = value if type(value) != base_types.auto else self.make_default("RsndReq")

		@RsndReq.deleter
		def RsndReq(self):
			del self._RsndReq
			self._RsndReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RsndReq', type=ResendRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

