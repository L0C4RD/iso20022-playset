from . import base_types
from .CollateralValueQueryV02 import CollateralValueQueryV02

class COLR_001_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollValQry"]
		@property
		def CollValQry(self):
			return self._CollValQry

		@CollValQry.setter
		def CollValQry(self, value):
			self._CollValQry = value if type(value) != auto else self.make_default("CollValQry")

		@CollValQry.deleter
		def CollValQry(self):
			del self._CollValQry
			self._CollValQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValQry', type=CollateralValueQueryV02, min=1, max=1, mutex_group=None, array=False),
		))

