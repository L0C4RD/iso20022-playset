from . import base_types
import CollateralSubstitutionResponseV05

class COLR_011_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollSbstitnRspn"]
		@property
		def CollSbstitnRspn(self):
			return self._CollSbstitnRspn

		@CollSbstitnRspn.setter
		def CollSbstitnRspn(self, value):
			self._CollSbstitnRspn = value if type(value) != auto else self.make_default("CollSbstitnRspn")

		@CollSbstitnRspn.deleter
		def CollSbstitnRspn(self):
			del self._CollSbstitnRspn
			self._CollSbstitnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnRspn', type=CollateralSubstitutionResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

