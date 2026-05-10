from . import base_types
from ._FraudDispositionResponseV03 import FraudDispositionResponseV03

class CAFR_004_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FrdDspstnRspn"]
		@property
		def FrdDspstnRspn(self):
			return self._FrdDspstnRspn

		@FrdDspstnRspn.setter
		def FrdDspstnRspn(self, value):
			self._FrdDspstnRspn = value if type(value) != base_types.auto else self.make_default("FrdDspstnRspn")

		@FrdDspstnRspn.deleter
		def FrdDspstnRspn(self):
			del self._FrdDspstnRspn
			self._FrdDspstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdDspstnRspn', type=FraudDispositionResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

