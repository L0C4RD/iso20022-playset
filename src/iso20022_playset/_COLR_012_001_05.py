from . import base_types
from ._CollateralSubstitutionConfirmationV05 import CollateralSubstitutionConfirmationV05

class COLR_012_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollSbstitnConf"]
		@property
		def CollSbstitnConf(self):
			return self._CollSbstitnConf

		@CollSbstitnConf.setter
		def CollSbstitnConf(self, value):
			self._CollSbstitnConf = value if type(value) != base_types.auto else self.make_default("CollSbstitnConf")

		@CollSbstitnConf.deleter
		def CollSbstitnConf(self):
			del self._CollSbstitnConf
			self._CollSbstitnConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnConf', type=CollateralSubstitutionConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))

