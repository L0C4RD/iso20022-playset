from . import base_types
from ._FraudDispositionInitiationV03 import FraudDispositionInitiationV03

class CAFR_003_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FrdDspstnInitn"]
		@property
		def FrdDspstnInitn(self):
			return self._FrdDspstnInitn

		@FrdDspstnInitn.setter
		def FrdDspstnInitn(self, value):
			self._FrdDspstnInitn = value if type(value) != base_types.auto else self.make_default("FrdDspstnInitn")

		@FrdDspstnInitn.deleter
		def FrdDspstnInitn(self):
			del self._FrdDspstnInitn
			self._FrdDspstnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdDspstnInitn', type=FraudDispositionInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

