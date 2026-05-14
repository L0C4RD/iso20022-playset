from . import base_types
from ._ReconciliationInitiationV05 import ReconciliationInitiationV05

class CAAD_005_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RcncltnInitn"]
		@property
		def RcncltnInitn(self):
			return self._RcncltnInitn

		@RcncltnInitn.setter
		def RcncltnInitn(self, value):
			self._RcncltnInitn = value if type(value) != base_types.auto else self.make_default("RcncltnInitn")

		@RcncltnInitn.deleter
		def RcncltnInitn(self):
			del self._RcncltnInitn
			self._RcncltnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnInitn', type=ReconciliationInitiationV05, min=1, max=1, mutex_group=None, array=False),
		))

