import base_types
import PartyRegistrationAndGuaranteeAcknowledgementV01

class TSIN_012_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyRegnAndGrntAck"]
		@property
		def PtyRegnAndGrntAck(self):
			return self._PtyRegnAndGrntAck

		@PtyRegnAndGrntAck.setter
		def PtyRegnAndGrntAck(self, value):
			self._PtyRegnAndGrntAck = value if type(value) != auto else self.make_default("PtyRegnAndGrntAck")

		@PtyRegnAndGrntAck.deleter
		def PtyRegnAndGrntAck(self):
			del self._PtyRegnAndGrntAck
			self._PtyRegnAndGrntAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyRegnAndGrntAck', type=PartyRegistrationAndGuaranteeAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))

