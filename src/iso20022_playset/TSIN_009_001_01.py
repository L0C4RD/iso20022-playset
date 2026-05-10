import base_types
import PartyRegistrationAndGuaranteeRequestV01

class TSIN_009_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyRegnAndGrntReq"]
		@property
		def PtyRegnAndGrntReq(self):
			return self._PtyRegnAndGrntReq

		@PtyRegnAndGrntReq.setter
		def PtyRegnAndGrntReq(self, value):
			self._PtyRegnAndGrntReq = value if type(value) != auto else self.make_default("PtyRegnAndGrntReq")

		@PtyRegnAndGrntReq.deleter
		def PtyRegnAndGrntReq(self):
			del self._PtyRegnAndGrntReq
			self._PtyRegnAndGrntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntReq', type=PartyRegistrationAndGuaranteeRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

