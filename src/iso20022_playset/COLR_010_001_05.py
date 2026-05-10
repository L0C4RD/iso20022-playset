import base_types
import CollateralSubstitutionRequestV05

class COLR_010_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CollSbstitnReq"]
		@property
		def CollSbstitnReq(self):
			return self._CollSbstitnReq

		@CollSbstitnReq.setter
		def CollSbstitnReq(self, value):
			self._CollSbstitnReq = value if type(value) != auto else self.make_default("CollSbstitnReq")

		@CollSbstitnReq.deleter
		def CollSbstitnReq(self):
			del self._CollSbstitnReq
			self._CollSbstitnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnReq', type=CollateralSubstitutionRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

