from . import base_types
from .HostToATMAcknowledgementV01 import HostToATMAcknowledgementV01

class CAAM_008_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_HstToATMAck"]
		@property
		def HstToATMAck(self):
			return self._HstToATMAck

		@HstToATMAck.setter
		def HstToATMAck(self, value):
			self._HstToATMAck = value if type(value) != auto else self.make_default("HstToATMAck")

		@HstToATMAck.deleter
		def HstToATMAck(self):
			del self._HstToATMAck
			self._HstToATMAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='HstToATMAck', type=HostToATMAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))

